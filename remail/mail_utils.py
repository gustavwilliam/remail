import smtplib
import ssl

PORT = 465  # For SSL


class Mail:
    def __init__(self, subject: str = "", body: str = "") -> None:
        self.subject = subject
        self.body = body

    @property
    def raw(self):
        return f"Subject: {self.subject}\n\n{self.body}"


def send(mail: Mail, sender_email: str, receiver_email: str, sender_password: str) -> None:
    context = ssl.create_default_context()  # Create a secure SSL context
    with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, mail.raw)
