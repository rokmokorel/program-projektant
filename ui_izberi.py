########################### ui_izberi.py ####################################
#
# razred okna za izbor enot, dodajanje enot v excel popis
#
# MainWindow - osnovno okolje okoli gradnikov/widgetov
# Widget - gradnik funkcionalnosti
# Layout - prostor, kjer prebivajo gradniki
#
#############################################################################

from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QFrame, QComboBox, QFileDialog, QTableWidget, QTableWidgetItem, QTableView
# from PyQt5.QtGui import QTableView
from PyQt5.QtCore import QRect, QSize

import tabela as tab
import sqlite.func_baza as fba


class Ui_Izberi(QWidget):
    def setupUi(self, MainWindow):
        # postavi glavni gradnik
        self.centralWidget = QWidget(MainWindow)
        # lokacija excel
        self.lokacijaExcelBtn = QPushButton("Lokacija excel", self.centralWidget)
        self.lokacijaExcelBtn.setGeometry(QRect(40, 19, 100, 24))
        self.lokacijaExcelLe = QLineEdit(self.centralWidget)
        self.lokacijaExcelLe.setGeometry(QRect(160, 20, 340, 22))
        # zakljuci zapis
        self.zakljuciZapisBtn = QPushButton(self.centralWidget)
        self.zakljuciZapisBtn.setGeometry(QRect(380, 50, 120, 28))
        self.zakljuciZapisBtn.setText("Zaključi zapis")
        # tabela dodane postavke
        dodanePostavkeLb = QLabel(self.centralWidget)
        dodanePostavkeLb.setGeometry(QRect(40, 80, 100, 20))
        dodanePostavkeLb.setText("Dodane postavke")
        self.dodanePostavkeTb = tab.Ui_Tabela(self.centralWidget)
        self.dodanePostavkeTb.setupUi(self.centralWidget)

        # skupaj
        skupajLb = QLabel(self.centralWidget)
        skupajLb.setGeometry(QRect(310, 200, 40, 20))
        skupajLe = QLineEdit(self.centralWidget)
        skupajLe.setGeometry(QRect(380, 200, 120, 22))
        skupajLb.setText("Skupaj")
        # horizontala
        delitev = QFrame(self.centralWidget)
        delitev.setGeometry(QRect(7, 230, 513, 20))
        delitev.setFrameShape(QFrame.HLine)
        delitev.setFrameShadow(QFrame.Sunken)
        # dodaj postavke
        dodajPostavkoLb = QLabel(self.centralWidget)
        dodajPostavkoLb.setGeometry(QRect(40, 260, 160, 20))
        dodajPostavkoLb.setText("Dodajanje postavke")
        # izberi segment, model, velikost
        izberiSegmentLb = QLabel(self.centralWidget)
        izberiSegmentLb.setGeometry(QRect(40, 290, 90, 20))
        izberiSegmentLb.setText("Izberi segment")
        self.izberiSegmentCb = QComboBox(self.centralWidget)
        self.izberiSegmentCb.setGeometry(QRect(240, 290, 260, 20))
        self.izberiSegmentCb.addItems(['chiller', 'heat pump'])
        self.izberiSegmentCb.currentTextChanged.connect(self.posodobi_model)

        izberiModelLb = QLabel(self.centralWidget)
        izberiModelLb.setGeometry(QRect(40, 320, 90, 20))
        izberiModelLb.setText("Izberi model")
        self.izberiModelCb = QComboBox(self.centralWidget)
        self.izberiModelCb.setGeometry(QRect(240, 320, 260, 20))
        self.izberiModelCb.currentTextChanged.connect(self.posodobi_izvedbe)

        izberiIzvedboLb = QLabel(self.centralWidget)
        izberiIzvedboLb.setGeometry(QRect(40, 350, 90, 20))
        izberiIzvedboLb.setText("Izberi izvedbo")
        self.izberiIzvedboCb = QComboBox(self.centralWidget)
        self.izberiIzvedboCb.setGeometry(QRect(240, 350, 260, 20))
        self.izberiIzvedboCb.currentTextChanged.connect(self.posodobi_velikosti)

        izberiVelikostLb = QLabel(self.centralWidget)
        izberiVelikostLb.setGeometry(QRect(40, 380, 90, 20))
        izberiVelikostLb.setText("Izberi velikost")
        self.izberiVelikostCb = QComboBox(self.centralWidget)
        self.izberiVelikostCb.setGeometry(QRect(240, 380, 260, 20))
        # gumb dodaj
        dodajPostavkoBtn = QPushButton("Dodaj postavko", self.centralWidget)
        dodajPostavkoBtn.setGeometry(QRect(380, 410, 120, 28))
        dodajPostavkoBtn.clicked.connect(self.dodaj_postavko)
        # glavni gradnik postavimo v okno
        MainWindow.setCentralWidget(self.centralWidget)

    def fileDialog(self):
        fname = QFileDialog.getExistingDirectory(self, "Izberi mapo")
        self.lokacijaExcelLe.setText(fname)

    def posodobi_model(self):
        self.segment = self.izberiSegmentCb.currentText()
        self.izberiModelCb.clear()
        self.izberiIzvedboCb.clear()
        self.izberiVelikostCb.clear()
        if self.segment == 'chiller':
            self.baza = fba.Baza()
            self.baza.povezi_bazo()
            self.izberiModelCb.addItems(self.baza.poisci_modele())
            self.posodobi_izvedbe()
        else:
            pass

    def posodobi_izvedbe(self):
        self.izberiIzvedboCb.clear()
        try:
            _ = self.baza.poisci_izvedbe(self.izberiModelCb.currentText())
            self.izberiIzvedboCb.addItems(_)
        except:
            pass

    def posodobi_velikosti(self):
        try:
            _ = self.baza.poisci_velikost(
                self.izberiModelCb.currentText(),
                self.izberiIzvedboCb.currentText())
            self.izberiVelikostCb.clear()
            self.izberiVelikostCb.addItems(_)
        except:
            pass

    def dodaj_postavko(self):
        model = self.izberiModelCb.currentText()
        izvedba = self.izberiIzvedboCb.currentText()
        velikost = self.izberiVelikostCb.currentText()
        print(model, izvedba, velikost)
        self.dodanePostavkeTb.dodajStolpec(model, izvedba, velikost)
