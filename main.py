############################# HEADER ######################################
#
# main program
# vpis podatkov iz SQLite baze v excel(.xlsx) datoteko
#
###########################################################################


from PyQt5 import QtWidgets, QtGui, QtCore
# from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    # set app icon    
    app_icon = QtGui.QIcon('logo\logo_72.ico')
    win.setWindowIcon(app_icon)

    win.setGeometry(400, 300, 300, 300)
    win.setWindowTitle("Aplikacija")

    napis = QtWidgets.QLabel(win)
    napis.setText("Dober dan!!")
    napis.move(50, 50)

    win.show()
    sys.exit(app.exec_())

window()


