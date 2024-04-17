import smtplib  # Importing the SMTP library for sending emails
from email import encoders  # Importing encoders for handling attachments
from email.mime.text import MIMEText  # Importing MIMEText for handling text
from email.mime.base import MIMEBase  # Importing MIMEBase for handling attachments
from email.mime.multipart import MIMEMultipart  # Importing MIMEMultipart for handling multipart messages

# Establishing a connection to the SMTP server (in this case, Gmail's SMTP server)
server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()  # Initiating the SMTP connection

# Retrieving the password from a text file
with open('password.txt', 'r') as f:
    password = f.read()

# Logging into the email account using the provided credentials
server.login('mail@gmail.com', password)

# Creating a multipart message
msg = MIMEMultipart()
msg['From'] = '<your_name>'  # Setting the sender's name
msg['To'] = '<targetmail@gmail.com>'  # Setting the recipient's email address
msg['Subject'] = '<your_subject>'  # Setting the email subject

# Reading the message content from a text file
with open('message.txt', 'r') as f:
    message = f.read()

# Attaching the message content to the email
msg.attach(MIMEText(message, 'plain'))

filename = '<attachment_file_name>'  # Defining the filename of the attachment
attachment = open(filename, 'rb')  # Opening the attachment file

# Creating a MIMEBase instance for the attachment
p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())  # Setting the payload of the attachment

encoders.encode_base64(p)  # Encoding the attachment
p.add_header('Content-Disposition', f'attachment', filename={filename})  # Adding header for attachment
msg.attach(p)  # Attaching the attachment to the email message

text = msg.as_string()  # Converting the email message to a string
server.sendmail('mail@gmail.com', 'targetmail@gmail.com', text)  # Sending the email
