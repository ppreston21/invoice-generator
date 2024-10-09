import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os


# Step 1: Generate invoices from CSV with multiple items per invoice
def generate_invoice(sales_data, output_pdf):
    print(f"Generating invoice for sales order: {sales_data.iloc[0]['Sales order']}")

    pdf = canvas.Canvas(output_pdf, pagesize=letter)
    pdf.setFont("Helvetica", 12)

    # Company header info
    pdf.drawString(100, 750, "Globex Corporation")
    pdf.drawString(100, 735, "111 Scorpio Way, Cypress Creek")
    pdf.drawString(100, 720, "Email: hank.scorpio@globex.com")
    pdf.drawString(100, 705, "Phone: (123) 555-1234")

    # Client info (take the first item in the group for common info)
    client_data = sales_data.iloc[0]
    pdf.drawString(100, 670, f"Invoice for: {client_data['Client Name']}")
    pdf.drawString(100, 655, f"Address: {client_data['Address']}")
    pdf.drawString(100, 640, f"Email: {client_data['Email']}")
    pdf.drawString(100, 625, f"Phone: {client_data['Phone']}")
    pdf.drawString(100, 610, f"Date: {client_data['Date']}")

    # Invoice table headers
    pdf.drawString(100, 580, "Item")
    pdf.drawString(300, 580, "Description")
    pdf.drawString(500, 580, "Amount")

    # Invoice details: loop through items for the same sales order
    y_position = 560
    for _, item in sales_data.iterrows():
        pdf.drawString(100, y_position, item['Item'])
        pdf.drawString(300, y_position, item['Description'])
        pdf.drawString(500, y_position, item['Amount'])
        y_position -= 20  # move down for the next item

    # Footer
    pdf.drawString(100, 100, "Thank you for your business!")
    pdf.save()
    print(f"Invoice saved: {output_pdf}")


# Step 2: Read CSV and group by 'Sales order' to create individual invoices
def process_csv(file_path):
    df = pd.read_csv(file_path)
    grouped = df.groupby('Sales order')  # group by sales order to aggregate items for each invoice

    # Create an output directory for the PDFs
    output_dir = "invoices"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for sales_order, sales_data in grouped:
        file_name = f"invoice_{sales_order}.pdf"
        output_path = os.path.join(output_dir, file_name)
        generate_invoice(sales_data, output_path)


# Execute the process
process_csv("sales-orders.csv")
