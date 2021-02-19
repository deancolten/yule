import smtplib


class Mailer():
    def __init__(self, user, password):
        self.user = user
        self.password = password


class Gmailer(Mailer):
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def send_mail(self, subject, message, to_mail, from_mail=None):
        if from_mail:
            f_mail = from_mail
        else:
            f_mail = self.user
        port = 587
        msg = f"Subject: {subject}\n{message}"
        with smtplib.SMTP('smtp.gmail.com', port) as server:
            server.ehlo()
            server.starttls()
            server.login(user=self.user, password=self.password)
            server.sendmail(f_mail, to_mail, msg)
        return True
