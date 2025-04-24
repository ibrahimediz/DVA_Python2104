from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QMessageBox

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi("ui/arayuz.ui",self)
        self.setupUi()
        self.setupConnect()

    def setupConnect(self):
        self.bt1.clicked.connect(self.mesaj)
    def setupUi(self):
        self.setWindowTitle("PyQt5 Ornek")
        self.statusbar.showMessage("Hazır")

    def yazdir(self):
        print(self.txt1.text())
    
    def mesaj(self):
        QMessageBox.information(self,"Bilgi",self.txt1.text())