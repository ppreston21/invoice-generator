invoice-generator.py


Sales order grouping: The data is grouped by Sales order, so multiple purchases by the same client will appear on a single invoice.
Invoice formatting: The generate_invoice function now loops through all items associated with a given sales order and lists them with descriptions and amounts.
Y-axis management: The Y position for drawing strings (y_position) decreases for each new item so that multiple items are properly spaced.

To Run:
Make sure the CSV file path is correct (sales-orders.csv).
Run the script and check if the print statements appear, indicating the PDF generation process.
Check the invoices folder in your project directory for the generated PDF files.
Let me know if this solves the issue or if further troubleshooting is needed!


email-step.py

Key Details:
Input:
The script requests the invoice number (e.g., 00-001) from the user.
Client Information:
It uses pandas to fetch the Client Name and Email from the sales CSV to personalize the email.
Email Setup:
MIMEMultipart allows you to format the email with both text and attachments.
The PDF file is attached to the email.
SMTP for Gmail:
Connects to Gmail’s SMTP server (smtp.gmail.com on port 587).
Logs in with the sender's email and password to send the email.
Important: If you use two-factor authentication (2FA) on your Gmail account, you'll need to generate an app password instead of using your regular password.
Steps to Run:
Fill in the sender's email and password:

Replace "your_email@gmail.com" and "your_password" in the script with your Gmail credentials.
Prepare CSV:

Ensure your sales-orders.csv is present in the same folder or specify the correct path.
Check Output:

The script will check if the corresponding invoice file (invoice_00-001.pdf) exists.
If found, it will send the email with the attached invoice.
Run the script.

Would you like help adjusting this further or setting up your Gmail for this script?






