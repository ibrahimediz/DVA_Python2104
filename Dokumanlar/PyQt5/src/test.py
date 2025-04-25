import time
from PyQt5 import QtWidgets,uic
from datetime import date,datetime
from PyQt5.QtWidgets import QMessageBox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi("ui/test.ui",self)
        self.setupUi()
        self.setupConnect()

    def setupConnect(self):
        self.bt1.clicked.connect(self.bilgileriAl)
        self.bt2.clicked.connect(self.tarayiciAc)

    def setupUi(self):
        self.setWindowTitle("PyQt5 Test Ekranı")
        self.statusbar.showMessage("Hazır")



    def bilgileriAl(self):
        liste = ["adi","yazar","aciklama","fiyat","tarih"]
        sozluk = dict.fromkeys(liste,"")
        sozluk["adi"] = self.txtAd.text()
        sozluk["yazar"] = self.txtYazar.text()
        sozluk["aciklama"] = self.txtAciklama.text()
        sozluk["fiyat"] = self.txtFiyat.text()
        sozluk["tarih"] = ""
        print(sozluk)

    def tarayiciAc(self):
        opt = Options()
        opt.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=opt)
        driver.get("http://www.google.com")
        WebDriverWait(driver,10)