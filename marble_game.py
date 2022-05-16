#File: Marble Game.py

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import random

class MarbleGame(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.bag = int()
        self.firstTurn = bool()
        self.wins = 0
        self.losses = 0
        
        self.setupUi()
        self.retranslateUi()
        self.setupSignals()
        self.show()
    
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.setEnabled(True)
        self.resize(502, 598)


        self.setupGroupBox = QtWidgets.QGroupBox(self)
        self.setupGroupBox.setEnabled(True)
        self.setupGroupBox.setGeometry(QtCore.QRect(20, 60, 151, 311))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.setupGroupBox.setFont(font)
        self.setupGroupBox.setStyleSheet("")
        self.setupGroupBox.setTitle("")
        self.setupGroupBox.setObjectName("setupGroupBox")


        self.sPushButton2 = QtWidgets.QPushButton(self.setupGroupBox)
        self.sPushButton2.setGeometry(QtCore.QRect(10, 180, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.sPushButton2.setFont(font)
        self.sPushButton2.setObjectName("sPushButton2")


        self.sLabel3 = QtWidgets.QLabel(self.setupGroupBox)
        self.sLabel3.setGeometry(QtCore.QRect(40, 110, 70, 19))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.sLabel3.setFont(font)
        self.sLabel3.setObjectName("sLabel3")


        self.sLabel1 = QtWidgets.QLabel(self.setupGroupBox)
        self.sLabel1.setGeometry(QtCore.QRect(10, 10, 128, 19))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.sLabel1.setFont(font)
        self.sLabel1.setObjectName("sLabel1")


        self.sLabel5 = QtWidgets.QLabel(self.setupGroupBox)
        self.sLabel5.setGeometry(QtCore.QRect(10, 230, 47, 13))
        self.sLabel5.setObjectName("sLabel5")

        
        self.sLabel6 = QtWidgets.QLabel(self.setupGroupBox)
        self.sLabel6.setGeometry(QtCore.QRect(10, 250, 81, 13))
        self.sLabel6.setObjectName("sLabel6")


        self.sPushButton3 = QtWidgets.QPushButton(self.setupGroupBox)
        self.sPushButton3.setGeometry(QtCore.QRect(10, 270, 131, 23))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.sPushButton3.setFont(font)
        self.sPushButton3.setObjectName("sPushButton3")


        self.sLabel4 = QtWidgets.QLabel(self.setupGroupBox)
        self.sLabel4.setGeometry(QtCore.QRect(40, 210, 60, 19))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.sLabel4.setFont(font)
        self.sLabel4.setObjectName("sLabel4")


        self.frame = QtWidgets.QFrame(self.setupGroupBox)
        self.frame.setGeometry(QtCore.QRect(0, 30, 151, 71))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")


        self.sRadioButton1 = QtWidgets.QRadioButton(self.frame)
        self.sRadioButton1.setGeometry(QtCore.QRect(10, 10, 16, 17))
        self.sRadioButton1.setText("")
        self.sRadioButton1.setObjectName("sRadioButton1")

        
        self.sComboBox = QtWidgets.QComboBox(self.frame)
        self.sComboBox.setEnabled(True)
        self.sComboBox.setGeometry(QtCore.QRect(30, 40, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.sComboBox.setFont(font)
        self.sComboBox.setObjectName("sComboBox")
        self.sComboBox.addItem("")
        self.sComboBox.addItem("")
        self.sComboBox.addItem("")
        self.sComboBox.addItem("")
        self.sComboBox.addItem("")
        self.sComboBox.addItem("")
        self.sComboBox.addItem("")
        self.sComboBox.addItem("")
        self.sComboBox.addItem("")
        self.sComboBox.addItem("")
        self.sComboBox.addItem("")
        self.sComboBox.addItem("")


        self.sPushButton1 = QtWidgets.QPushButton(self.frame)
        self.sPushButton1.setEnabled(True)
        self.sPushButton1.setGeometry(QtCore.QRect(30, 10, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.sPushButton1.setFont(font)
        self.sPushButton1.setObjectName("sPushButton1")


        self.sLabel2 = QtWidgets.QLabel(self.frame)
        self.sLabel2.setGeometry(QtCore.QRect(120, 10, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.sLabel2.setFont(font)
        self.sLabel2.setFrameShape(QtWidgets.QFrame.Box)
        self.sLabel2.setObjectName("sLabel2")


        self.sRadioButton2 = QtWidgets.QRadioButton(self.frame)
        self.sRadioButton2.setGeometry(QtCore.QRect(10, 40, 16, 17))
        self.sRadioButton2.setText("")
        self.sRadioButton2.setObjectName("sRadioButton2")


        self.frame_2 = QtWidgets.QFrame(self.setupGroupBox)
        self.frame_2.setGeometry(QtCore.QRect(0, 130, 151, 41))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")


        self.sRadioButton4 = QtWidgets.QRadioButton(self.frame_2)
        self.sRadioButton4.setGeometry(QtCore.QRect(10, 20, 118, 22))
        self.sRadioButton4.setObjectName("sRadioButton4")


        self.sRadioButton3 = QtWidgets.QRadioButton(self.frame_2)
        self.sRadioButton3.setGeometry(QtCore.QRect(10, 0, 93, 21))
        self.sRadioButton3.setObjectName("sRadioButton3")


        self.rulesGroupBox = QtWidgets.QGroupBox(self)
        self.rulesGroupBox.setEnabled(True)
        self.rulesGroupBox.setGeometry(QtCore.QRect(20, 380, 151, 191))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.rulesGroupBox.setFont(font)
        self.rulesGroupBox.setObjectName("rulesGroupBox")


        self.rPushButton = QtWidgets.QPushButton(self.rulesGroupBox)
        self.rPushButton.setGeometry(QtCore.QRect(10, 160, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(8)
        self.rPushButton.setFont(font)
        self.rPushButton.setObjectName("rPushButton")


        self.rPlainTextEdit = QtWidgets.QPlainTextEdit(self.rulesGroupBox)
        self.rPlainTextEdit.setGeometry(QtCore.QRect(10, 20, 131, 131))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.rPlainTextEdit.setFont(font)
        self.rPlainTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.rPlainTextEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.rPlainTextEdit.setReadOnly(True)
        self.rPlainTextEdit.setObjectName("rPlainTextEdit")


        self.Title = QtWidgets.QLabel(self)
        self.Title.setGeometry(QtCore.QRect(170, 20, 170, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(20)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")


        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(190, 60, 291, 511))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")


        self.gLabel1 = QtWidgets.QLabel(self.groupBox)
        self.gLabel1.setGeometry(QtCore.QRect(20, 10, 90, 19))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.gLabel1.setFont(font)
        self.gLabel1.setObjectName("gLabel1")


        self.gPlainTextEdit1 = QtWidgets.QPlainTextEdit(self.groupBox)
        self.gPlainTextEdit1.setGeometry(QtCore.QRect(20, 130, 111, 341))
        self.gPlainTextEdit1.setReadOnly(True)
        self.gPlainTextEdit1.setObjectName("gPlainTextEdit1")


        self.gPushButton1 = QtWidgets.QPushButton(self.groupBox)
        self.gPushButton1.setGeometry(QtCore.QRect(20, 70, 75, 23))
        self.gPushButton1.setObjectName("gPushButton1")


        self.gLabel4 = QtWidgets.QLabel(self.groupBox)
        self.gLabel4.setGeometry(QtCore.QRect(20, 110, 57, 19))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.gLabel4.setFont(font)
        self.gLabel4.setObjectName("gLabel4")


        self.gPlainTextEdit2 = QtWidgets.QPlainTextEdit(self.groupBox)
        self.gPlainTextEdit2.setGeometry(QtCore.QRect(150, 130, 121, 101))
        self.gPlainTextEdit2.setReadOnly(True)
        self.gPlainTextEdit2.setObjectName("gPlainTextEdit2")


        self.gPushButton4 = QtWidgets.QPushButton(self.groupBox)
        self.gPushButton4.setGeometry(QtCore.QRect(150, 240, 121, 31))
        self.gPushButton4.setObjectName("gPushButton4")


        self.gPushButton3 = QtWidgets.QPushButton(self.groupBox)
        self.gPushButton3.setGeometry(QtCore.QRect(200, 70, 75, 23))
        self.gPushButton3.setObjectName("gPushButton3")


        self.gLabel3 = QtWidgets.QLabel(self.groupBox)
        self.gLabel3.setGeometry(QtCore.QRect(20, 40, 167, 19))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.gLabel3.setFont(font)
        self.gLabel3.setObjectName("gLabel3")


        self.gPushButton5 = QtWidgets.QPushButton(self.groupBox)
        self.gPushButton5.setGeometry(QtCore.QRect(150, 280, 121, 31))
        self.gPushButton5.setObjectName("gPushButton5")


        self.gLabel2 = QtWidgets.QLabel(self.groupBox)
        self.gLabel2.setGeometry(QtCore.QRect(140, 10, 61, 19))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.gLabel2.setFont(font)
        self.gLabel2.setObjectName("gLabel2")


        self.gLabel5 = QtWidgets.QLabel(self.groupBox)
        self.gLabel5.setGeometry(QtCore.QRect(150, 110, 80, 19))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.gLabel5.setFont(font)
        self.gLabel5.setObjectName("gLabel5")


        self.picture = QtWidgets.QLabel(self.groupBox)
        self.picture.setGeometry(QtCore.QRect(150, 320, 121, 151))
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap("images/marble-jar.jpg"))
        self.picture.setScaledContents(True)
        self.picture.setObjectName("picture")


        self.gPushButton2 = QtWidgets.QPushButton(self.groupBox)
        self.gPushButton2.setGeometry(QtCore.QRect(110, 70, 75, 23))
        self.gPushButton2.setObjectName("gPushButton2")


        for i in self.groupBox.children():
                i.setEnabled(False)


        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Marble Game"))
        self.sPushButton2.setText(_translate("MainWindow", "Confirm"))
        self.sLabel3.setText(_translate("MainWindow", "First Turn"))
        self.sLabel1.setText(_translate("MainWindow", "Bag Start Amount"))
        self.sLabel5.setText(_translate("MainWindow", "Wins: " + str(self.wins)))
        self.sLabel6.setText(_translate("MainWindow", "Losses: " + str(self.losses)))
        self.sPushButton3.setText(_translate("MainWindow", "Reset Counter"))
        self.sLabel4.setText(_translate("MainWindow", "Counter"))
        self.sComboBox.setItemText(0, _translate("MainWindow", "Choose"))
        self.sComboBox.setItemText(1, _translate("MainWindow", "20"))
        self.sComboBox.setItemText(2, _translate("MainWindow", "21"))
        self.sComboBox.setItemText(3, _translate("MainWindow", "22"))
        self.sComboBox.setItemText(4, _translate("MainWindow", "23"))
        self.sComboBox.setItemText(5, _translate("MainWindow", "24"))
        self.sComboBox.setItemText(6, _translate("MainWindow", "25"))
        self.sComboBox.setItemText(7, _translate("MainWindow", "26"))
        self.sComboBox.setItemText(8, _translate("MainWindow", "27"))
        self.sComboBox.setItemText(9, _translate("MainWindow", "28"))
        self.sComboBox.setItemText(10, _translate("MainWindow", "29"))
        self.sComboBox.setItemText(11, _translate("MainWindow", "30"))
        self.sPushButton1.setText(_translate("MainWindow", "Randomize"))
        self.sLabel2.setText(_translate("MainWindow", "..."))
        self.sRadioButton4.setText(_translate("MainWindow", "Computer Starts"))
        self.sRadioButton3.setText(_translate("MainWindow", "Player Starts"))
        self.rulesGroupBox.setTitle(_translate("MainWindow", "Rules"))
        self.rPushButton.setText(_translate("MainWindow", "Details"))
        self.rPlainTextEdit.setPlainText(_translate("MainWindow", "Take turns taking marbles out of a bag in intervals of 1, 3, or 4 at a time in order to get the last marble"))
        self.Title.setText(_translate("MainWindow", "Marble Game"))
        self.gLabel1.setText(_translate("MainWindow", "Turn: Player"))
        self.gPushButton1.setText(_translate("MainWindow", "1"))
        self.gLabel4.setText(_translate("MainWindow", "History:"))
        self.gPushButton4.setText(_translate("MainWindow", "Start"))
        self.gPushButton3.setText(_translate("MainWindow", "4"))
        self.gLabel3.setText(_translate("MainWindow", "Select Marble Amount:"))
        self.gPushButton5.setText(_translate("MainWindow", "Settings"))
        self.gLabel2.setText(_translate("MainWindow", "Bag: 0"))
        self.gLabel5.setText(_translate("MainWindow", "Computer:"))
        self.gPushButton2.setText(_translate("MainWindow", "3"))

    def setupSignals(self):

        self.sRadioButton1.clicked.connect(self.sRadioButton1_onPressed)
        self.sRadioButton2.clicked.connect(self.sRadioButton2_onPressed)
        
        self.sPushButton1.clicked.connect(self.sPushButton1_onPressed)
        self.sPushButton2.clicked.connect(self.sPushButton2_onPressed)
        self.sPushButton3.clicked.connect(self.sPushButton3_onPressed)

        self.sComboBox.currentTextChanged.connect(self.sComboBox_onPressed)

        self.rPushButton.clicked.connect(self.rPushButton_onPressed)

        self.gPushButton1.clicked.connect(lambda: self.playerTurn(1))
        self.gPushButton2.clicked.connect(lambda: self.playerTurn(3))
        self.gPushButton3.clicked.connect(lambda: self.playerTurn(4))
        self.gPushButton4.clicked.connect(self.gPushButton4_onPressed)
        self.gPushButton5.clicked.connect(self.gPushButton5_onPressed)



    def sRadioButton1_onPressed(self):
        # Randomize radio button
        self.sPushButton1.setEnabled(True)
        self.sLabel2.setEnabled(True)
        self.sComboBox.setEnabled(False)
        self.sPushButton1_onPressed()
    
    def sRadioButton2_onPressed(self):
        # Choose radio button
        self.sPushButton1.setEnabled(False)
        self.sLabel2.setEnabled(False)
        self.sComboBox.setEnabled(True)
    
    def sComboBox_onPressed(self):
        # Choose combo box
        self.sRadioButton2.setChecked(True)
    
    def sPushButton1_onPressed(self):
        # Randomize push button
        choices = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        self.sLabel2.setText(str(random.choice(choices)))
        self.sRadioButton1.setChecked(True)

    def sPushButton2_onPressed(self):
        # Confirm push button
        if self.sRadioButton2.isChecked() and self.sComboBox.currentText() == "Choose":
            return
        elif (self.sRadioButton1.isChecked() or self.sRadioButton2.isChecked()) and (self.sRadioButton3.isChecked() or self.sRadioButton4.isChecked()):
            self.setSettings()

            self.setupGroupBox.setEnabled(False)
            self.awaitGameStart()
            self.gPushButton4.setEnabled(True)
            self.setComputerText("start game")
        else:
            return
        self.updateBag()
        
    
    
    def sPushButton3_onPressed(self):
        # Reset Counter push button
        self.wins = 0
        self.losses = 0
        self.sLabel5.setText("Wins: " + str(self.wins))
        self.sLabel6.setText("Losses: " + str(self.losses))

    def gPushButton4_onPressed(self):
        # Start push button
        
        if self.gPushButton4.text() == "Start":
            self.gPushButton4.setText("Restart")
            for i in self.groupBox.children():
                i.setEnabled(True)
        elif self.gPushButton4.text() == "Restart":
            self.gPlainTextEdit1.clear()
            self.setSettings()
        self.updateBag()
        
        self.setComputerText("player first")
        if not self.firstTurn:
            self.computerTurn()
            self.setComputerText("computer first")
            return
        
        
        
    def gPushButton5_onPressed(self):
        # Details push button
        self.gPushButton4.setText("Start")
        self.gPlainTextEdit1.clear()
        self.setComputerText("settings")

        self.setupGroupBox.setEnabled(True)
        self.setSettings()

        for i in self.groupBox.children():
            i.setEnabled(False)
        self.awaitGameStart()
        
    def rPushButton_onPressed(self):
        self.rulesWindow = RulesWindow()



    def playerTurn(self, input):
        if self.firstTurn == None:
            return
        if input > self.bag:
            self.setComputerText("cheater")
            return
        
        self.bag -= input
        self.appendHistory("P: -" + str(input) + " | B: " + str(self.bag))
        
        if self.bag <= 0:
            self.playerWins(True)
            return
        self.computerTurn()
        
    def computerTurn(self):
        if not self.firstTurn:
            self.firstTurn = True
        if self.bag == 2:
            # Single specific case
            choice = 1
        elif self.bag % 7 == 0 or self.bag % 7 == 2:
            
            choices = [1, 3, 4]
            choice = random.choice(choices)
        else:
            tempBag = self.bag
            while (tempBag % 7 != 0) and (tempBag % 7 != 2 or (self.bag - tempBag == 2)):
                tempBag -= 1
            choice = self.bag - tempBag
        
            

        self.bag -= choice
        self.updateBag()
        self.appendHistory("C: -" + str(choice) + " | B: " + str(self.bag))
        self.setComputerText("computer thinking")


        if self.bag <= 0:
            self.playerWins(False)

    def updateBag(self):
        self.gLabel2.setText("Bag: " + str(self.bag))

    def setComputerText(self, group):
        if group == "start game":
            choices = ["Come on and press the start button!", "Let's start already!", "Start the game!"]
        elif group == "player first":
            choices = ["I'll let you go first", "Looks like you take the first turn!", "Go ahead and make your choice", "Think really carefully"]
        elif group == "computer first":
            choices = ["Looks like I'll take the first turn!", "Winners first!", "The first move is most important!"]
        elif group == "computer thinking":
            choices = ["Easy decision to be made", "Hmm....", "I'll do this I guess"]
        elif group == "computer win":
            choices = ["Hahaha I win!", "Looks like I win!", "Don't feel too bad"]
        elif group == "player win":
            choices = ["You... beat me? Lucky I guess...", "No way you beat me, rematch?", "You won?? Let's go again."]
        elif group == "settings":
            choices = ["Got a different strategy?", "Maybe a different approach would be better?", "Do whatever you want, I know I'll win!"]
        elif group == "cheater":
            choices = ["Theres not enough marbles in the bag cheater!", "Hey! Look at the amount of marbles that are in there!", "What are you doing? There's only " + str(self.bag) + " marbles!"]
        else:
            choices = "X"
        self.gPlainTextEdit2.setPlainText(random.choice(choices))
    
    def appendHistory(self, dialog):
        self.gPlainTextEdit1.appendPlainText(dialog)

    def playerWins(self, playerWon):
        self.firstTurn = None
        if playerWon:
            self.appendHistory("Player has won!")
            self.setComputerText("player win")
            self.wins += 1
        else:
            self.appendHistory("Computer has won!")
            self.setComputerText("computer win")
            self.losses += 1
        self.sLabel5.setText("Wins: " + str(self.wins))
        self.sLabel6.setText("Losses: " + str(self.losses))
        
    def setSettings(self):
        if self.sRadioButton1.isChecked():
            self.bag = int(self.sLabel2.text())
        else:
            self.bag = int(self.sComboBox.currentText())
        if self.sRadioButton3.isChecked():
            self.firstTurn = True
        else:
            self.firstTurn = False
        
    def awaitGameStart(self):
        self.gLabel5.setEnabled(True)
        self.gPlainTextEdit2.setEnabled(True)



class RulesWindow(QDialog):
    def __init__(self, parent = None):
        super(RulesWindow, self).__init__(parent)
        self.setupUi()
        self.show()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(331, 275)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 301, 251))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Rules"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "Take turns with a computer taking marbles out of a bag in amounts of 1, 3, or 4. The goal of the game is to take out the last marble. \n"
"\n"
"This game is designed so that the computer will always win against a player with no strategy, and will always lose against  a player with a strategy\n"
"\n"
"First select a starting amount of marbles in the bag, with the option of a randomized amount of marbles between 20-30 or player\'s choice between 20-30. Then choose whether the computer takes the first turn. Clicking confirm will start the game with the set settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = MarbleGame()
    
    sys.exit(app.exec_())