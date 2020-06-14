########################### ui_zacetek.py ####################################
#
# razred zacetnega okna aplikacije
#
# MainWindow - osnovno okolje okoli gradnikov/widgetov
# Widget - gradnik funkcionalnosti
# Layout - prostor, kjer prebivajo gradniki
#
#############################################################################

from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy, QFileDialog
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import QSize


class Ui_Zacetek(QWidget):
    def setupUi(self, MainWindow):
        # nastavitev fonta, ikone, velikosti okna, naslova
        MainWindow.setWindowTitle("Projektantski popis")
        MainWindow.setFixedSize(QSize(525, 460))
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        app_icon = QIcon('logo\logo_256.ico')
        MainWindow.setWindowIcon(app_icon)

        # glavni gradnik in skupni vertikalni prostor
        self.centralWidget = QWidget(MainWindow)
        self.skupniVLayout = QVBoxLayout(self.centralWidget)
        self.p1 = QSpacerItem(40, 120)
        self.skupniVLayout.addSpacerItem(self.p1)
        # horizontalni prostor za sliko
        # H prostor, prostor L/D
        self.logoHLayout = QHBoxLayout()
        self.skupniVLayout.addLayout(self.logoHLayout)
        self.prostorR = QSpacerItem(80, 20, QSizePolicy.Minimum)
        self.prostorL = QSpacerItem(80, 20, QSizePolicy.Minimum)
        # slika
        self.slika = QLabel()
        self.slika.setFixedSize(QSize(120, 120))
        self.slika.setPixmap(QPixmap("logo\logo2.png"))
        self.slika.setScaledContents(True)
        # skupaj v prostor
        self.logoHLayout.addItem(self.prostorL)
        self.logoHLayout.addWidget(self.slika)
        self.logoHLayout.addItem(self.prostorR)
        self.p2 = QSpacerItem(40,60)
        self.skupniVLayout.addSpacerItem(self.p2)
        # horizontalni prostor, gumb Nov popis
        self.novPopisHLayout = QHBoxLayout()
        self.skupniVLayout.addLayout(self.novPopisHLayout)
        self.prostorNovPopL = QSpacerItem(80, 30, QSizePolicy.Minimum)
        self.prostorNovPopR = QSpacerItem(80, 30, QSizePolicy.Minimum)
        self.novPopisBtn = QPushButton("Nov popis")
        self.novPopisBtn.setFixedSize(QSize(120, 40))
        self.novPopisHLayout.addSpacerItem(self.prostorNovPopL)
        self.novPopisHLayout.addWidget(self.novPopisBtn)
        self.novPopisHLayout.addSpacerItem(self.prostorNovPopR)
        # horizontalni prostor, gumb Posodobi bazo
        self.popraviPopisHLayout = QHBoxLayout()
        self.skupniVLayout.addLayout(self.popraviPopisHLayout)
        self.prostorPopPopL = QSpacerItem(80, 30, QSizePolicy.Minimum)
        self.prostorPopPopR = QSpacerItem(80, 30, QSizePolicy.Minimum)
        self.popraviPopisBtn = QPushButton("Posodobi bazo")
        self.popraviPopisBtn.setFixedSize(QSize(120, 30))
        self.popraviPopisHLayout.addSpacerItem(self.prostorPopPopL)
        self.popraviPopisHLayout.addWidget(self.popraviPopisBtn)
        self.popraviPopisHLayout.addSpacerItem(self.prostorPopPopR)
        # prostor spodaj
        self.prostorSpodaj = QSpacerItem(100, 40, QSizePolicy.Maximum)
        self.skupniVLayout.addSpacerItem(self.prostorSpodaj)

        MainWindow.setCentralWidget(self.centralWidget)
