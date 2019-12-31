############################# mail.py ######################################
#
# razred za posiljanje maila s projektnimi podatki na podjetje
#
###########################################################################

import smtplib, ssl

class Mail():

    def __init__(self):
        self.port = 587  # For starttls
        self.smtp_server = "smtp.gmail.com"
        self.posiljatelj = "6projektant@gmail.com"
        self.prejemnik = "rok.mokorel@gmail.com"
        self.geslo = 'projektmisija'

        self.vsebina = """UPDATE projekta: projektant

        Sporočilo iz programa.
        """
        
    def sporocilo(self, objekt):
        self.podatki = objekt
        self.vsebina = """\
Subject: Hi there

This message is sent from Python."""

    def poslji(self):
        kontekst = ssl.create_default_context()
        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.ehlo()  # lahko izpustimo
            server.starttls(context=kontekst)
            server.ehlo()  # lahko izpustimo
            server.login(self.posiljatelj, self.geslo)
            server.sendmail(self.posiljatelj, self.prejemnik, self.vsebina)