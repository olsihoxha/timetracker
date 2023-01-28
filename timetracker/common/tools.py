from django.db.models import Q
from rest_framework import serializers
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from timetracker.common.mail_conf import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
from timetracker.common.pdf_generator import generate_pdf

KEY_TO_NAME = {
    'id': 'ID',
    'working_date': 'Date',
    'task_description': 'Desc',
    'time_start': 'Started',
    'time_end': 'Ended',
    'user': 'Email',
    'task': 'Task',
}


def check_time_overlap(model, spec_date, given_times, user):
    query = Q()
    for time in given_times:
        query |= Q(time_start__lte=time, time_end__gte=time)

    result = model.objects.filter(query, working_date=spec_date, user=user)
    if result:
        raise serializers.ValidationError({"detail": "There is overlapping time"})


def query_to_list(query):
    field_names = [field.name for field in query.model._meta.fields]
    results = [[KEY_TO_NAME[field_name] for field_name in field_names]]
    # Iterate over the queryset and append the data to the results list
    for obj in query:
        results.append([str(getattr(obj, field)) for field in field_names])
    return results


def send_pdf_as_email(model_data, user_email):
    list_for_pdf = query_to_list(model_data)
    pdf_name = generate_pdf(list_for_pdf)
    send_email(pdf_name, user_email, "Employee Time", "Test Body")


def send_email(pdf_name, recipient_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_HOST_USER
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body))

    with open(pdf_name, "rb") as f:
        pdf_attachment = MIMEApplication(f.read(), _subtype="pdf")
        pdf_attachment.add_header('content-disposition', 'attachment', filename=pdf_name)
        msg.attach(pdf_attachment)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    server.sendmail(EMAIL_HOST_USER, recipient_email, msg.as_string())
    server.quit()
