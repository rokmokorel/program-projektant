############################# mail.py ######################################
#
# razred za posiljanje maila s projektnimi podatki na podjetje
#
###########################################################################

import smtplib, ssl
from datetime import datetime

class Mail():
    def __init__(self):
        self.port = 587  # For starttls
        self.smtp_server = "smtp.gmail.com"
        self.posiljatelj = "6projektant@gmail.com"
        self.prejemnik = "rok.mokorel@gmail.com"
        self.geslo = 'projektmisija'

        self.sporocilo = ''

    def gen_sporocilo(self, slovar):
        podatki = {
        'Content-Type': 'text/html; charset=utf-8',
        'Content-Disposition': 'inline',
        'Content-Transfer-Encoding': '8bit',
        'From': self.prejemnik,
        'To': self.posiljatelj,
        'Date': datetime.now().strftime('%a, %d %b %Y  %H:%M:%S'),
        'Subject': f'PODATKI O PROJEKTU: {slovar["naziv"]}'}

        for polje, vrednost in podatki.items():
            self.sporocilo += f'{polje}: {vrednost}\n'
        
        self.sporocilo += f'\nNaziv: {slovar["naziv"]}<br>' \
        f'Lokacija: {slovar["lokacija"]}<br>' \
        f'Izvajalec: {slovar["izvajalec"]}<br>' \
        f'Pričetek: {slovar["pricetek"]}<br>' \
        f'Posebnosti: {slovar["posebnosti"]}<br>\n'
        return None

    def poslji(self):
        kontekst = ssl.create_default_context()
        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.ehlo()  # lahko izpustimo
            server.starttls(context=kontekst)
            server.ehlo()  # lahko izpustimo
            server.login(self.posiljatelj, self.geslo)
            server.sendmail(self.posiljatelj, self.prejemnik, \
                self.sporocilo.encode("utf8"))