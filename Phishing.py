from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


class Phising:

    def __init__(self):
        self.sender_address = input("Please type : Sender email addressc\n")
        self.sender_pass = input("Please type : Sender password\n")
        self.receiver_address = input("Please type : Receiver address\n")
        self.smtp_address = input("Please type : your mail vendor smtp address (Example : smtp.gmail.com)\n")
        self.smtp_port = input("Please type : your mail vendor smtp port (Example : 587)\n")
        self.mail_content = '''Team,
Because of recent cybersecurity threats that have been discovered in linux kernel , we have decided to update all linux machines to 
latest security patch , as such, we need everyone to ensure that your follow this tutorial.
                
1. Download the attached file.
                
2. Open the directory where you downloaded the file.
                
3.press right click and then choose open terminal here. 
                
4. type in the terminal sudo ./filename and type in your password.
                
We appreciate your attention to this URGENT matter.
                
--
                
Information Technology Services
                
'''

    def send_mail(self):
        subject = 'Urgent; Security Update'
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = self.sender_address
        message['To'] = self.receiver_address
        message['Subject'] = subject  # The subject line
        # The body and the attachments for the mail
        message.attach(MIMEText(self.mail_content, 'plain'))
        # Create SMTP session for sending the mail
        session = smtplib.SMTP(self.smtp_address, self.smtp_port)  # use gmail with port
        session.starttls()  # enable security
        session.login(self.sender_address, self.sender_pass)  # login with mail_id and password
        text = message.as_string()
        session.sendmail(self.sender_address, self.receiver_address, text)
        session.quit()
        print('Mail Sent')



if __name__ == '__main__':
    p = Phising()
    print(p.mail_content)
    p.send_mail()
