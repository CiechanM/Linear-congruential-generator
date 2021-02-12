from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import  *
from PyQt5.QtCore import  *
import tkinter
from tkinter import filedialog
import time
import string
import random
import traceback, sys, os


class Okno(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Okno, self).__init__(*args, *kwargs)
        self.setWindowTitle("Generator LCG")

        #tytul aplikacji gora srodek
        titleText = QLabel()
        titleText.setText("Generator LCG")
        titleText.setAlignment(Qt.AlignCenter)
        titleText.setFont(QFont('Courier New',40 ))
        titleText.setStyleSheet("QLabel {color: #1B2A41} ")


        emptyText = QLabel()
        emptyText.setText(" ")
        emptyText.setAlignment(Qt.AlignCenter)
        emptyText.setFont(QFont('Courier New',15 ))
        emptyText.setStyleSheet("QLabel {color: #1B2A41} ")

        # tekst uwaga na zlodzieje
        welcomeText = QLabel()
        welcomeText.setWordWrap(True)
        welcomeText.setText("Insert your own values, or choose one of the basic generators")
        welcomeText.setAlignment(Qt.AlignCenter)
        welcomeText.setFont(QFont('Courier New', 15))
        welcomeText.setStyleSheet("QLabel {color: #1B2A41} ")

        instructionText = QLabel()
        instructionText.setWordWrap(True)
        instructionText.setText("Insert M, A, B, C, D, X0 and choose power")
        instructionText.setAlignment(Qt.AlignCenter)
        instructionText.setFont(QFont('Courier New', 15))
        instructionText.setStyleSheet("QLabel {color: #1B2A41} ")

        #pole M
        self.mField = QLineEdit()
        self.mField.setPlaceholderText("*Insert M*")
        self.mField.setFont(QFont('Courier New', 11))
        self.mField.setStyleSheet("QLineEdit {color: #000000}")

        #pole A
        self.aField = QLineEdit()
        self.aField.setPlaceholderText("*Insert A*")
        self.aField.setFont(QFont('Courier New', 11))
        self.aField.setStyleSheet("QLineEdit {color: #1B2A41}")

        self.bField = QLineEdit()
        self.bField.setPlaceholderText("*Insert B*")
        self.bField.setFont(QFont('Courier New', 11))
        self.bField.setStyleSheet("QLineEdit {color: #1B2A41}")

        self.cField = QLineEdit()
        self.cField.setPlaceholderText("*Insert C*")
        self.cField.setFont(QFont('Courier New', 11))
        self.cField.setStyleSheet("QLineEdit {color: #1B2A41}")

        self.dField = QLineEdit()
        self.dField.setPlaceholderText("*Insert D*")
        self.dField.setFont(QFont('Courier New', 11))
        self.dField.setStyleSheet("QLineEdit {color: #1B2A41}")

        self.xField = QLineEdit()
        self.xField.setPlaceholderText("*Insert X0*")
        self.xField.setFont(QFont('Courier New', 11))
        self.xField.setStyleSheet("QLineEdit {color: #1B2A41}")

        self.powerField = QComboBox(self)
        self.powerField.setGeometry(200, 150, 150, 30)
        potegaField = ["1", "2", "3"]
        self.powerField.setEditable(True)
        self.powerField.addItems(potegaField)
        editPowerField = self.powerField.lineEdit()
        editPowerField.setAlignment(Qt.AlignRight)

        #pola obok siebie
        textFieldsLayout = QHBoxLayout()
        textFieldsLayout.addWidget(self.mField)
        textFieldsLayout.addWidget(self.aField)
        textFieldsLayout.addWidget(self.bField)
        textFieldsLayout.addWidget(self.cField)
        textFieldsLayout.addWidget(self.dField)
        textFieldsLayout.addWidget(self.xField)
        textFieldsLayout.addWidget(self.powerField)
        textFieldsLayoutWidget = QWidget()
        textFieldsLayoutWidget.setLayout(textFieldsLayout)

        self.saveButton = QPushButton()
        self.saveButton.setText("Generate and save bits to file")
        self.saveButton.setFont(QFont('Courier New', 12))
        self.saveButton.setStyleSheet("QPushButton {background : #1B2A41}")
        self.saveButton.setStyleSheet("QPushButton {color : #1B2A41}")
        self.saveButton.clicked.connect(self.saveClicked)
        self.saveButton.setEnabled(False)

        self.infoButton = QPushButton()
        self.infoButton.setText("Info")
        self.infoButton.setFont(QFont('Courier New', 12))
        self.infoButton.setStyleSheet("QPushButton {background : #1B2A41}")
        self.infoButton.setStyleSheet("QPushButton {color : #1B2A41}")
        self.infoButton.clicked.connect(self.infoClicked)


        infoButtonsLayout = QHBoxLayout()
        infoButtonsLayout.addWidget(self.saveButton)
        infoButtonsLayout.addWidget(self.infoButton)
        infoButtonsLayoutWidget = QWidget()
        infoButtonsLayoutWidget.setLayout(infoButtonsLayout)


        self.saveMessageButton = QPushButton()
        self.saveMessageButton.setText("Generate, save bits and inserted values to files")
        self.saveMessageButton.setFont(QFont('Courier New', 12))
        self.saveMessageButton.setStyleSheet("QPushButton {background : #1B2A41}")
        self.saveMessageButton.setStyleSheet("QPushButton {color : #1B2A41}")
        self.saveMessageButton.clicked.connect(self.generateAndSaveClicked)
        self.saveButton.setEnabled(True)

        saveButtonsLayout = QHBoxLayout()
        saveButtonsLayout.addWidget(self.saveMessageButton)
        saveButtonsLayoutWidget = QWidget()
        saveButtonsLayoutWidget.setLayout(saveButtonsLayout)

        instruction2Text = QLabel()
        instruction2Text.setText("Choose basic generator, power and insert X0 value")
        instruction2Text.setAlignment(Qt.AlignCenter)
        instruction2Text.setFont(QFont('Courier New', 15))
        instruction2Text.setStyleSheet("QLabel {color: #1B2A41} ")

        self.comboBox = QComboBox(self)
       # self.comboBox.setGeometry(200, 150, 150, 30)
        generators = ["ANSI C", "MIN STD", "RANDU", "Fortran", "NAG", "APPLE"]
        self.comboBox.setEditable(True)
        self.comboBox.addItems(generators)
        edit = self.comboBox.lineEdit()
        edit.setAlignment(Qt.AlignRight)

        self.power = QComboBox(self)
        self.power.setGeometry(200, 150, 150, 30)
        potega = ["1", "2", "3"]
        self.power.setEditable(True)
        self.power.addItems(potega)
        editPower = self.power.lineEdit()
        editPower.setAlignment(Qt.AlignRight)


        self.x0Field = QLineEdit()
        self.x0Field.setPlaceholderText("*Insert X0*")
        self.x0Field.setFont(QFont('Courier New', 11))
        self.x0Field.setStyleSheet("QLineEdit {color: #1B2A41}")

        generatorFieldsLayout = QHBoxLayout()
        generatorFieldsLayout.addWidget(self.comboBox)
        generatorFieldsLayout.addWidget(self.power)
        generatorFieldsLayout.addWidget(self.x0Field)
        generatorFieldsLayoutWidget = QWidget()
        generatorFieldsLayoutWidget.setLayout(generatorFieldsLayout)


        #wstawianie przygotowanych pol do programu
        mainMenu = QVBoxLayout()
        mainMenu.setAlignment(Qt.AlignCenter)
        mainMenu.addWidget(titleText)
        mainMenu.addWidget(welcomeText)
        mainMenu.addWidget(emptyText)

        mainMenu.addWidget(instructionText)
        mainMenu.addWidget(textFieldsLayoutWidget)
        mainMenu.addWidget(saveButtonsLayoutWidget)

        mainMenu.addWidget(emptyText)

        mainMenu.addWidget(instruction2Text)
        mainMenu.addWidget(generatorFieldsLayoutWidget)
        mainMenu.addWidget(infoButtonsLayoutWidget)

        mainMenuWidget = QWidget()
        mainMenuWidget.setLayout(mainMenu)

        self.setCentralWidget(mainMenuWidget)

    def saveClicked(self):

        power = str(self.power.currentText())
        argument = str(self.comboBox.currentText())

        x0 = self.x0Field.text()
        if(not self.x0Field.text().isdigit()):
            x0 = 0

        self.switch(argument, power, int(x0))

    def generateAndSaveClicked(self):
        m = self.mField.text()
        a = self.aField.text()
        b = self.bField.text()
        c = self.cField.text()
        d = self.dField.text()
        x = self.xField.text()
        power = str(self.powerField.currentText())

        if(not self.mField.text().isdigit()):
            m = 0
        if(not self.aField.text().isdigit()):
            a = 0
        if(not self.bField.text().isdigit()):
            b = 0
        if(not self.cField.text().isdigit()):
            c = 0
        if(not self.dField.text().isdigit()):
            d = 0
        if(not self.xField.text().isdigit()):
            x = 0

        f = open("userGeneratorConfig.txt", "w")
        f.write(str(m) + '\n')
        f.write(str(a) + '\n')
        f.write(str(b) + '\n')
        f.write(str(c) + '\n')
        f.write(str(d) + '\n')
        f.write(str(x) + '\n')
        f.write(str(power) + '\n')
        f.close()

        gen = Generator(int(m), int(a), int(b), int(c), int(d), int(x))

        if (power == "1"):
            gen.genLCG()
        elif (power == "2"):
            gen.genSquaredLCG()
        elif (power == "3"):
            gen.genCubedLCG()

    def infoClicked(self):
        info = QMessageBox()
        info.setWindowTitle("Info")
        info.setStyleSheet("QMessageBox {background-color : #CCC9DC}")
        f = open("info.txt", "r")
        data = f.read()
        info.setText(data)
        info.setFont(QFont('Courier New', 11))
        info.exec_()

    def switch(self, argument, power, x0):

        if (argument == "ANSI C"):
            gen = Generator(4294967296, 1103515245, 12345, 0, 0, x0)
            if(power == "1"):
                gen.genLCG()
            elif(power == "2"):
                gen.genSquaredLCG()
            elif(power == "3"):
                gen.genCubedLCG()
        elif (argument == "MIN STD"):
            gen = Generator(2147483647, 16807, 0, 0, 0, x0)
            if(power == "1"):
                gen.genLCG()
            elif(power == "2"):
                gen.genSquaredLCG()
            elif(power == "3"):
                gen.genCubedLCG()
        elif (argument == "RANDU"):
            gen = Generator(2147483648, 65539, 0, 0, 0, x0)
            if(power == "1"):
                gen.genLCG()
            elif(power == "2"):
                gen.genSquaredLCG()
            elif(power == "3"):
                gen.genCubedLCG()
        elif (argument == "Fortran"):
            gen = Generator(4294967295, 630360016, 0, 0, 0, x0)
            if(power == "1"):
                gen.genLCG()
            elif(power == "2"):
                gen.genSquaredLCG()
            elif(power == "3"):
                gen.genCubedLCG()
        elif (argument == "NAG"):
            gen = Generator(576460752303423488, 302875106592253, 0, 0, 0, x0)
            if(power == "1"):
                gen.genLCG()
            elif(power == "2"):
                gen.genSquaredLCG()
            elif(power == "3"):
                gen.genCubedLCG()
        elif (argument == "APPLE"):
            gen = Generator(34359738368, 19530937237, 0, 0, 0, x0)
            if(power == "1"):
                gen.genLCG()
            elif(power == "2"):
                gen.genSquaredLCG()
            elif(power == "3"):
                gen.genCubedLCG()


class Generator:
    def __init__(self, m, a, c, d, e, x0):
        self.m = m
        self.a = a
        self.c = c
        self.d = d
        self.e = e
        self.x0 = x0

    def genLCG(self):
        x = self.x0
        ile = 0
        tmp = 0
        tekst = "Wcale sie nie powtarza nic a nic"
        zera = 0
        jedynki = 0

        f = open("binary.txt", "w")
        for i in range(1000000):
            if i == 0:
                #print("Pierwsza rundka")
                x = (self.a * x + self.c) % self.m
                f.write(bin(x)[len(bin(x))-1])
                print(str(i) + ". " + str(x))
                if (str(bin(x)[len(bin(x))-1])) == '1':
                    jedynki += 1
                else:
                    zera += 1
                tmp = x
            else:
                #print("druga rundka")

                x = (self.a * x + self.c) % self.m
                print(str(i) + ". " + str(x))
                #print(bin(x)[len(bin(x))-1])
                f.write(bin(x)[len(bin(x))-1])
                if (str(bin(x)[len(bin(x))-1])) == '1':
                    jedynki += 1
                else:
                    zera += 1
            if i>5 and x == tmp:
                ile += 1
                if ile == 1:
                    tekst = "Powrotrzyla sie po " + str(i) + " petlach"
                print("Liczba sie powtorzyla")
                print(str(x) + ". ." + str(tmp))
        print(tekst + ", czyli " + str(ile) + " razy")
        print("Zera " + str(zera))
        print("Jedynki " + str(jedynki))
        f.close()

    def genSquaredLCG(self):
        x = self.x0
        ile = 0
        tmp = 0
        tekst = "Wcale sie nie powtarza nic a nic"
        zera = 0
        jedynki = 0

        f = open("binarySquared.txt", "w")
        for i in range(1000000):
            if i == 0:
                #print("Pierwsza rundka")
                x = (self.a * x * x + self.c + self.a * x + self.d) % self.m
                f.write(bin(x)[len(bin(x))-1])
                print(str(i) + ". " + str(x))
                tmp = x
                if (str(bin(x)[len(bin(x))-1])) == '1':
                    jedynki += 1
                else:
                    zera += 1
            else:
                x = (self.a * x * x + self.c + self.a * x + self.d) % self.m
                print(str(i) + ". " + str(x))
                #print(bin(x)[len(bin(x))-1])
                f.write(bin(x)[len(bin(x))-1])
                if (str(bin(x)[len(bin(x))-1])) == '1':
                    jedynki += 1
                else:
                    zera += 1
            if i>5 and x == tmp:
                ile += 1
                if ile == 1:
                    tekst = "Powrotrzyla sie po " + str(i) + " petlach"
                print("Liczba sie powtorzyla")
                print(str(x) + ". ." + str(tmp))
                #break
        #print(ile)
        print(tekst + ", czyli " + str(ile) + " razy")
        print("Zera " + str(zera))
        print("Jedynki " + str(jedynki))
        f.close()

    def genCubedLCG(self):
        x = self.x0
        ile = 0
        tmp = 0
        tekst = "Wcale sie nie powtarza nic a nic"
        zera = 0
        jedynki = 0

        f = open("binaryCubed.txt", "w")
        for i in range(1000000):
            if i == 0:
                #print("Pierwsza rundka")
                x = (self.a * x * x * x + self.c + self.a * x * x + self.d + self.a * x + self.e) % self.m
                f.write(bin(x)[len(bin(x))-1])
                print(str(i) + ". " + str(x))
                tmp = x
                if (str(bin(x)[len(bin(x))-1])) == '1':
                    jedynki += 1
                else:
                    zera += 1
            else:
                x = (self.a * x * x * x + self.c + self.a * x * x + self.d + self.a * x + self.e) % self.m
                print(str(i) + ". " + str(x))
                #print(bin(x)[len(bin(x))-1])
                f.write(bin(x)[len(bin(x))-1])
                if (str(bin(x)[len(bin(x))-1])) == '1':
                    jedynki += 1
                else:
                    zera += 1
            if i>5 and x == tmp:
                ile += 1
                if ile == 1:
                    tekst = "Powrotrzyla sie po " + str(i) + " petlach"
                print("Liczba sie powtorzyla")
                print(str(x) + ". ." + str(tmp))
                #break
        #print(ile)
        print(tekst + ", czyli " + str(ile) + " razy")
        print("Zera " + str(zera))
        print("Jedynki " + str(jedynki))
        f.close()

##--------------MAIN--------------------------

app = QApplication(sys.argv)

window = Okno()
window.setFixedSize(800,500)
window.setStyleSheet("background-color:  #CCC9DC ;")
window.show()

app.exec_()