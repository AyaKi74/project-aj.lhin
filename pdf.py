from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import sqlite3

conn = sqlite3.connect('matchs.db')
cursor = conn.cursor()


def create_pdf(output_filename, records):
    # Create a PDF document
    c = canvas.Canvas(output_filename, pagesize=letter)

    # Add content to the PDF
    y_coordinate = 750
    for record in records:
        for field in record:
            c.drawString(100, y_coordinate, str(field))
            y_coordinate -= 20  # Move down by 20 units for each field
        y_coordinate -= 20  # Add some space between records

    # Save the PDF file
    c.save()

if __name__ == "__main__":
    output_filename = "database_records.pdf"
    
    # Connect to the SQLite database and execute a query
    
    cursor.execute('SELECT * FROM y ')
    results = cursor.fetchall()
    conn.close()

    create_pdf(output_filename, results)
    print(f"PDF saved as {output_filename}")
