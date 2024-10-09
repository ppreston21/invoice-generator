import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd

# Step 1: Request invoice number input
invoice_number = input("Enter the invoice number (e.g., 00-001): ")

# Define the directory where the invoices are saved
invoice_dir = "invoices"
invoice_path = os.path.join(invoice_dir, f"invoice_{invoice_number}.pdf")

# Step 2: Get client details from the CSV (ensure it matches the invoice)
def get_client_details(invoice_number, csv_file="sales-orders.csv"):
    df = pd.read_csv(csv_file)
    client_data = df[df['Sales order'] == invoice_number].iloc[0]
    return client_data['Client Name'], client_data['Email']

try:
    client_name, client_email = get_client_details(invoice_number)
except IndexError:
    print(f"Invoice {invoice_number} not found.")
    exit()

# Step 3: Set up the email parameters
sender_email = "INSERT EMAIL HERE"
sender_password = "INSERT APP PASSWORD HERE"
subject = f"Invoice {invoice_number} - Globex Corporation"
body = f"Hello, {client_name}\n\nPlease find your invoice attached.\n\nBest regards,\nGlobex Corporation"

# Step 4: Prepare the email
def send_email(sender_email, sender_password, recipient_email, subject, body, attachment_path):
    # Set up the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the body text
    msg.attach(MIMEText(body, 'plain'))

    # Attach the PDF file
    with open(attachment_path, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(attachment_path)}")
        msg.attach(part)

    # Step 5: Connect to Gmail and send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print(f"Email sent to {recipient_email} with invoice {invoice_number}.")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

# Step 6: Check if the invoice exists and send the email
if os.path.exists(invoice_path):
    send_email(sender_email, sender_password, client_email, subject, body, invoice_path)
else:
    print(f"Invoice {invoice_number} not found in {invoice_dir}.")
