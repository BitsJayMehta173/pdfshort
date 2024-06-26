from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def convert_txt_to_pdf(txt_file, pdf_file):
    c = canvas.Canvas(pdf_file, pagesize=letter)

    c.setFont("Helvetica", 12)

    with open(txt_file, 'r') as f:
        lines = f.readlines()
        y = 750  

        for line in lines:
            if y < 50:
                c.showPage()
                c.setFont("Helvetica", 12)
                y = 750  

            c.drawString(100, y, line.strip())  
            y -= 15  

    c.save()
txt_file = 'ianf.txt'
pdf_file = 'iaf.pdf'

convert_txt_to_pdf(txt_file, pdf_file)
