import uuid

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph

TABLE_STYLE = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.white),
                          ('TEXTCOLOR', (0, 0), (-1, 0), colors.red),
                          ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                          ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                          ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                          ('BACKGROUND', (0, -1), (-1, -1), colors.white),
                          ('GRID', (0, 0), (-1, -1), 1, colors.black)])


def generate_pdf(table_data):
    file_name = f"pdfs/{uuid.uuid4()}.pdf"
    pdf_doc = SimpleDocTemplate(file_name, pagesize=A4,
                                rightMargin=20, leftMargin=20)

    title = Paragraph("Working time for the user")
    content = []
    table = Table(table_data, colWidths=(pdf_doc.pagesize[0] - 20) / 8)
    table.setStyle(TABLE_STYLE)
    table.spaceBefore = 30
    table.spaceAfter = 30

    content.append(title)
    content.append(table)

    pdf_doc.build(content)
    return file_name
