from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def convert_txt_to_pdf(txt_file, pdf_file):
    # Create a canvas
    c = canvas.Canvas(pdf_file, pagesize=letter)

    # Set font and size
    c.setFont("Helvetica", 12)

    # Read text from the txt file
    with open(txt_file, 'r') as f:
        lines = f.readlines()
        y = 750  # Starting y position

        for line in lines:
            if y < 50:
                # Add a new page if remaining space is not sufficient
                c.showPage()
                c.setFont("Helvetica", 12)
                y = 750  # Reset y position for the new page

            c.drawString(100, y, line.strip())  # Write each line
            y -= 15  # Adjust y position for the next line

    # Save PDF
    c.save()

# Replace these with your file paths
txt_file = 'ianf.txt'
pdf_file = 'iaf.pdf'

convert_txt_to_pdf(txt_file, pdf_file)
