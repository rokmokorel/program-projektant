############################# MAIN.PY ######################################
#
# main program
# vpis podatkov iz SQLite baze v excel(.xlsx) datoteko
#
# MainWindow - osnovno okolje okoli gradnikov/widgetov
# Widget - gradnik funkcionalnosti
# Layout - prostor, kjer prebivajo gradniki
###########################################################################
from ui_zacetek import *
from ui_izberi import *
from ui_koncaj import *

# from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Ui_MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.uiZacetek = Ui_Zacetek()
        self.uiOkno = Ui_Izberi()
        
        self.show()
        self.zacni_tu()

    def zacni_tu(self):
        self.uiZacetek.setupUi(self)
        
        self.uiZacetek.novPopisBtn.clicked.connect(self.nadaljuj_tu)

    def nadaljuj_tu(self):
        self.uiOkno.setupUi(self)
        self.uiOkno.zakljuciZapisBtn.clicked.connect(self.zacni_tu)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    sys.exit(app.exec_())
