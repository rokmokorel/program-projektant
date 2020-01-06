############################# HEADER ######################################
#
# razred za konstrukcijo tabele s podatki o izbranih enotah
#
###########################################################################


from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QTableView, QAbstractItemView
from PyQt5.QtCore import QRect, QSize, Qt, QCoreApplication, QMetaObject
from PyQt5.QtGui import QBrush, QColor

class Ui_Tabela(QWidget):
    
    def __init__(self):
        self.dodane = []

    def setupUi(self, WidgetHolder):
        self.tabela = QTableWidget(WidgetHolder)
        self.tabela.setGeometry(QRect(40, 100, 460, 90))
        self.tabela.setFocusPolicy(Qt.NoFocus)
        self.tabela.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.tabela.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tabela.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabela.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tabela.setShowGrid(False)
        self.tabela.setGridStyle(Qt.SolidLine)
        self.tabela.setRowCount(1)
        self.tabela.setColumnCount(5)
        self.tabela.setObjectName("tableWidget")
        # podatki glava
        self.tabela.horizontalHeader().setVisible(False)
        self.tabela.verticalHeader().setVisible(False)
        self.tabela.horizontalHeader().setDefaultSectionSize(92)
        self.tabela.horizontalHeader().setMinimumSectionSize(20)
        self.tabela.verticalHeader().setDefaultSectionSize(10)

        # 1 vrstica tabele, "header"
        item = QTableWidgetItem("Model")
        brush = QBrush(QColor(227, 227, 227))
        brush.setStyle(Qt.Dense4Pattern)
        item.setBackground(brush)
        self.tabela.setItem(0, 0, item)
        item = QTableWidgetItem("Izvedba")
        brush = QBrush(QColor(227, 227, 227))
        brush.setStyle(Qt.Dense4Pattern)
        item.setBackground(brush)
        self.tabela.setItem(0, 1, item)
        item = QTableWidgetItem("Velikost")
        brush = QBrush(QColor(227, 227, 227))
        brush.setStyle(Qt.Dense4Pattern)
        item.setBackground(brush)
        self.tabela.setItem(0, 2, item)
        item = QTableWidgetItem("Količina")
        brush = QBrush(QColor(227, 227, 227))
        brush.setStyle(Qt.Dense4Pattern)
        item.setBackground(brush)
        self.tabela.setItem(0, 3, item)
        item = QTableWidgetItem("Cena")
        brush = QBrush(QColor(227, 227, 227))
        brush.setStyle(Qt.Dense4Pattern)
        item.setBackground(brush)
        self.tabela.setItem(0, 4, item)
        QMetaObject.connectSlotsByName(WidgetHolder)

    def dodajVrstico(self, model, izvedba, velikost, kolicina, cena):
        if model and izvedba and velikost:
            vr = self.tabela.rowCount()
            self.tabela.insertRow(vr)
            # vnesi tekst
            self.tabela.setItem(vr, 0, QTableWidgetItem(model))
            self.tabela.setItem(vr, 1, QTableWidgetItem(izvedba))
            self.tabela.setItem(vr, 2, QTableWidgetItem(velikost))
            self.tabela.setItem(vr, 3, QTableWidgetItem(f'{kolicina} kos'))
            self.tabela.setItem(vr, 4, QTableWidgetItem(f'{cena},00'))

    def trenutnoVTabeli(self):
        vrstic = self.tabela.rowCount()
        for vr in range(1, vrstic):
            mod = self.tabela.item(vr, 0)
            mod = mod.text()
            iz = self.tabela.item(vr, 1)
            iz = iz.text()
            vel = self.tabela.item(vr, 2)
            vel = vel.text()
            kol = self.tabela.item(vr, 3)
            kol = kol.text()
            cena = self.tabela.item(vr, 4)
            cena = cena.text()
            self.dodane.append((mod, iz, vel, kol, cena))


