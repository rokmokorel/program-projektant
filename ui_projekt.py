########################### ui_projekt.py ####################################
#
# razred okna za vnos podatkov o projektu
#
# MainWindow - osnovno okolje okoli gradnikov/widgetov
# Widget - gradnik funkcionalnosti
# Layout - prostor, kjer prebivajo gradniki
#
#############################################################################

from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QPlainTextEdit, QLabel
from PyQt5.QtCore import QRect, QSize
from PyQt5.QtGui import QFont


class Ui_Projekt(QWidget):
    
    def setupUi(self, MainWindow):
        self.centralWidget = QWidget(MainWindow)
        naslovLb = QLabel(self.centralWidget)
        naslovLb.setGeometry(QRect(40, 30, 230, 30))
        font = QFont()
        font.setPointSize(12)
        naslovLb.setFont(font)
        naslovLb.setText('Referenčni podatki o projektu')
        
        nazivLb = QLabel(self.centralWidget)
        nazivLb.setGeometry(QRect(40, 80, 150, 20))
        nazivLb.setText('Naziv projekta')
        self.nazivLe = QLineEdit(self.centralWidget)
        self.nazivLe.setGeometry(QRect(200, 80, 300, 20))
        
        narocnikLb = QLabel(self.centralWidget)
        narocnikLb.setGeometry(QRect(40, 115, 150, 20))
        narocnikLb.setText("Naročnik")
        self.narocnikLe = QLineEdit(self.centralWidget)
        self.narocnikLe.setGeometry(QRect(200, 115, 300, 20))

        lokacijaLb = QLabel(self.centralWidget)
        lokacijaLb.setGeometry(QRect(40, 150, 150, 20))
        lokacijaLb.setText("Lokacija")
        self.lokacijaLe = QLineEdit(self.centralWidget)
        self.lokacijaLe.setGeometry(QRect(200, 150, 300, 20))
        
        izvajalecLb = QLabel(self.centralWidget)
        izvajalecLb.setGeometry(QRect(40, 185, 150, 20))
        izvajalecLb.setText("Izvajalec del")
        self.izvajalecLe = QLineEdit(self.centralWidget)
        self.izvajalecLe.setGeometry(QRect(200, 185, 300, 20))
        
        pricetekLb = QLabel(self.centralWidget)
        pricetekLb.setGeometry(QRect(40, 220, 150, 20))
        pricetekLb.setText("Predviden pričetek del")
        self.pricetekLe = QLineEdit(self.centralWidget)
        self.pricetekLe.setGeometry(QRect(200, 220, 300, 20))
        
        posebnostiLb = QLabel(self.centralWidget)
        posebnostiLb.setGeometry(QRect(40, 255, 150, 20))
        posebnostiLb.setText("Posebnosti")
        self.posebnostiPle = QPlainTextEdit(self.centralWidget)
        self.posebnostiPle.setGeometry(QRect(200, 255, 300, 140))
       
        # gumb nadaljuj
        self.nadaljujBtn = QPushButton("Nadaljuj", self.centralWidget)
        self.nadaljujBtn.setGeometry(QRect(380, 410, 120, 28))
        MainWindow.setCentralWidget(self.centralWidget)
