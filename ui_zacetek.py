########################### ui_zacetek.py ####################################
#
# razred zacetnega okna aplikacije
#
# MainWindow - osnovno okolje okoli gradnikov/widgetov
# Widget - gradnik funkcionalnosti
# Layout - prostor, kjer prebivajo gradniki
#############################################################################

from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import QSize


class Ui_Zacetek():

    def setupUi(self, MainWindow):
        # nastavitev fonta, ikone, velikosti okna, naslova
        MainWindow.setWindowTitle("Projektantski popis")
        MainWindow.setFixedSize(QSize(525, 430))
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        app_icon = QIcon('logo/logo2_256.ico')
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
        self.slika.setFixedSize(QSize(105, 28))
        self.slika.setPixmap(QPixmap("logo/logoArtboard-2.png"))
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
        self.prostorNovPopL = QSpacerItem(80, 40, QSizePolicy.Minimum)
        self.prostorNovPopR = QSpacerItem(80, 40, QSizePolicy.Minimum)
        self.novPopisBtn = QPushButton("Nov popis")
        self.novPopisBtn.setFixedSize(QSize(120, 40))
        self.novPopisHLayout.addSpacerItem(self.prostorNovPopL)
        self.novPopisHLayout.addWidget(self.novPopisBtn)
        self.novPopisHLayout.addSpacerItem(self.prostorNovPopR)
        # horizontalni prostor, gumb Popravi popis
        self.popraviPopisHLayout = QHBoxLayout()
        self.skupniVLayout.addLayout(self.popraviPopisHLayout)
        self.prostorPopPopL = QSpacerItem(80, 30, QSizePolicy.Minimum)
        self.prostorPopPopR = QSpacerItem(80, 30, QSizePolicy.Minimum)
        self.popraviPopisBtn = QPushButton("Popravi popis")
        self.popraviPopisBtn.setFixedSize(QSize(120, 30))
        self.popraviPopisHLayout.addSpacerItem(self.prostorPopPopL)
        self.popraviPopisHLayout.addWidget(self.popraviPopisBtn)
        self.popraviPopisHLayout.addSpacerItem(self.prostorPopPopR)
        # prostor spodaj
        self.prostorSpodaj = QSpacerItem(100, 40, QSizePolicy.Maximum)
        self.skupniVLayout.addSpacerItem(self.prostorSpodaj)

        MainWindow.setCentralWidget(self.centralWidget)
