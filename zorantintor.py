# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from Crypto.Cipher import DES
import random
import string
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

# Klasa za rad s prozorom dekriptiraj

class MyQwidgetDekriptiraj(QtGui.QWidget):
    def izradi(self):
        uiDekriptiraj.setupUiDekriptiraj(Dekriptiraj)

    def izmjeni(self):
        uiDekriptiraj.lineEdit.setText(FileDialog.getOpenFileName())

    def validiraj(self):
        if  uiDekriptiraj.comboBox.currentIndex()== 0:
            uiDekriptiraj.ispisLabel.setText(QtGui.QApplication.translate("DekriptirajForm", "<html><head/><body><p><span style=\" color:#ff0000;\">Nije potrebna validacija </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        else:
            try:
                readDekriptiranaDatoteka=open('dekriptirani_text.txt','r')
                tekst = readDekriptiranaDatoteka.read()
                readDekriptiranaDatoteka.close()
                hash = SHA.new(tekst).digest()
                uiDekriptiraj.textEdit.setText(hash)
                try:
                    readPotpis=open('potpis.txt','r')
                    potpis = readPotpis.read()
                    readPotpis.close()
                    try:
                        readJavniKljuc = open('javni_kljuc2.txt','r')
                        public_key2 = RSA.importKey(readJavniKljuc.read())
                        readJavniKljuc.close()
                        if public_key2.verify(hash,eval(potpis)) == 1:
                            uiDekriptiraj.ispisLabel.setText(QtGui.QApplication.translate("DekriptirajForm", "<html><head/><body><p><span style=\" color:#006400;\">Validacija uspješna</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
                        else:
                            uiDekriptiraj.ispisLabel.setText(QtGui.QApplication.translate("DekriptirajForm", "<html><head/><body><p><span style=\" color:#ff0000;\">Validacija neuspješna</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
                    except IOError:
                        uiDekriptiraj.ispisLabel.setText(QtGui.QApplication.translate("DekriptirajForm", "<html><head/><body><p><span style=\" color:#ff0000;\">Nedostaje javni ključ 2</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
                except IOError:
                    uiDekriptiraj.ispisLabel.setText(QtGui.QApplication.translate("DekriptirajForm", "<html><head/><body><p><span style=\" color:#ff0000;\">Nedostaje potpis</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
            except IOError:
                uiDekriptiraj.ispisLabel.setText(QtGui.QApplication.translate("DekriptirajForm", "<html><head/><body><p><span style=\" color:#ff0000;\">Datoteka nije dekriptirana</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

    def spremi(self):
        if  uiDekriptiraj.comboBox.currentIndex()== 0:
            try:
                readTajniKljuc = open('tajni_kljuc.txt','r')
                key = readTajniKljuc.read()
                readTajniKljuc.close()
                des = DES.new(key, DES.MODE_ECB)
                try:
                    readDatoteka=open(uiDekriptiraj.lineEdit.text(),'r')
                    tekst = readDatoteka.read()
                    readDatoteka.close()
                    writeDekriptirana=open('dekriptirani_text.txt','w')
                    writeDekriptirana.write(des.decrypt(tekst))
                    writeDekriptirana.close()
                    uiDekriptiraj.ispisLabel.setText(QtGui.QApplication.translate("DekriptirajForm", "<html><head/><body><p><span style=\" color:#006400;\">Datoteka uspješno dekriptirana </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
                except IOError:
                    uiDekriptiraj.ispisLabel.setText(QtGui.QApplication.translate("DekriptirajForm", "<html><head/><body><p><span style=\" color:#ff0000;\">Odaberite datoteku</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
                except SyntaxError:
                    uiDekriptiraj.ispisLabel.setText(QtGui.QApplication.translate("DekriptirajForm", "<html><head/><body><p><span style=\" color:#ff0000;\">Pogrešna datoteka</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))                                        
            except IOError:
                uiDekriptiraj.ispisLabel.setText(QtGui.QApplication.translate("DekriptirajForm", "<html><head/><body><p><span style=\" color:#ff0000;\">Nedostaje tajni ključ</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
            except ValueError:
                uiDekriptiraj.ispisLabel.setText(QtGui.QApplication.translate("DekriptirajForm", "<html><head/><body><p><span style=\" color:#ff0000;\">Krivi ključ</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))  
        else:
            try:
                readDatoteka=open(uiDekriptiraj.lineEdit.text(),'r')
                tekst = readDatoteka.read()
                readDatoteka.close()
                try:
                    readPrivatniKljuc = open('privatni_kljuc.txt','r')
                    key = RSA.importKey(readPrivatniKljuc.read())
                    readPrivatniKljuc.close()
                    writeDekriptiranaDatoteka=open('dekriptirani_text.txt','w')
                    writeDekriptiranaDatoteka.write(key.decrypt(eval(tekst)))
                    writeDekriptiranaDatoteka.close()
                    uiDekriptiraj.ispisLabel.setText(QtGui.QApplication.translate("DekriptirajForm", "<html><head/><body><p><span style=\" color:#006400;\">Datoteka uspješno dekriptirana </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
                except IOError:
                    uiDekriptiraj.ispisLabel.setText(QtGui.QApplication.translate("DekriptirajForm", "<html><head/><body><p><span style=\" color:#ff0000;\">Nedostaje privatni ključ</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
                except SyntaxError:
                    uiDekriptiraj.ispisLabel.setText(QtGui.QApplication.translate("DekriptirajForm", "<html><head/><body><p><span style=\" color:#ff0000;\">Krivi ključ</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))                    
            except IOError:
                uiDekriptiraj.ispisLabel.setText(QtGui.QApplication.translate("DekriptirajForm", "<html><head/><body><p><span style=\" color:#ff0000;\">Odaberite datoteku</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
            except SyntaxError:
                uiDekriptiraj.ispisLabel.setText(QtGui.QApplication.translate("DekriptirajForm", "<html><head/><body><p><span style=\" color:#ff0000;\">Pogrešna datoteka</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))                    

# Klasa za rad s prozorom kriptiraj

class MyQwidgetKriptiraj(QtGui.QWidget):
    def izradi(self):
        uiKriptiraj.setupUiKriptiraj(Kriptiraj)

    def izmjeni(self):
        uiKriptiraj.lineEdit.setText(FileDialog.getOpenFileName())

    def spremi(self):
        if  uiKriptiraj.comboBox.currentIndex()== 0:
            try:
                readTajniKljuc = open('tajni_kljuc.txt','r')
                key = readTajniKljuc.read()
                readTajniKljuc.close()
                des = DES.new(key, DES.MODE_ECB)
                try:
                    readDatoteka=open(uiKriptiraj.lineEdit.text(),'r')
                    tekst = readDatoteka.read()
                    readDatoteka.close()
                    sredeniTekst = tekst + 'X' * (8 - len(tekst)%8)
                    writeKriptiranaDatoteka=open('kriptirani_text.txt','w')
                    writeKriptiranaDatoteka.write(des.encrypt(sredeniTekst))
                    writeKriptiranaDatoteka.close()
                    uiKriptiraj.ispisLabel.setText(QtGui.QApplication.translate("KriptirajForm", "<html><head/><body><p><span style=\" color:#006400;\">Datoteka uspješno kriptirana </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
                except IOError:
                    uiKriptiraj.ispisLabel.setText(QtGui.QApplication.translate("KriptirajForm", "<html><head/><body><p><span style=\" color:#ff0000;\">Odaberite datoteku</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
                except SyntaxError:
                    uiKriptiraj.ispisLabel.setText(QtGui.QApplication.translate("KriptirajForm", "<html><head/><body><p><span style=\" color:#ff0000;\">Pogrešna datoteka</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))                                        
            except IOError:
                uiKriptiraj.ispisLabel.setText(QtGui.QApplication.translate("KriptirajForm", "<html><head/><body><p><span style=\" color:#ff0000;\">Nedostaje tajni ključ</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        else:
            try:
                readDatoteka=open(uiKriptiraj.lineEdit.text(),'r')
                tekst = readDatoteka.read()
                readDatoteka.close()
                hash = SHA.new(tekst).digest()
                uiKriptiraj.textEdit.setText(hash)
                try:
                    readPrivatniKljuc = open('privatni_kljuc2.txt','r')
                    key2 = RSA.importKey(readPrivatniKljuc.read())
                    readPrivatniKljuc.close()
                    potpis = key2.sign(hash,'32')
                    writePotpis=open('potpis.txt','w')
                    writePotpis.write(str(potpis))
                    writePotpis.close()
                    try:
                        readJavniKljuc = open('javni_kljuc.txt','r')
                        public_key = RSA.importKey(readJavniKljuc.read())
                        readJavniKljuc.close()
                        writeKriptiranaDatoteka=open('kriptirani_text.txt','w')
                        writeKriptiranaDatoteka.write(str(public_key.encrypt(tekst,'32')))
                        writeKriptiranaDatoteka.close()
                        uiKriptiraj.ispisLabel.setText(QtGui.QApplication.translate("KriptirajForm", "<html><head/><body><p><span style=\" color:#006400;\">Datoteka potpisana i kriptirana </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
                    except IOError:
                        uiKriptiraj.ispisLabel.setText(QtGui.QApplication.translate("KriptirajForm", "<html><head/><body><p><span style=\" color:#ff0000;\">Nedostaje javni ključ</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
                except IOError:
                    uiKriptiraj.ispisLabel.setText(QtGui.QApplication.translate("KriptirajForm", "<html><head/><body><p><span style=\" color:#ff0000;\">Nedostaje privatni ključ 2</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
            except IOError:
                uiKriptiraj.ispisLabel.setText(QtGui.QApplication.translate("KriptirajForm", "<html><head/><body><p><span style=\" color:#ff0000;\">Odaberite datoteku</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
            except SyntaxError:
                uiKriptiraj.ispisLabel.setText(QtGui.QApplication.translate("KriptirajForm", "<html><head/><body><p><span style=\" color:#ff0000;\">Pogrešna datoteka</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

# Klasa za rad s prozorom generiraj
                    
class MyQwidgetGeneriraj(QtGui.QWidget):
    def izradi(self):
        uiGeneriraj.setupUiGeneriraj(Generiraj)

    def spremi(self):
        if  uiGeneriraj.comboBox.currentIndex()== 0:
            uiGeneriraj.labelIspis.clear()
            uiGeneriraj.labelIspis.setText(QtGui.QApplication.translate("FormGeneriraj", "<html><head/><body><p><span style=\" color:#006400;\">Uspješno generiran </span></p><p><span style=\" color:#ff0000;\">simetrični ključ</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

            sifra = "".join( [random.choice(string.digits+string.letters) for i in xrange(8)] )
            obj = DES.new(sifra, DES.MODE_ECB)

            writeTajniKljuc=open('tajni_kljuc.txt','w')
            writeTajniKljuc.write(sifra)
            writeTajniKljuc.close()            
        else:
            uiGeneriraj.labelIspis.clear()
            uiGeneriraj.labelIspis.setText(QtGui.QApplication.translate("FormGeneriraj", "<html><head/><body><p><span style=\" color:#006400;\">Uspješno generirani </span></p><p><span style=\" color:#ff0000;\">asimetrični ključevi</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

            random_generator = Random.new().read
            key = RSA.generate(1024, random_generator)
            publicKey = key.publickey()

            writePrivatniKljuc=open('privatni_kljuc.txt','w')
            writePrivatniKljuc.write(key.exportKey('PEM'))
            writePrivatniKljuc.close()

            writeJavniKljuc=open('javni_kljuc.txt','w')
            writeJavniKljuc.write(publicKey.exportKey('PEM'))
            writeJavniKljuc.close()

# Klasa za postavljanje FileDialoga

class MyQwidgetFileDialog(QtGui.QFileDialog):
    def prikaziKriptiraj(self):
        uiFileDialog.setupUiFileDialogKriptiraj(FileDialog)

    def prikaziDekriptiraj(self):
        uiFileDialog.setupUiFileDialogDekriptiraj(FileDialog)

# Klasa za definiranje FileDialoga - napravljena pomoću QT Designera osim definiranja akcije kod izlazka iz File Dialoga

class Ui_FileDialog(object):
    def setupUiFileDialogKriptiraj(self, FileDialog):
        if FileDialog.exec_:
            Kriptiraj.izmjeni()

    def setupUiFileDialogDekriptiraj(self, FileDialog):
        if FileDialog.exec_:
            Dekriptiraj.izmjeni()
                        
# Klasa za definiranje elemenata u glavnom prozoru - napravljena pomoću QT Designera osim signala

class Ui_MainForm(object):
    def setupUiMain(self, MainForm):
        MainForm.setObjectName(_fromUtf8("MainForm"))
        MainForm.resize(400, 300)
        MainForm.setFixedSize(MainForm.size())
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/kripto.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainForm.setWindowIcon(icon)
        MainForm.setStyleSheet(_fromUtf8("background-color:rgb(255, 254, 205);"))
        self.encryptButton = QtGui.QPushButton(MainForm)
        self.encryptButton.setGeometry(QtCore.QRect(110, 80, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.encryptButton.setFont(font)
        self.encryptButton.setStyleSheet(_fromUtf8("background-color:rgb(200, 200, 200);\n"
"color:rgb(0, 100, 0);"))
        self.encryptButton.setObjectName(_fromUtf8("encryptButton"))
        self.decryptButton = QtGui.QPushButton(MainForm)
        self.decryptButton.setGeometry(QtCore.QRect(110, 150, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.decryptButton.setFont(font)
        self.decryptButton.setStyleSheet(_fromUtf8("background-color:rgb(200, 200, 200);\n"
"color:rgb(0, 100, 0);"))
        self.decryptButton.setObjectName(_fromUtf8("decryptButton"))
        self.generateButton = QtGui.QPushButton(MainForm)
        self.generateButton.setGeometry(QtCore.QRect(110, 220, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.generateButton.setFont(font)
        self.generateButton.setStyleSheet(_fromUtf8("background-color:rgb(200, 200, 200);\n"
"color:rgb(0, 100, 0);"))
        self.generateButton.setObjectName(_fromUtf8("generateButton"))
        self.mainLabel = QtGui.QLabel(MainForm)
        self.mainLabel.setGeometry(QtCore.QRect(90, 10, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.mainLabel.setFont(font)
        self.mainLabel.setObjectName(_fromUtf8("mainLabel"))

        self.retranslateUi(MainForm)
        QtCore.QObject.connect(self.generateButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainForm.close)
        QtCore.QObject.connect(self.generateButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Generiraj.izradi)          # Tek pritiskom na gumb Ok izraduju se i postavljaju elementi okvira Rezultati.
        QtCore.QObject.connect(self.generateButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Generiraj.show)
        QtCore.QObject.connect(self.encryptButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainForm.close)
        QtCore.QObject.connect(self.encryptButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Kriptiraj.izradi)          # Tek pritiskom na gumb Ok izraduju se i postavljaju elementi okvira Rezultati.
        QtCore.QObject.connect(self.encryptButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Kriptiraj.show)
        QtCore.QObject.connect(self.decryptButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainForm.close)
        QtCore.QObject.connect(self.decryptButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dekriptiraj.izradi)          # Tek pritiskom na gumb Ok izraduju se i postavljaju elementi okvira Rezultati.
        QtCore.QObject.connect(self.decryptButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dekriptiraj.show)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QtGui.QApplication.translate("MainForm", "Aplikacija za kriptiranje i dekriptiranje", None, QtGui.QApplication.UnicodeUTF8))
        self.encryptButton.setText(QtGui.QApplication.translate("MainForm", "Kriptiraj", None, QtGui.QApplication.UnicodeUTF8))
        self.decryptButton.setText(QtGui.QApplication.translate("MainForm", "Dekriptiraj", None, QtGui.QApplication.UnicodeUTF8))
        self.generateButton.setText(QtGui.QApplication.translate("MainForm", "Generiraj ključ", None, QtGui.QApplication.UnicodeUTF8))
        self.mainLabel.setText(QtGui.QApplication.translate("MainForm", "<html><head/><body><p><span style=\" color:#006400;\">Dobro došli u aplikaciju za </span></p><p><span style=\" color:#006400;\">kriptitanje i dekriptiranje !</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

# Klasa za definiranje elemenata u prozoru generiraj - napravljena pomoću QT Designera osim signala

class Ui_FormGeneriraj(object):
    def setupUiGeneriraj(self, FormGeneriraj):
        FormGeneriraj.setObjectName(_fromUtf8("FormGeneriraj"))
        FormGeneriraj.resize(400, 300)
        FormGeneriraj.setFixedSize(FormGeneriraj.size())
        FormGeneriraj.setStyleSheet(_fromUtf8("background-color:rgb(255, 254, 205);"))
        self.comboBox = QtGui.QComboBox(FormGeneriraj)
        self.comboBox.setGeometry(QtCore.QRect(100, 40, 211, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255);\n"
"color:rgb(0, 100, 0);"))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.genButton = QtGui.QPushButton(FormGeneriraj)
        self.genButton.setGeometry(QtCore.QRect(120, 110, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.genButton.setFont(font)
        self.genButton.setStyleSheet(_fromUtf8("background-color:rgb(200, 200, 200);\n"
"color:rgb(0, 100, 0);"))
        self.genButton.setObjectName(_fromUtf8("genButton"))
        self.labelIspis = QtGui.QLabel(FormGeneriraj)
        self.labelIspis.setGeometry(QtCore.QRect(100, 150, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.labelIspis.setFont(font)
        self.labelIspis.setObjectName(_fromUtf8("labelIspis"))
        self.backButton = QtGui.QPushButton(FormGeneriraj)
        self.backButton.setGeometry(QtCore.QRect(150, 260, 98, 27))
        self.backButton.setStyleSheet(_fromUtf8("background-color:rgb(200, 200, 200);\n"
"color:rgb(0, 100, 0);"))
        self.backButton.setObjectName(_fromUtf8("backButton"))

        self.retranslateUi(FormGeneriraj)
        QtCore.QObject.connect(self.genButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Generiraj.spremi)        
        QtCore.QObject.connect(self.backButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Generiraj.close)         
        QtCore.QObject.connect(self.backButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainForm.show)
        QtCore.QMetaObject.connectSlotsByName(FormGeneriraj)

    def retranslateUi(self, FormGeneriraj):
        FormGeneriraj.setWindowTitle(QtGui.QApplication.translate("FormGeneriraj", "Generiraj Ključ", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("FormGeneriraj", "Simetrični", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("FormGeneriraj", "Asimetrični", None, QtGui.QApplication.UnicodeUTF8))
        self.genButton.setText(QtGui.QApplication.translate("FormGeneriraj", "Generiraj", None, QtGui.QApplication.UnicodeUTF8))
        self.labelIspis.setText(QtGui.QApplication.translate("FormGeneriraj", "<html><head/><body><p><span style=\" color:#ff0000;\">""</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("FormGeneriraj", "Početna", None, QtGui.QApplication.UnicodeUTF8))

# Klasa za definiranje elemenata u prozoru kriptiraj - napravljena pomoću QT Designera osim signala

class Ui_KriptirajForm(object):
    def setupUiKriptiraj(self, KriptirajForm):
        KriptirajForm.setObjectName(_fromUtf8("KriptirajForm"))
        KriptirajForm.resize(400, 300)
        KriptirajForm.setStyleSheet(_fromUtf8("background-color:rgb(255, 254, 205);"))
        self.lineEdit = QtGui.QLineEdit(KriptirajForm)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 311, 27))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255);"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.setDisabled(True)
        self.toolButton = QtGui.QToolButton(KriptirajForm)
        self.toolButton.setGeometry(QtCore.QRect(350, 40, 23, 25))
        self.toolButton.setStyleSheet(_fromUtf8("background-color:rgb(200, 200, 200);"))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.labelDatotrka = QtGui.QLabel(KriptirajForm)
        self.labelDatotrka.setGeometry(QtCore.QRect(20, 10, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelDatotrka.setFont(font)
        self.labelDatotrka.setObjectName(_fromUtf8("labelDatotrka"))
        self.comboBox = QtGui.QComboBox(KriptirajForm)
        self.comboBox.setGeometry(QtCore.QRect(20, 110, 191, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255);\n"
"color:rgb(0, 100, 0);"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.labelKljuc = QtGui.QLabel(KriptirajForm)
        self.labelKljuc.setGeometry(QtCore.QRect(20, 80, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelKljuc.setFont(font)
        self.labelKljuc.setObjectName(_fromUtf8("labelKljuc"))
        self.labelSazetak = QtGui.QLabel(KriptirajForm)
        self.labelSazetak.setGeometry(QtCore.QRect(20, 150, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelSazetak.setFont(font)
        self.labelSazetak.setObjectName(_fromUtf8("labelSazetak"))
        self.backButton = QtGui.QPushButton(KriptirajForm)
        self.backButton.setGeometry(QtCore.QRect(260, 270, 98, 27))
        self.backButton.setStyleSheet(_fromUtf8("background-color:rgb(200, 200, 200);\n"
"color:rgb(0, 100, 0);"))
        self.backButton.setObjectName(_fromUtf8("backButton"))
        self.kriptirajButton = QtGui.QPushButton(KriptirajForm)
        self.kriptirajButton.setGeometry(QtCore.QRect(250, 110, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.kriptirajButton.setFont(font)
        self.kriptirajButton.setStyleSheet(_fromUtf8("background-color:rgb(200, 200, 200);\n"
"color:rgb(0, 100, 0);"))
        self.kriptirajButton.setObjectName(_fromUtf8("kriptirajButton"))
        self.textEdit = QtGui.QTextEdit(KriptirajForm)
        self.textEdit.setGeometry(QtCore.QRect(20, 180, 351, 81))
        self.textEdit.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255);"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.ispisLabel = QtGui.QLabel(KriptirajForm)
        self.ispisLabel.setGeometry(QtCore.QRect(10, 270, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ispisLabel.setFont(font)
        self.ispisLabel.setText(_fromUtf8(""))
        self.ispisLabel.setObjectName(_fromUtf8("ispisLabel"))

        self.retranslateUi(KriptirajForm)
        QtCore.QObject.connect(self.toolButton, QtCore.SIGNAL(_fromUtf8("clicked()")), FileDialog.prikaziKriptiraj)
        QtCore.QObject.connect(self.kriptirajButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Kriptiraj.spremi)
        QtCore.QObject.connect(self.backButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Kriptiraj.close)         
        QtCore.QObject.connect(self.backButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainForm.show)
        QtCore.QMetaObject.connectSlotsByName(KriptirajForm)

    def retranslateUi(self, KriptirajForm):
        KriptirajForm.setWindowTitle(QtGui.QApplication.translate("KriptirajForm", "Kriptiraj datoteku", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("KriptirajForm", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDatotrka.setText(QtGui.QApplication.translate("KriptirajForm", "<html><head/><body><p><span style=\" color:#006400;\">Izaberi datoteku:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("KriptirajForm", "tajni_kljuc.txt", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("KriptirajForm", "javni_kljuc.txt", None, QtGui.QApplication.UnicodeUTF8))
        self.labelKljuc.setText(QtGui.QApplication.translate("KriptirajForm", "<html><head/><body><p><span style=\" color:#006400;\">Izaberi ključ:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSazetak.setText(QtGui.QApplication.translate("KriptirajForm", "<html><head/><body><p><span style=\" color:#006400;\">Sažetak:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("KriptirajForm", "Početna", None, QtGui.QApplication.UnicodeUTF8))
        self.kriptirajButton.setText(QtGui.QApplication.translate("KriptirajForm", "Kriptiraj", None, QtGui.QApplication.UnicodeUTF8))

# Klasa za definiranje elemenata u prozoru kriptiraj - napravljena pomoću QT Designera osim signala

class Ui_DekriptirajForm(object):
    def setupUiDekriptiraj(self, DekriptirajForm):
        DekriptirajForm.setObjectName(_fromUtf8("DekriptirajForm"))
        DekriptirajForm.resize(400, 300)
        DekriptirajForm.setStyleSheet(_fromUtf8("background-color:rgb(255, 254, 205);"))
        self.lineEdit = QtGui.QLineEdit(DekriptirajForm)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 311, 27))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255);"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.setDisabled(True)
        self.toolButton = QtGui.QToolButton(DekriptirajForm)
        self.toolButton.setGeometry(QtCore.QRect(350, 40, 23, 25))
        self.toolButton.setStyleSheet(_fromUtf8("background-color:rgb(200, 200, 200);"))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.labelDatotrka = QtGui.QLabel(DekriptirajForm)
        self.labelDatotrka.setGeometry(QtCore.QRect(20, 10, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelDatotrka.setFont(font)
        self.labelDatotrka.setObjectName(_fromUtf8("labelDatotrka"))
        self.comboBox = QtGui.QComboBox(DekriptirajForm)
        self.comboBox.setGeometry(QtCore.QRect(20, 110, 191, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255);\n"
"color:rgb(0, 100, 0);"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.labelKljuc = QtGui.QLabel(DekriptirajForm)
        self.labelKljuc.setGeometry(QtCore.QRect(20, 80, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelKljuc.setFont(font)
        self.labelKljuc.setObjectName(_fromUtf8("labelKljuc"))
        self.labelSazetak = QtGui.QLabel(DekriptirajForm)
        self.labelSazetak.setGeometry(QtCore.QRect(20, 150, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelSazetak.setFont(font)
        self.labelSazetak.setObjectName(_fromUtf8("labelSazetak"))
        self.backButton = QtGui.QPushButton(DekriptirajForm)
        self.backButton.setGeometry(QtCore.QRect(260, 270, 98, 27))
        self.backButton.setStyleSheet(_fromUtf8("background-color:rgb(200, 200, 200);\n"
"color:rgb(0, 100, 0);"))
        self.backButton.setObjectName(_fromUtf8("backButton"))
        self.dekriptirajButton = QtGui.QPushButton(DekriptirajForm)
        self.dekriptirajButton.setGeometry(QtCore.QRect(250, 80, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.dekriptirajButton.setFont(font)
        self.dekriptirajButton.setStyleSheet(_fromUtf8("background-color:rgb(200, 200, 200);\n"
"color:rgb(0, 100, 0);"))
        self.dekriptirajButton.setObjectName(_fromUtf8("dekriptirajButton"))
        self.textEdit = QtGui.QTextEdit(DekriptirajForm)
        self.textEdit.setGeometry(QtCore.QRect(20, 180, 351, 81))
        self.textEdit.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255);"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.ispisLabel = QtGui.QLabel(DekriptirajForm)
        self.ispisLabel.setGeometry(QtCore.QRect(10, 270, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ispisLabel.setFont(font)
        self.ispisLabel.setText(_fromUtf8(""))
        self.ispisLabel.setObjectName(_fromUtf8("ispisLabel"))
        self.validButton = QtGui.QPushButton(DekriptirajForm)
        self.validButton.setGeometry(QtCore.QRect(250, 130, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.validButton.setFont(font)
        self.validButton.setStyleSheet(_fromUtf8("background-color:rgb(200, 200, 200);\n"
"color:rgb(0, 100, 0);"))
        self.validButton.setObjectName(_fromUtf8("validButton"))

        self.retranslateUi(DekriptirajForm)
        QtCore.QObject.connect(self.toolButton, QtCore.SIGNAL(_fromUtf8("clicked()")), FileDialog.prikaziDekriptiraj)
        QtCore.QObject.connect(self.validButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dekriptiraj.validiraj)
        QtCore.QObject.connect(self.dekriptirajButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dekriptiraj.spremi)
        QtCore.QObject.connect(self.backButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dekriptiraj.close)         
        QtCore.QObject.connect(self.backButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainForm.show)
        QtCore.QMetaObject.connectSlotsByName(DekriptirajForm)

    def retranslateUi(self, DekriptirajForm):
        DekriptirajForm.setWindowTitle(QtGui.QApplication.translate("DekriptirajForm", "Dekriptiraj datoteku", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("DekriptirajForm", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDatotrka.setText(QtGui.QApplication.translate("DekriptirajForm", "<html><head/><body><p><span style=\" color:#006400;\">Izaberi datoteku:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("DekriptirajForm", "tajni_kljuc.txt", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("DekriptirajForm", "privatni_kljuc.txt", None, QtGui.QApplication.UnicodeUTF8))
        self.labelKljuc.setText(QtGui.QApplication.translate("DekriptirajForm", "<html><head/><body><p><span style=\" color:#006400;\">Izaberi ključ:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSazetak.setText(QtGui.QApplication.translate("DekriptirajForm", "<html><head/><body><p><span style=\" color:#006400;\">Sažetak:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("DekriptirajForm", "Početna", None, QtGui.QApplication.UnicodeUTF8))
        self.dekriptirajButton.setText(QtGui.QApplication.translate("DekriptirajForm", "Dekriptiraj", None, QtGui.QApplication.UnicodeUTF8))
        self.validButton.setText(QtGui.QApplication.translate("DekriptirajForm", "Validiraj", None, QtGui.QApplication.UnicodeUTF8))

# main

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dekriptiraj = MyQwidgetDekriptiraj()
    uiDekriptiraj = Ui_DekriptirajForm()
    Kriptiraj = MyQwidgetKriptiraj()
    uiKriptiraj = Ui_KriptirajForm()
    FileDialog = MyQwidgetFileDialog()
    uiFileDialog = Ui_FileDialog()
    Generiraj = MyQwidgetGeneriraj()
    uiGeneriraj = Ui_FormGeneriraj()
    MainForm = QtGui.QWidget()
    uiMain = Ui_MainForm()
    uiMain.setupUiMain(MainForm)
    MainForm.show()
    sys.exit(app.exec_())

