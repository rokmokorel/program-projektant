############################# MAIN.PY ######################################
#
# main program
# vpis podatkov iz SQLite baze v excel(.xlsx) datoteko
#
# MainWindow - osnovno okolje okoli gradnikov/widgetov
# Widget - gradnik funkcionalnosti
# Layout - prostor, kjer prebivajo gradniki
#
###########################################################################

import sys
from collections import defaultdict
# from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

from ui_zacetek import *
from ui_izberi import *
from ui_projekt import *
from mail import *


class Ui_MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        # splosni podatki o projektantu in projektu
        self.podatki = defaultdict(lambda: '')
        self.mail = Mail()
        # pripravimo razrede za okna
        self.uiZacetek = Ui_Zacetek()
        self.uiProjekt = Ui_Projekt()
        self.uiOkno = Ui_Izberi()
        
        self.show()
        self.zacni_tu()

    def zacni_tu(self):
        self.uiZacetek.setupUi(self)
        self.uiZacetek.novPopisBtn.clicked.connect(self.opisi_projekt)

    def opisi_projekt(self):
        self.uiProjekt.setupUi(self)
        self.uiProjekt.nadaljujBtn.clicked.connect(self.info_projekt)
        self.uiProjekt.nadaljujBtn.clicked.connect(self.nadaljuj_tu)
        self.uiProjekt.nadaljujBtn.clicked.connect(self.mail_podatki)
    
    def nadaljuj_tu(self):
        self.uiOkno.setupUi(self)
        self.uiOkno.projekt = self.podatki
        # odpri dialog, lokacija excel datoteke
        self.uiOkno.lokacijaExcelBtn.clicked.connect(self.uiOkno.fileDialog)
        
        self.uiOkno.zakljuciZapisBtn.clicked.connect(self.zacni_tu)
        # self.uiOkno.zakljuciZapisBtn.clicked.connect(self.mail.poslji)

    def mail_podatki(self):
        print(self.mail.sporocilo(self.podatki))

    # posodobimo splosne podatke o projektu
    def info_projekt(self):
        for key, value in self.uiProjekt.vrni_vrednosti():
            self.podatki[key] = value

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    sys.exit(app.exec_())
