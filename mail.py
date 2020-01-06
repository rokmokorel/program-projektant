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
    # TODO: DEBUG, vrne sporocilo() takes 0 positional arguments but 1 was given
    def sporocilo(self, **objekt):
        self.vsebina =  f'NOVI PROJEKT: {objekt["naziv"]}, projektant: \
            {objekt["projektant"]}'\
            f''\
            f'Podatki o projektu: {objekt["naziv"]}'\
            f'Lokacija: {objekt["lokacija"]}'\
            f'Naročnik: {objekt["naročnik"]}'
        return self.vsebina

    def poslji(self):
        kontekst = ssl.create_default_context()
        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.ehlo()  # lahko izpustimo
            server.starttls(context=kontekst)
            server.ehlo()  # lahko izpustimo
            server.login(self.posiljatelj, self.geslo)
            server.sendmail(self.posiljatelj, self.prejemnik, self.vsebina)