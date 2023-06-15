import sys
from PyQt5.QtWidgets import  QApplication
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QTextEdit, QSizePolicy, QDialog
from PyQt5.QtCore import Qt, QUrl
from tkinter import messagebox
from PyQt5.QtCore import pyqtSignal, QObject
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import UpdateDatabase
import SearchFile
image = r"M:\QA 11122019\24_JeremyProgrammingFolder\CTAlogo.png"
con = sqlite3.connect(UpdateDatabase.path)
cur = con.cursor()

class Ui_Main(object):
    def __init__(self, car_num):
        self.car_num = car_num
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1618, 900)
        # Main.setMaximumSize(QtCore.QSize(16777215, 900))
        Main.setMaximumSize(QtCore.QSize(16777215, 9000))

        Main.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setStyleSheet("background-color:#0091DA;\n")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ScrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.ScrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.ScrollArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ScrollArea.setAutoFillBackground(True)
        self.ScrollArea.setStyleSheet("background-color:#0091DA")
        self.ScrollArea.setWidgetResizable(True)
        self.ScrollArea.setObjectName("ScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(-1390, 0, 2988, 842))
        self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.MainPannel = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.MainPannel.setMinimumSize(QtCore.QSize(2970, 800))
        self.MainPannel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.MainPannel.setSizeIncrement(QtCore.QSize(3, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.MainPannel.setFont(font)
        self.MainPannel.setStyleSheet("background-color:rgb(169, 228, 255)")
        self.MainPannel.setObjectName("MainPannel")
        self.DottedLine1_8 = QtWidgets.QFrame(self.MainPannel)
        self.DottedLine1_8.setGeometry(QtCore.QRect(121, 714, 2790, 2))
        self.DottedLine1_8.setStyleSheet("border-style: dotted;\n"
" border-width: 2 px;\n"
"border-left: none;\n"
"border-right: none;")
        self.DottedLine1_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.DottedLine1_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DottedLine1_8.setObjectName("DottedLine1_8")
        self.DottedLine1_5 = QtWidgets.QFrame(self.MainPannel)
        self.DottedLine1_5.setGeometry(QtCore.QRect(121, 547, 2790, 2))
        self.DottedLine1_5.setStyleSheet("border-style: dotted;\n"
" border-width: 2 px;\n"
"border-left: none;\n"
"border-right: none;")
        self.DottedLine1_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.DottedLine1_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DottedLine1_5.setObjectName("DottedLine1_5")
        self.DottedLine1_6 = QtWidgets.QFrame(self.MainPannel)
        self.DottedLine1_6.setGeometry(QtCore.QRect(119, 325, 2790, 2))
        self.DottedLine1_6.setStyleSheet("border-style: dotted;\n"
" border-width: 2 px;\n"
"border-left: none;\n"
"border-right: none;")
        self.DottedLine1_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.DottedLine1_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DottedLine1_6.setObjectName("DottedLine1_6")
        self.DottedLine1 = QtWidgets.QFrame(self.MainPannel)
        self.DottedLine1.setGeometry(QtCore.QRect(120, 74, 2790, 2))
        self.DottedLine1.setStyleSheet("border-style: dotted;\n"
" border-width: 2 px;\n"
"border-left: none;\n"
"border-right: none;")
        self.DottedLine1.setFrameShape(QtWidgets.QFrame.HLine)
        self.DottedLine1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DottedLine1.setObjectName("DottedLine1")
        self.DottedLine1_4 = QtWidgets.QFrame(self.MainPannel)
        self.DottedLine1_4.setGeometry(QtCore.QRect(121, 631, 2790, 2))
        self.DottedLine1_4.setStyleSheet("border-style: dotted;\n"
" border-width: 2 px;\n"
"border-left: none;\n"
"border-right: none;")
        self.DottedLine1_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.DottedLine1_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DottedLine1_4.setObjectName("DottedLine1_4")
        self.DottedLine1_7 = QtWidgets.QFrame(self.MainPannel)
        self.DottedLine1_7.setGeometry(QtCore.QRect(120, 241, 2790, 2))
        self.DottedLine1_7.setStyleSheet("border-style: dotted;\n"
" border-width: 2 px;\n"
"border-left: none;\n"
"border-right: none;")
        self.DottedLine1_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.DottedLine1_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DottedLine1_7.setObjectName("DottedLine1_7")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.MainPannel)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(121, -9, 2791, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.HorizonalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.HorizonalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.HorizonalLayout.setContentsMargins(0, 7, 11, 0)
        self.HorizonalLayout.setSpacing(0)
        self.HorizonalLayout.setObjectName("HorizonalLayout")
        self.Label1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Label1.setStyleSheet("background-color:#0066da;\n"
"color:#CCCCCC;")
        self.Label1.setObjectName("Label1")
        self.HorizonalLayout.addWidget(self.Label1)
        self.line_9 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_9.setStyleSheet("background-color:#0066da;")
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.HorizonalLayout.addWidget(self.line_9)
        self.label_26 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_26.setStyleSheet("background-color:#0066da;\n"
"color:#CCCCCC;")
        self.label_26.setObjectName("label_26")
        self.HorizonalLayout.addWidget(self.label_26)
        self.line_10 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_10.setStyleSheet("background-color:#0066da;")
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.HorizonalLayout.addWidget(self.line_10)
        self.label_24 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_24.setStyleSheet("background-color:#0066da;\n"
"color:#CCCCCC;")
        self.label_24.setObjectName("label_24")
        self.HorizonalLayout.addWidget(self.label_24)
        self.line_11 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_11.setStyleSheet("background-color:#0066da;")
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.HorizonalLayout.addWidget(self.line_11)
        self.label_23 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_23.setStyleSheet("background-color:#0066da;\n"
"color:#CCCCCC;")
        self.label_23.setObjectName("label_23")
        self.HorizonalLayout.addWidget(self.label_23)
        self.line_12 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_12.setStyleSheet("background-color:#0066da;")
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.HorizonalLayout.addWidget(self.line_12)
        self.label_21 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_21.setStyleSheet("background-color:#0066da;\n"
"color:#CCCCCC;")
        self.label_21.setObjectName("label_21")
        self.HorizonalLayout.addWidget(self.label_21)
        self.line_13 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_13.setStyleSheet("background-color:#0066da;")
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.HorizonalLayout.addWidget(self.line_13)
        self.label_22 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_22.setStyleSheet("background-color:#0066da;\n"
"color:#CCCCCC;")
        self.label_22.setObjectName("label_22")
        self.HorizonalLayout.addWidget(self.label_22)
        self.line_14 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_14.setStyleSheet("background-color:#0066da;")
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.HorizonalLayout.addWidget(self.line_14)
        self.label_20 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_20.setStyleSheet("background-color:#0066da;\n"
"color:#CCCCCC;")
        self.label_20.setObjectName("label_20")
        self.HorizonalLayout.addWidget(self.label_20)
        self.line_15 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_15.setStyleSheet("background-color:#0066da;")
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.HorizonalLayout.addWidget(self.line_15)
        self.label_17 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_17.setStyleSheet("background-color:#0066da;\n"
"color:#CCCCCC;")
        self.label_17.setObjectName("label_17")
        self.HorizonalLayout.addWidget(self.label_17)
        self.line_16 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_16.setStyleSheet("background-color:#0066da;")
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.HorizonalLayout.addWidget(self.line_16)
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_16.setStyleSheet("background-color:#0066da;\n"
"color:#CCCCCC;")
        self.label_16.setObjectName("label_16")
        self.HorizonalLayout.addWidget(self.label_16)
        self.line_17 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_17.setStyleSheet("background-color:#0066da;")
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.HorizonalLayout.addWidget(self.line_17)
        self.label_19 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_19.setStyleSheet("background-color:#0066da;\n"
"color:#CCCCCC;")
        self.label_19.setObjectName("label_19")
        self.HorizonalLayout.addWidget(self.label_19)
        self.line_18 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_18.setStyleSheet("background-color:#0066da;")
        self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.HorizonalLayout.addWidget(self.line_18)
        self.label_15 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_15.setStyleSheet("background-color:#0066da;\n"
"color:#CCCCCC;")
        self.label_15.setObjectName("label_15")
        self.HorizonalLayout.addWidget(self.label_15)
        self.line_19 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_19.setStyleSheet("background-color:#0066da;")
        self.line_19.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.HorizonalLayout.addWidget(self.line_19)
        self.label_18 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_18.setStyleSheet("background-color:#0066da;\n"
"color:#CCCCCC;")
        self.label_18.setObjectName("label_18")
        self.HorizonalLayout.addWidget(self.label_18)
        self.line_20 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_20.setStyleSheet("background-color:#0066da;")
        self.line_20.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.HorizonalLayout.addWidget(self.line_20)
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_14.setStyleSheet("background-color:#0066da;\n"
"color:#CCCCCC;")
        self.label_14.setObjectName("label_14")
        self.HorizonalLayout.addWidget(self.label_14)
        self.line_21 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_21.setStyleSheet("background-color:#0066da;")
        self.line_21.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.HorizonalLayout.addWidget(self.line_21)
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_13.setStyleSheet("background-color:#0066da;\n"
"color:#CCCCCC;")
        self.label_13.setObjectName("label_13")
        self.HorizonalLayout.addWidget(self.label_13)
        self.line_22 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_22.setStyleSheet("background-color:#0066da;")
        self.line_22.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.HorizonalLayout.addWidget(self.line_22)
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_12.setStyleSheet("background-color:#0066da;\n"
"color:#CCCCCC;")
        self.label_12.setObjectName("label_12")
        self.HorizonalLayout.addWidget(self.label_12)
        self.line_23 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_23.setStyleSheet("background-color:#0066da;")
        self.line_23.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.HorizonalLayout.addWidget(self.line_23)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_11.setStyleSheet("background-color:#0066da;\n"
"color:#CCCCCC;")
        self.label_11.setObjectName("label_11")
        self.HorizonalLayout.addWidget(self.label_11)
        self.line_24 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_24.setStyleSheet("background-color:#0066da;")
        self.line_24.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.HorizonalLayout.addWidget(self.line_24)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_10.setStyleSheet("background-color:#0066da;\n"
"color:#CCCCCC;")
        self.label_10.setObjectName("label_10")
        self.HorizonalLayout.addWidget(self.label_10)
        self.line_25 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_25.setStyleSheet("background-color:#0066da;")
        self.line_25.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_25.setObjectName("line_25")
        self.HorizonalLayout.addWidget(self.line_25)
        self.label_28 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_28.setStyleSheet("background-color:#0066da;\n"
"color:#CCCCCC;")
        self.label_28.setObjectName("label_28")
        self.HorizonalLayout.addWidget(self.label_28)
        self.line_26 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_26.setStyleSheet("background-color:#0066da;")
        self.line_26.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_26.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_26.setObjectName("line_26")
        self.HorizonalLayout.addWidget(self.line_26)
        self.label_29 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_29.setStyleSheet("background-color:#0066da;\n"
"color:#CCCCCC;")
        self.label_29.setObjectName("label_29")
        self.HorizonalLayout.addWidget(self.label_29)
        self.line_27 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_27.setStyleSheet("background-color:#0066da;")
        self.line_27.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_27.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_27.setObjectName("line_27")
        self.HorizonalLayout.addWidget(self.line_27)
        self.label_31 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_31.setStyleSheet("background-color:#0066da;\n"
"color:#CCCCCC;")
        self.label_31.setObjectName("label_31")
        self.HorizonalLayout.addWidget(self.label_31)
        self.line_28 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_28.setStyleSheet("background-color:#0066da;")
        self.line_28.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_28.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_28.setObjectName("line_28")
        self.HorizonalLayout.addWidget(self.line_28)
        self.label_27 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_27.setStyleSheet("background-color:#0066da;\n"
"color:#CCCCCC;")
        self.label_27.setObjectName("label_27")
        self.HorizonalLayout.addWidget(self.label_27)
        self.line_29 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_29.setStyleSheet("background-color:#0066da;")
        self.line_29.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_29.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_29.setObjectName("line_29")
        self.HorizonalLayout.addWidget(self.line_29)
        self.label_25 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_25.setStyleSheet("background-color:#0066da;\n"
"color:#CCCCCC;")
        self.label_25.setObjectName("label_25")
        self.HorizonalLayout.addWidget(self.label_25)
        self.line_30 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_30.setStyleSheet("background-color:#0066da;")
        self.line_30.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_30.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_30.setObjectName("line_30")
        self.HorizonalLayout.addWidget(self.line_30)
        self.label_32 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_32.setStyleSheet("background-color:#0066da;\n"
"color:#CCCCCC;")
        self.label_32.setObjectName("label_32")
        self.HorizonalLayout.addWidget(self.label_32)
        self.line_31 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_31.setStyleSheet("background-color:#0066da;")
        self.line_31.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_31.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_31.setObjectName("line_31")
        self.HorizonalLayout.addWidget(self.line_31)
        self.label_30 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_30.setStyleSheet("background-color:#0066da;\n"
"color:#CCCCCC;")
        self.label_30.setObjectName("label_30")
        self.HorizonalLayout.addWidget(self.label_30)
        self.DottedLine1_3 = QtWidgets.QFrame(self.MainPannel)
        self.DottedLine1_3.setGeometry(QtCore.QRect(120, 408, 2790, 2))
        self.DottedLine1_3.setStyleSheet("border-style: dotted;\n"
" border-width: 2 px;\n"
"border-left: none;\n"
"border-right: none;")
        self.DottedLine1_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.DottedLine1_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DottedLine1_3.setObjectName("DottedLine1_3")
        self.DottedLine1_2 = QtWidgets.QFrame(self.MainPannel)
        self.DottedLine1_2.setGeometry(QtCore.QRect(120, 158, 2790, 2))
        self.DottedLine1_2.setStyleSheet("border-style: dotted;\n"
" border-width: 2 px;\n"
"border-left: none;\n"
"border-right: none;")
        self.DottedLine1_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.DottedLine1_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DottedLine1_2.setObjectName("DottedLine1_2")
        self.V1 = QtWidgets.QFrame(self.MainPannel)
        self.V1.setGeometry(QtCore.QRect(226, 76, 2, 712))
        self.V1.setStyleSheet("border-style: dotted; border-width: 2px; border-bottom: none; border-top: none;")
        self.V1.setFrameShape(QtWidgets.QFrame.VLine)
        self.V1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V1.setObjectName("V1")
        self.V2 = QtWidgets.QFrame(self.MainPannel)
        self.V2.setGeometry(QtCore.QRect(333, 76, 2, 712))
        self.V2.setStyleSheet("border-style: dotted; border-width: 2px; border-bottom: none; border-top: none;")
        self.V2.setFrameShape(QtWidgets.QFrame.VLine)
        self.V2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V2.setObjectName("V2")
        self.V4 = QtWidgets.QFrame(self.MainPannel)
        self.V4.setGeometry(QtCore.QRect(550, 76, 2, 712))
        self.V4.setStyleSheet("border-style: dotted; border-width: 2px; border-bottom: none; border-top: none;")
        self.V4.setFrameShape(QtWidgets.QFrame.VLine)
        self.V4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V4.setObjectName("V4")
        self.V9 = QtWidgets.QFrame(self.MainPannel)
        self.V9.setGeometry(QtCore.QRect(1084, 76, 2, 712))
        self.V9.setStyleSheet("border-style: dotted; border-width: 2px; border-bottom: none; border-top: none;")
        self.V9.setFrameShape(QtWidgets.QFrame.VLine)
        self.V9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V9.setObjectName("V9")
        self.V5 = QtWidgets.QFrame(self.MainPannel)
        self.V5.setGeometry(QtCore.QRect(656, 76, 2, 712))
        self.V5.setStyleSheet("border-style: dotted; border-width: 2px; border-bottom: none; border-top: none;")
        self.V5.setFrameShape(QtWidgets.QFrame.VLine)
        self.V5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V5.setObjectName("V5")
        self.V10 = QtWidgets.QFrame(self.MainPannel)
        self.V10.setGeometry(QtCore.QRect(1192, 76, 2, 712))
        self.V10.setStyleSheet("border-style: dotted; border-width: 2px; border-bottom: none; border-top: none;")
        self.V10.setFrameShape(QtWidgets.QFrame.VLine)
        self.V10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V10.setObjectName("V10")
        self.V11 = QtWidgets.QFrame(self.MainPannel)
        self.V11.setGeometry(QtCore.QRect(1302, 76, 2, 712))
        self.V11.setStyleSheet("border-style: dotted; border-width: 2px; border-bottom: none; border-top: none;")
        self.V11.setFrameShape(QtWidgets.QFrame.VLine)
        self.V11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V11.setObjectName("V11")
        self.V12 = QtWidgets.QFrame(self.MainPannel)
        self.V12.setGeometry(QtCore.QRect(1410, 76, 2, 712))
        self.V12.setStyleSheet("border-style: dotted; border-width: 2px; border-bottom: none; border-top: none;")
        self.V12.setFrameShape(QtWidgets.QFrame.VLine)
        self.V12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V12.setObjectName("V12")
        self.V6 = QtWidgets.QFrame(self.MainPannel)
        self.V6.setGeometry(QtCore.QRect(765, 76, 2, 712))
        self.V6.setStyleSheet("border-style: dotted; border-width: 2px; border-bottom: none; border-top: none;")
        self.V6.setFrameShape(QtWidgets.QFrame.VLine)
        self.V6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V6.setObjectName("V6")
        self.V7 = QtWidgets.QFrame(self.MainPannel)
        self.V7.setGeometry(QtCore.QRect(868, 76, 2, 712))
        self.V7.setStyleSheet("border-style: dotted; border-width: 2px; border-bottom: none; border-top: none;")
        self.V7.setFrameShape(QtWidgets.QFrame.VLine)
        self.V7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V7.setObjectName("V7")
        self.V8 = QtWidgets.QFrame(self.MainPannel)
        self.V8.setGeometry(QtCore.QRect(978, 76, 2, 712))
        self.V8.setStyleSheet("border-style: dotted; border-width: 2px; border-bottom: none; border-top: none;")
        self.V8.setFrameShape(QtWidgets.QFrame.VLine)
        self.V8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V8.setObjectName("V8")
        self.V3 = QtWidgets.QFrame(self.MainPannel)
        self.V3.setGeometry(QtCore.QRect(442, 76, 2, 712))
        self.V3.setStyleSheet("border-style: dotted; border-width: 2px; border-bottom: none; border-top: none;")
        self.V3.setFrameShape(QtWidgets.QFrame.VLine)
        self.V3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V3.setObjectName("V3")
        self.V12_2 = QtWidgets.QFrame(self.MainPannel)
        self.V12_2.setGeometry(QtCore.QRect(1517, 76, 2, 712))
        self.V12_2.setStyleSheet("border-style: dotted; border-width: 2px; border-bottom: none; border-top: none;")
        self.V12_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.V12_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V12_2.setObjectName("V12_2")
        self.V12_3 = QtWidgets.QFrame(self.MainPannel)
        self.V12_3.setGeometry(QtCore.QRect(1625, 76, 2, 712))
        self.V12_3.setStyleSheet("border-style: dotted; border-width: 2px; border-bottom: none; border-top: none;")
        self.V12_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.V12_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V12_3.setObjectName("V12_3")
        self.V12_4 = QtWidgets.QFrame(self.MainPannel)
        self.V12_4.setGeometry(QtCore.QRect(1733, 76, 2, 712))
        self.V12_4.setStyleSheet("border-style: dotted; border-width: 2px; border-bottom: none; border-top: none;")
        self.V12_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.V12_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V12_4.setObjectName("V12_4")
        self.V12_5 = QtWidgets.QFrame(self.MainPannel)
        self.V12_5.setGeometry(QtCore.QRect(1840, 76, 2, 712))
        self.V12_5.setStyleSheet("border-style: dotted; border-width: 2px; border-bottom: none; border-top: none;")
        self.V12_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.V12_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V12_5.setObjectName("V12_5")
        self.V12_6 = QtWidgets.QFrame(self.MainPannel)
        self.V12_6.setGeometry(QtCore.QRect(1948, 76, 2, 712))
        self.V12_6.setStyleSheet("border-style: dotted; border-width: 2px; border-bottom: none; border-top: none;")
        self.V12_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.V12_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V12_6.setObjectName("V12_6")
        self.V12_7 = QtWidgets.QFrame(self.MainPannel)
        self.V12_7.setGeometry(QtCore.QRect(2055, 76, 2, 712))
        self.V12_7.setStyleSheet("border-style: dotted; border-width: 2px; border-bottom: none; border-top: none;")
        self.V12_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.V12_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V12_7.setObjectName("V12_7")
        self.V12_8 = QtWidgets.QFrame(self.MainPannel)
        self.V12_8.setGeometry(QtCore.QRect(2263, 76, 2, 712))
        self.V12_8.setStyleSheet("border-style: dotted; border-width: 2px; border-bottom: none; border-top: none;")
        self.V12_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.V12_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V12_8.setObjectName("V12_8")
        self.V12_9 = QtWidgets.QFrame(self.MainPannel)
        self.V12_9.setGeometry(QtCore.QRect(2370, 76, 2, 712))
        self.V12_9.setStyleSheet("border-style: dotted; border-width: 2px; border-bottom: none; border-top: none;")
        self.V12_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.V12_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V12_9.setObjectName("V12_9")
        self.V12_10 = QtWidgets.QFrame(self.MainPannel)
        self.V12_10.setGeometry(QtCore.QRect(2578, 76, 2, 712))
        self.V12_10.setStyleSheet("border-style: dotted; border-width: 2px; border-bottom: none; border-top: none;")
        self.V12_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.V12_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V12_10.setObjectName("V12_10")
        self.V12_11 = QtWidgets.QFrame(self.MainPannel)
        self.V12_11.setGeometry(QtCore.QRect(2686, 76, 2, 712))
        self.V12_11.setStyleSheet("border-style: dotted; border-width: 2px; border-bottom: none; border-top: none;")
        self.V12_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.V12_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V12_11.setObjectName("V12_11")
        self.V12_12 = QtWidgets.QFrame(self.MainPannel)
        self.V12_12.setGeometry(QtCore.QRect(2910, 76, 2, 712))
        self.V12_12.setStyleSheet("border-style: dotted; border-width: 2px; border-bottom: none; border-top: none;")
        self.V12_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.V12_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V12_12.setObjectName("V12_12")
        self.V12_13 = QtWidgets.QFrame(self.MainPannel)
        self.V12_13.setGeometry(QtCore.QRect(2793, 76, 2, 712))
        self.V12_13.setStyleSheet("border-style: dotted; border-width: 2px; border-bottom: none; border-top: none;")
        self.V12_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.V12_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V12_13.setObjectName("V12_13")
        self.DottedLine1_9 = QtWidgets.QFrame(self.MainPannel)
        self.DottedLine1_9.setGeometry(QtCore.QRect(120, 790, 2790, 2))
        self.DottedLine1_9.setStyleSheet("border-style: dotted;\n"
" border-width: 2 px;\n"
"border-left: none;\n"
"border-right: none;")
        self.DottedLine1_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.DottedLine1_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DottedLine1_9.setObjectName("DottedLine1_9")
        self.INO = QtWidgets.QPushButton(self.MainPannel)
        self.INO.setGeometry(QtCore.QRect(130, 450, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.INO.setFont(font)
        self.INO.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.INO.setObjectName("INO")
        self.INI = QtWidgets.QPushButton(self.MainPannel)
        self.INI.setGeometry(QtCore.QRect(237, 450, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.INI.setFont(font)
        self.INI.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.INI.setObjectName("INI")
        self.PFP = QtWidgets.QPushButton(self.MainPannel)
        self.PFP.setGeometry(QtCore.QRect(343, 450, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.PFP.setFont(font)
        self.PFP.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.PFP.setObjectName("PFP")
        self.FWT = QtWidgets.QPushButton(self.MainPannel)
        self.FWT.setGeometry(QtCore.QRect(560, 450, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.FWT.setFont(font)
        self.FWT.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.FWT.setObjectName("FWT")
        self.EWC = QtWidgets.QPushButton(self.MainPannel)
        self.EWC.setGeometry(QtCore.QRect(453, 90, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.EWC.setFont(font)
        self.EWC.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.EWC.setObjectName("EWC")
        self.EWC1 = QtWidgets.QPushButton(self.MainPannel)
        self.EWC1.setGeometry(QtCore.QRect(453, 260, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.EWC1.setFont(font)
        self.EWC1.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.EWC1.setObjectName("EWC1")
        self.EXE = QtWidgets.QPushButton(self.MainPannel)
        self.EXE.setGeometry(QtCore.QRect(453, 650, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.EXE.setFont(font)
        self.EXE.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.EXE.setObjectName("EXE")
        self.HE1 = QtWidgets.QPushButton(self.MainPannel)
        self.HE1.setGeometry(QtCore.QRect(666, 340, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.HE1.setFont(font)
        self.HE1.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.HE1.setObjectName("HE1")
        self.INS = QtWidgets.QPushButton(self.MainPannel)
        self.INS.setGeometry(QtCore.QRect(666, 570, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.INS.setFont(font)
        self.INS.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.INS.setObjectName("INS")
        self.CPI = QtWidgets.QPushButton(self.MainPannel)
        self.CPI.setGeometry(QtCore.QRect(666, 650, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.CPI.setFont(font)
        self.CPI.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.CPI.setObjectName("CPI")
        self.FIF = QtWidgets.QPushButton(self.MainPannel)
        self.FIF.setGeometry(QtCore.QRect(776, 570, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.FIF.setFont(font)
        self.FIF.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.FIF.setObjectName("FIF")
        self.UNE = QtWidgets.QPushButton(self.MainPannel)
        self.UNE.setGeometry(QtCore.QRect(883, 650, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.UNE.setFont(font)
        self.UNE.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.UNE.setObjectName("UNE")
        self.SBD = QtWidgets.QPushButton(self.MainPannel)
        self.SBD.setGeometry(QtCore.QRect(990, 570, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.SBD.setFont(font)
        self.SBD.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.SBD.setObjectName("SBD")
        self.UWC = QtWidgets.QPushButton(self.MainPannel)
        self.UWC.setGeometry(QtCore.QRect(990, 730, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.UWC.setFont(font)
        self.UWC.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.UWC.setObjectName("UWC")
        self.FIE = QtWidgets.QPushButton(self.MainPannel)
        self.FIE.setGeometry(QtCore.QRect(990, 340, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.FIE.setFont(font)
        self.FIE.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.FIE.setObjectName("FIE")
        self.FIW = QtWidgets.QPushButton(self.MainPannel)
        self.FIW.setGeometry(QtCore.QRect(1097, 260, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.FIW.setFont(font)
        self.FIW.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.FIW.setObjectName("FIW")
        self.FCE = QtWidgets.QPushButton(self.MainPannel)
        self.FCE.setGeometry(QtCore.QRect(1097, 173, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.FCE.setFont(font)
        self.FCE.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.FCE.setObjectName("FCE")
        self.SIW = QtWidgets.QPushButton(self.MainPannel)
        self.SIW.setGeometry(QtCore.QRect(1205, 260, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.SIW.setFont(font)
        self.SIW.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.SIW.setObjectName("SIW")
        self.SIE = QtWidgets.QPushButton(self.MainPannel)
        self.SIE.setGeometry(QtCore.QRect(1205, 340, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.SIE.setFont(font)
        self.SIE.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.SIE.setObjectName("SIE")
        self.SCE = QtWidgets.QPushButton(self.MainPannel)
        self.SCE.setGeometry(QtCore.QRect(1310, 173, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.SCE.setFont(font)
        self.SCE.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.SCE.setObjectName("SCE")
        self.CWC = QtWidgets.QPushButton(self.MainPannel)
        self.CWC.setGeometry(QtCore.QRect(1420, 90, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.CWC.setFont(font)
        self.CWC.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.CWC.setObjectName("CWC")
        self.COT = QtWidgets.QPushButton(self.MainPannel)
        self.COT.setGeometry(QtCore.QRect(1527, 385, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.COT.setFont(font)
        self.COT.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.COT.setObjectName("COT")
        self.HPT = QtWidgets.QPushButton(self.MainPannel)
        self.HPT.setGeometry(QtCore.QRect(1635, 387, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.HPT.setFont(font)
        self.HPT.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.HPT.setObjectName("HPT")
        self.REC = QtWidgets.QPushButton(self.MainPannel)
        self.REC.setGeometry(QtCore.QRect(1742, 387, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.REC.setFont(font)
        self.REC.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.REC.setObjectName("REC")
        self.ITN = QtWidgets.QPushButton(self.MainPannel)
        self.ITN.setGeometry(QtCore.QRect(1850, 560, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.ITN.setFont(font)
        self.ITN.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.ITN.setObjectName("ITN")
        self.UND = QtWidgets.QPushButton(self.MainPannel)
        self.UND.setGeometry(QtCore.QRect(1850, 644, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.UND.setFont(font)
        self.UND.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.UND.setObjectName("UND")
        self.TUK = QtWidgets.QPushButton(self.MainPannel)
        self.TUK.setGeometry(QtCore.QRect(1960, 420, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.TUK.setFont(font)
        self.TUK.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.TUK.setObjectName("TUK")
        self.WEG = QtWidgets.QPushButton(self.MainPannel)
        self.WEG.setGeometry(QtCore.QRect(1960, 480, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.WEG.setFont(font)
        self.WEG.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.WEG.setObjectName("WEG")
        self.WCT = QtWidgets.QPushButton(self.MainPannel)
        self.WCT.setGeometry(QtCore.QRect(1960, 720, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.WCT.setFont(font)
        self.WCT.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.WCT.setObjectName("WCT")
        self.GAU = QtWidgets.QPushButton(self.MainPannel)
        self.GAU.setGeometry(QtCore.QRect(2065, 420, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.GAU.setFont(font)
        self.GAU.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.GAU.setObjectName("GAU")
        self.PPR = QtWidgets.QPushButton(self.MainPannel)
        self.PPR.setGeometry(QtCore.QRect(2168, 420, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.PPR.setFont(font)
        self.PPR.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.PPR.setObjectName("PPR")
        self.SWT = QtWidgets.QPushButton(self.MainPannel)
        self.SWT.setGeometry(QtCore.QRect(2065, 480, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.SWT.setFont(font)
        self.SWT.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.SWT.setObjectName("SWT")
        self.CUP = QtWidgets.QPushButton(self.MainPannel)
        self.CUP.setGeometry(QtCore.QRect(2273, 385, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.CUP.setFont(font)
        self.CUP.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.CUP.setObjectName("CUP")
        self.CUR = QtWidgets.QPushButton(self.MainPannel)
        self.CUR.setGeometry(QtCore.QRect(2380, 385, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.CUR.setFont(font)
        self.CUR.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.CUR.setObjectName("CUR")
        self.SCS = QtWidgets.QPushButton(self.MainPannel)
        self.SCS.setGeometry(QtCore.QRect(2480, 385, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.SCS.setFont(font)
        self.SCS.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.SCS.setObjectName("SCS")
        self.DCS = QtWidgets.QPushButton(self.MainPannel)
        self.DCS.setGeometry(QtCore.QRect(2590, 385, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.DCS.setFont(font)
        self.DCS.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.DCS.setObjectName("DCS")
        self.PSI = QtWidgets.QPushButton(self.MainPannel)
        self.PSI.setGeometry(QtCore.QRect(2695, 385, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.PSI.setFont(font)
        self.PSI.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.PSI.setObjectName("PSI")
        self.DEL = QtWidgets.QPushButton(self.MainPannel)
        self.DEL.setGeometry(QtCore.QRect(2807, 385, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.DEL.setFont(font)
        self.DEL.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.DEL.setObjectName("DEL")
        self.label_34 = QtWidgets.QLabel(self.MainPannel)
        self.label_34.setGeometry(QtCore.QRect(298, 450, 28, 28))
        self.label_34.setMinimumSize(QtCore.QSize(0, 0))
        self.label_34.setText("")
        self.label_34.setPixmap(QtGui.QPixmap(image))
        self.label_34.setScaledContents(True)
        self.label_34.setObjectName("label_34")
        self.label_42 = QtWidgets.QLabel(self.MainPannel)
        self.label_42.setGeometry(QtCore.QRect(620, 450, 28, 28))
        self.label_42.setMinimumSize(QtCore.QSize(0, 0))
        self.label_42.setText("")
        self.label_42.setPixmap(QtGui.QPixmap(image))
        self.label_42.setScaledContents(True)
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.MainPannel)
        self.label_43.setGeometry(QtCore.QRect(1158, 260, 28, 28))
        self.label_43.setMinimumSize(QtCore.QSize(0, 0))
        self.label_43.setText("")
        self.label_43.setPixmap(QtGui.QPixmap(image))
        self.label_43.setScaledContents(True)
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.MainPannel)
        self.label_44.setGeometry(QtCore.QRect(1805, 390, 26, 26))
        self.label_44.setMinimumSize(QtCore.QSize(0, 0))
        self.label_44.setText("")
        self.label_44.setPixmap(QtGui.QPixmap(image))
        self.label_44.setScaledContents(True)
        self.label_44.setObjectName("label_44")
        self.label_35 = QtWidgets.QLabel(self.MainPannel)
        self.label_35.setGeometry(QtCore.QRect(1910, 645, 28, 28))
        self.label_35.setMinimumSize(QtCore.QSize(0, 0))
        self.label_35.setText("")
        self.label_35.setPixmap(QtGui.QPixmap(image))
        self.label_35.setScaledContents(True)
        self.label_35.setObjectName("label_35")
        self.label_37 = QtWidgets.QLabel(self.MainPannel)
        self.label_37.setGeometry(QtCore.QRect(2440, 386, 28, 28))
        self.label_37.setMinimumSize(QtCore.QSize(0, 0))
        self.label_37.setText("")
        self.label_37.setPixmap(QtGui.QPixmap(image))
        self.label_37.setScaledContents(True)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.MainPannel)
        self.label_38.setGeometry(QtCore.QRect(2757, 385, 28, 28))
        self.label_38.setMinimumSize(QtCore.QSize(0, 0))
        self.label_38.setText("")
        self.label_38.setPixmap(QtGui.QPixmap(image))
        self.label_38.setScaledContents(True)
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.MainPannel)
        self.label_39.setGeometry(QtCore.QRect(2868, 385, 28, 28))
        self.label_39.setMinimumSize(QtCore.QSize(0, 0))
        self.label_39.setText("")
        self.label_39.setPixmap(QtGui.QPixmap(image))
        self.label_39.setScaledContents(True)
        self.label_39.setObjectName("label_39")
        self.widget = QtWidgets.QWidget(self.MainPannel)
        self.widget.setGeometry(QtCore.QRect(0, 0, 121, 791))
        self.widget.setStyleSheet("background-color:#0066da;")
        self.widget.setObjectName("widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 121, 791))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.Teams_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Teams_4.setContentsMargins(0, 0, 0, 0)
        self.Teams_4.setObjectName("Teams_4")
        self.label_61 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_61.setStyleSheet("color:#CCCCCC;")
        self.label_61.setObjectName("label_61")
        self.Teams_4.addWidget(self.label_61)
        self.line_48 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_48.setStyleSheet("color:#0091DA\n"
"")
        self.line_48.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_48.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_48.setObjectName("line_48")
        self.Teams_4.addWidget(self.line_48)
        self.label_62 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_62.setStyleSheet("color:#CCCCCC;")
        self.label_62.setObjectName("label_62")
        self.Teams_4.addWidget(self.label_62)
        self.line_49 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_49.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_49.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_49.setObjectName("line_49")
        self.Teams_4.addWidget(self.line_49)
        self.label_63 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_63.setStyleSheet("color:#CCCCCC;")
        self.label_63.setObjectName("label_63")
        self.Teams_4.addWidget(self.label_63)
        self.line_50 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_50.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_50.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_50.setObjectName("line_50")
        self.Teams_4.addWidget(self.line_50)
        self.label_64 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_64.setStyleSheet("color:#CCCCCC;")
        self.label_64.setObjectName("label_64")
        self.Teams_4.addWidget(self.label_64)
        self.line_51 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_51.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_51.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_51.setObjectName("line_51")
        self.Teams_4.addWidget(self.line_51)
        self.label_65 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_65.setStyleSheet("color:#CCCCCC;")
        self.label_65.setObjectName("label_65")
        self.Teams_4.addWidget(self.label_65)
        self.line_52 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_52.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_52.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_52.setObjectName("line_52")
        self.Teams_4.addWidget(self.line_52)
        self.label_66 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_66.setStyleSheet("color:#CCCCCC;")
        self.label_66.setObjectName("label_66")
        self.Teams_4.addWidget(self.label_66)
        self.line_53 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_53.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_53.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_53.setObjectName("line_53")
        self.Teams_4.addWidget(self.line_53)
        self.label_67 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_67.setStyleSheet("color:#CCCCCC;")
        self.label_67.setObjectName("label_67")
        self.Teams_4.addWidget(self.label_67)
        self.line_54 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_54.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_54.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_54.setObjectName("line_54")
        self.Teams_4.addWidget(self.line_54)
        self.label_68 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_68.setStyleSheet("color:#CCCCCC;")
        self.label_68.setObjectName("label_68")
        self.Teams_4.addWidget(self.label_68)
        self.line_55 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_55.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_55.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_55.setObjectName("line_55")
        self.Teams_4.addWidget(self.line_55)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("color:#CCCCCC;")
        self.label.setObjectName("label")
        self.Teams_4.addWidget(self.label)
        self.testline_5 = QtWidgets.QFrame(self.MainPannel)
        self.testline_5.setGeometry(QtCore.QRect(280, 110, 221, 3))
        self.testline_5.setMaximumSize(QtCore.QSize(16777215, 3))
        self.testline_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_5.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_5.setStyleSheet("background-color:#fe6f5e;")
        self.testline_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.testline_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_5.setLineWidth(0)
        self.testline_5.setMidLineWidth(0)
        self.testline_5.setObjectName("testline_5")
        self.testline_52 = QtWidgets.QFrame(self.MainPannel)
        self.testline_52.setGeometry(QtCore.QRect(390, 480, 3, 271))
        self.testline_52.setMinimumSize(QtCore.QSize(3, 0))
        self.testline_52.setMaximumSize(QtCore.QSize(3, 16777215))
        self.testline_52.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_52.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_52.setStyleSheet("background-color:#fe6f5e;")
        self.testline_52.setFrameShape(QtWidgets.QFrame.VLine)
        self.testline_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_52.setLineWidth(0)
        self.testline_52.setMidLineWidth(0)
        self.testline_52.setObjectName("testline_52")
        self.testline_53 = QtWidgets.QFrame(self.MainPannel)
        self.testline_53.setGeometry(QtCore.QRect(390, 750, 321, 3))
        self.testline_53.setMaximumSize(QtCore.QSize(16777215, 3))
        self.testline_53.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_53.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_53.setStyleSheet("background-color:#fe6f5e;")
        self.testline_53.setFrameShape(QtWidgets.QFrame.HLine)
        self.testline_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_53.setLineWidth(0)
        self.testline_53.setMidLineWidth(0)
        self.testline_53.setObjectName("testline_53")
        self.testline_54 = QtWidgets.QFrame(self.MainPannel)
        self.testline_54.setGeometry(QtCore.QRect(710, 670, 3, 81))
        self.testline_54.setMinimumSize(QtCore.QSize(3, 0))
        self.testline_54.setMaximumSize(QtCore.QSize(3, 16777215))
        self.testline_54.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_54.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_54.setStyleSheet("background-color:#fe6f5e;")
        self.testline_54.setFrameShape(QtWidgets.QFrame.VLine)
        self.testline_54.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_54.setLineWidth(0)
        self.testline_54.setMidLineWidth(0)
        self.testline_54.setObjectName("testline_54")

        self.testline_4 = QtWidgets.QFrame(self.MainPannel)
        self.testline_4.setGeometry(QtCore.QRect(280, 110, 3, 351))
        self.testline_4.setMinimumSize(QtCore.QSize(3, 0))
        self.testline_4.setMaximumSize(QtCore.QSize(3, 16777215))
        self.testline_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_4.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_4.setStyleSheet("background-color:#fe6f5e;")
        self.testline_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.testline_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_4.setLineWidth(0)
        self.testline_4.setMidLineWidth(0)
        self.testline_4.setObjectName("testline_4")
        self.testline_8 = QtWidgets.QFrame(self.MainPannel)
        self.testline_8.setGeometry(QtCore.QRect(710, 200, 641, 3))
        self.testline_8.setMaximumSize(QtCore.QSize(16777215, 3))
        self.testline_8.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_8.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_8.setStyleSheet("background-color:#fe6f5e;")
        self.testline_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.testline_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_8.setLineWidth(0)
        self.testline_8.setMidLineWidth(0)
        self.testline_8.setObjectName("testline_8")
        self.testline_9 = QtWidgets.QFrame(self.MainPannel)
        self.testline_9.setGeometry(QtCore.QRect(280, 280, 321, 3))
        self.testline_9.setMaximumSize(QtCore.QSize(16777215, 3))
        self.testline_9.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_9.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_9.setStyleSheet("background-color:#fe6f5e;")
        self.testline_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.testline_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_9.setLineWidth(0)
        self.testline_9.setMidLineWidth(0)
        self.testline_9.setObjectName("testline_9")
        self.testline_10 = QtWidgets.QFrame(self.MainPannel)
        self.testline_10.setGeometry(QtCore.QRect(280, 380, 221, 3))
        self.testline_10.setMaximumSize(QtCore.QSize(16777215, 3))
        self.testline_10.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_10.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_10.setStyleSheet("background-color:#fe6f5e;")
        self.testline_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.testline_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_10.setLineWidth(0)
        self.testline_10.setMidLineWidth(0)
        self.testline_10.setObjectName("testline_10")
        self.testline_7 = QtWidgets.QFrame(self.MainPannel)
        self.testline_7.setGeometry(QtCore.QRect(600, 280, 3, 401))
        self.testline_7.setMinimumSize(QtCore.QSize(3, 0))
        self.testline_7.setMaximumSize(QtCore.QSize(3, 16777215))
        self.testline_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_7.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_7.setStyleSheet("background-color:#fe6f5e;")
        self.testline_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.testline_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_7.setLineWidth(0)
        self.testline_7.setMidLineWidth(0)
        self.testline_7.setObjectName("testline_7")
        self.testline_11 = QtWidgets.QFrame(self.MainPannel)
        self.testline_11.setGeometry(QtCore.QRect(500, 380, 3, 301))
        self.testline_11.setMinimumSize(QtCore.QSize(3, 0))
        self.testline_11.setMaximumSize(QtCore.QSize(3, 16777215))
        self.testline_11.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_11.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_11.setStyleSheet("background-color:#fe6f5e;")
        self.testline_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.testline_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_11.setLineWidth(0)
        self.testline_11.setMidLineWidth(0)
        self.testline_11.setObjectName("testline_11")
        self.testline_12 = QtWidgets.QFrame(self.MainPannel)
        self.testline_12.setGeometry(QtCore.QRect(500, 680, 51, 3))
        self.testline_12.setMaximumSize(QtCore.QSize(16777215, 3))
        self.testline_12.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_12.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_12.setStyleSheet("background-color:#fe6f5e;")
        self.testline_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.testline_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_12.setLineWidth(0)
        self.testline_12.setMidLineWidth(0)
        self.testline_12.setObjectName("testline_12")
        self.testline_13 = QtWidgets.QFrame(self.MainPannel)
        self.testline_13.setGeometry(QtCore.QRect(550, 470, 3, 211))
        self.testline_13.setMinimumSize(QtCore.QSize(3, 0))
        self.testline_13.setMaximumSize(QtCore.QSize(3, 16777215))
        self.testline_13.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_13.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_13.setStyleSheet("background-color:#fe6f5e;")
        self.testline_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.testline_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_13.setLineWidth(0)
        self.testline_13.setMidLineWidth(0)
        self.testline_13.setObjectName("testline_13")
        self.testline_14 = QtWidgets.QFrame(self.MainPannel)
        self.testline_14.setGeometry(QtCore.QRect(550, 470, 161, 3))
        self.testline_14.setMaximumSize(QtCore.QSize(16777215, 3))
        self.testline_14.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_14.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_14.setStyleSheet("background-color:#fe6f5e;")
        self.testline_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.testline_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_14.setLineWidth(0)
        self.testline_14.setMidLineWidth(0)
        self.testline_14.setObjectName("testline_14")
        self.testline_15 = QtWidgets.QFrame(self.MainPannel)
        self.testline_15.setGeometry(QtCore.QRect(710, 200, 3, 271))
        self.testline_15.setMinimumSize(QtCore.QSize(3, 0))
        self.testline_15.setMaximumSize(QtCore.QSize(3, 16777215))
        self.testline_15.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_15.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_15.setStyleSheet("background-color:#fe6f5e;")
        self.testline_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.testline_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_15.setLineWidth(0)
        self.testline_15.setMidLineWidth(0)
        self.testline_15.setObjectName("testline_15")
        self.testline_16 = QtWidgets.QFrame(self.MainPannel)
        self.testline_16.setGeometry(QtCore.QRect(710, 360, 111, 3))
        self.testline_16.setMaximumSize(QtCore.QSize(16777215, 3))
        self.testline_16.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_16.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_16.setStyleSheet("background-color:#fe6f5e;")
        self.testline_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.testline_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_16.setLineWidth(0)
        self.testline_16.setMidLineWidth(0)
        self.testline_16.setObjectName("testline_16")
        self.testline_17 = QtWidgets.QFrame(self.MainPannel)
        self.testline_17.setGeometry(QtCore.QRect(820, 360, 3, 231))
        self.testline_17.setMinimumSize(QtCore.QSize(3, 0))
        self.testline_17.setMaximumSize(QtCore.QSize(3, 16777215))
        self.testline_17.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_17.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_17.setStyleSheet("background-color:#fe6f5e;")
        self.testline_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.testline_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_17.setLineWidth(0)
        self.testline_17.setMidLineWidth(0)
        self.testline_17.setObjectName("testline_17")
        self.testline_18 = QtWidgets.QFrame(self.MainPannel)
        self.testline_18.setGeometry(QtCore.QRect(600, 590, 321, 3))
        self.testline_18.setMaximumSize(QtCore.QSize(16777215, 3))
        self.testline_18.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_18.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_18.setStyleSheet("background-color:#fe6f5e;")
        self.testline_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.testline_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_18.setLineWidth(0)
        self.testline_18.setMidLineWidth(0)
        self.testline_18.setObjectName("testline_18")
        self.testline_19 = QtWidgets.QFrame(self.MainPannel)
        self.testline_19.setGeometry(QtCore.QRect(920, 360, 3, 231))
        self.testline_19.setMinimumSize(QtCore.QSize(3, 0))
        self.testline_19.setMaximumSize(QtCore.QSize(3, 16777215))
        self.testline_19.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_19.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_19.setStyleSheet("background-color:#fe6f5e;")
        self.testline_19.setFrameShape(QtWidgets.QFrame.VLine)
        self.testline_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_19.setLineWidth(0)
        self.testline_19.setMidLineWidth(0)
        self.testline_19.setObjectName("testline_19")
        self.testline_20 = QtWidgets.QFrame(self.MainPannel)
        self.testline_20.setGeometry(QtCore.QRect(920, 360, 121, 3))
        self.testline_20.setMaximumSize(QtCore.QSize(16777215, 3))
        self.testline_20.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_20.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_20.setStyleSheet("background-color:#fe6f5e;")
        self.testline_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.testline_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_20.setLineWidth(0)
        self.testline_20.setMidLineWidth(0)
        self.testline_20.setObjectName("testline_20")
        self.testline_21 = QtWidgets.QFrame(self.MainPannel)
        self.testline_21.setGeometry(QtCore.QRect(1040, 280, 3, 311))
        self.testline_21.setMinimumSize(QtCore.QSize(3, 0))
        self.testline_21.setMaximumSize(QtCore.QSize(3, 16777215))
        self.testline_21.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_21.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_21.setStyleSheet("background-color:#fe6f5e;")
        self.testline_21.setFrameShape(QtWidgets.QFrame.VLine)
        self.testline_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_21.setLineWidth(0)
        self.testline_21.setMidLineWidth(0)
        self.testline_21.setObjectName("testline_21")
        self.testline_22 = QtWidgets.QFrame(self.MainPannel)
        self.testline_22.setGeometry(QtCore.QRect(1040, 280, 101, 3))
        self.testline_22.setMaximumSize(QtCore.QSize(16777215, 3))
        self.testline_22.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_22.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_22.setStyleSheet("background-color:#fe6f5e;")
        self.testline_22.setFrameShape(QtWidgets.QFrame.HLine)
        self.testline_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_22.setLineWidth(0)
        self.testline_22.setMidLineWidth(0)
        self.testline_22.setObjectName("testline_22")
        self.testline_23 = QtWidgets.QFrame(self.MainPannel)
        self.testline_23.setGeometry(QtCore.QRect(1140, 280, 3, 81))
        self.testline_23.setMinimumSize(QtCore.QSize(3, 0))
        self.testline_23.setMaximumSize(QtCore.QSize(3, 16777215))
        self.testline_23.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_23.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_23.setStyleSheet("background-color:#fe6f5e;")
        self.testline_23.setFrameShape(QtWidgets.QFrame.VLine)
        self.testline_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_23.setLineWidth(0)
        self.testline_23.setMidLineWidth(0)
        self.testline_23.setObjectName("testline_23")
        self.testline_24 = QtWidgets.QFrame(self.MainPannel)
        self.testline_24.setGeometry(QtCore.QRect(1140, 360, 111, 3))
        self.testline_24.setMaximumSize(QtCore.QSize(16777215, 3))
        self.testline_24.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_24.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_24.setStyleSheet("background-color:#fe6f5e;")
        self.testline_24.setFrameShape(QtWidgets.QFrame.HLine)
        self.testline_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_24.setLineWidth(0)
        self.testline_24.setMidLineWidth(0)
        self.testline_24.setObjectName("testline_24")
        self.testline_25 = QtWidgets.QFrame(self.MainPannel)
        self.testline_25.setGeometry(QtCore.QRect(1250, 290, 3, 301))
        self.testline_25.setMinimumSize(QtCore.QSize(3, 0))
        self.testline_25.setMaximumSize(QtCore.QSize(3, 16777215))
        self.testline_25.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_25.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_25.setStyleSheet("background-color:#fe6f5e;")
        self.testline_25.setFrameShape(QtWidgets.QFrame.VLine)
        self.testline_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_25.setLineWidth(0)
        self.testline_25.setMidLineWidth(0)
        self.testline_25.setObjectName("testline_25")
        self.testline_26 = QtWidgets.QFrame(self.MainPannel)
        self.testline_26.setGeometry(QtCore.QRect(1040, 590, 211, 3))
        self.testline_26.setMaximumSize(QtCore.QSize(16777215, 3))
        self.testline_26.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_26.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_26.setStyleSheet("background-color:#fe6f5e;")
        self.testline_26.setFrameShape(QtWidgets.QFrame.HLine)
        self.testline_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_26.setLineWidth(0)
        self.testline_26.setMidLineWidth(0)
        self.testline_26.setObjectName("testline_26")
        self.testline_27 = QtWidgets.QFrame(self.MainPannel)
        self.testline_27.setGeometry(QtCore.QRect(1250, 290, 161, 3))
        self.testline_27.setMaximumSize(QtCore.QSize(16777215, 3))
        self.testline_27.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_27.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_27.setStyleSheet("background-color:#fe6f5e;")
        self.testline_27.setFrameShape(QtWidgets.QFrame.HLine)
        self.testline_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_27.setLineWidth(0)
        self.testline_27.setMidLineWidth(0)
        self.testline_27.setObjectName("testline_27")
        self.testline_28 = QtWidgets.QFrame(self.MainPannel)
        self.testline_28.setGeometry(QtCore.QRect(1410, 290, 3, 121))
        self.testline_28.setMinimumSize(QtCore.QSize(3, 0))
        self.testline_28.setMaximumSize(QtCore.QSize(3, 16777215))
        self.testline_28.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_28.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_28.setStyleSheet("background-color:#fe6f5e;")
        self.testline_28.setFrameShape(QtWidgets.QFrame.VLine)
        self.testline_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_28.setLineWidth(0)
        self.testline_28.setMidLineWidth(0)
        self.testline_28.setObjectName("testline_28")
        self.testline_29 = QtWidgets.QFrame(self.MainPannel)
        self.testline_29.setGeometry(QtCore.QRect(1410, 410, 381, 3))
        self.testline_29.setMaximumSize(QtCore.QSize(16777215, 3))
        self.testline_29.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_29.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_29.setStyleSheet("background-color:#fe6f5e;")
        self.testline_29.setFrameShape(QtWidgets.QFrame.HLine)
        self.testline_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_29.setLineWidth(0)
        self.testline_29.setMidLineWidth(0)
        self.testline_29.setObjectName("testline_29")
        self.testline_30 = QtWidgets.QFrame(self.MainPannel)
        self.testline_30.setGeometry(QtCore.QRect(1350, 120, 3, 81))
        self.testline_30.setMinimumSize(QtCore.QSize(3, 0))
        self.testline_30.setMaximumSize(QtCore.QSize(3, 16777215))
        self.testline_30.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_30.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_30.setStyleSheet("background-color:#fe6f5e;")
        self.testline_30.setFrameShape(QtWidgets.QFrame.VLine)
        self.testline_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_30.setLineWidth(0)
        self.testline_30.setMidLineWidth(0)
        self.testline_30.setObjectName("testline_30")
        self.testline_31 = QtWidgets.QFrame(self.MainPannel)
        self.testline_31.setGeometry(QtCore.QRect(1350, 120, 221, 3))
        self.testline_31.setMaximumSize(QtCore.QSize(16777215, 3))
        self.testline_31.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_31.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_31.setStyleSheet("background-color:#fe6f5e;")
        self.testline_31.setFrameShape(QtWidgets.QFrame.HLine)
        self.testline_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_31.setLineWidth(0)
        self.testline_31.setMidLineWidth(0)
        self.testline_31.setObjectName("testline_31")
        self.testline_32 = QtWidgets.QFrame(self.MainPannel)
        self.testline_32.setGeometry(QtCore.QRect(1570, 120, 3, 631))
        self.testline_32.setMinimumSize(QtCore.QSize(3, 0))
        self.testline_32.setMaximumSize(QtCore.QSize(3, 16777215))
        self.testline_32.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_32.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_32.setStyleSheet("background-color:#fe6f5e;")
        self.testline_32.setFrameShape(QtWidgets.QFrame.VLine)
        self.testline_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_32.setLineWidth(0)
        self.testline_32.setMidLineWidth(0)
        self.testline_32.setObjectName("testline_32")
        self.testline_33 = QtWidgets.QFrame(self.MainPannel)
        self.testline_33.setGeometry(QtCore.QRect(1790, 410, 3, 261))
        self.testline_33.setMinimumSize(QtCore.QSize(3, 0))
        self.testline_33.setMaximumSize(QtCore.QSize(3, 16777215))
        self.testline_33.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_33.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_33.setStyleSheet("background-color:#fe6f5e;")
        self.testline_33.setFrameShape(QtWidgets.QFrame.VLine)
        self.testline_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_33.setLineWidth(0)
        self.testline_33.setMidLineWidth(0)
        self.testline_33.setObjectName("testline_33")
        self.testline_34 = QtWidgets.QFrame(self.MainPannel)
        self.testline_34.setGeometry(QtCore.QRect(180, 480, 211, 3))
        self.testline_34.setMaximumSize(QtCore.QSize(16777215, 3))
        self.testline_34.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_34.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_34.setStyleSheet("background-color:#fe6f5e;")
        self.testline_34.setFrameShape(QtWidgets.QFrame.HLine)
        self.testline_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_34.setLineWidth(0)
        self.testline_34.setMidLineWidth(0)
        self.testline_34.setObjectName("testline_34")
        self.toolButton_5 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_5.setGeometry(QtCore.QRect(215, 473, 31, 21))
        self.toolButton_5.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_5.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_6 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_6.setGeometry(QtCore.QRect(320, 473, 31, 21))
        self.toolButton_6.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_6.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolButton_7 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_7.setGeometry(QtCore.QRect(433, 103, 31, 21))
        self.toolButton_7.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_7.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_7.setObjectName("toolButton_7")
        self.testline_35 = QtWidgets.QFrame(self.MainPannel)
        self.testline_35.setGeometry(QtCore.QRect(500, 140, 3, 121))
        self.testline_35.setMinimumSize(QtCore.QSize(3, 0))
        self.testline_35.setMaximumSize(QtCore.QSize(3, 16777215))
        self.testline_35.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_35.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_35.setStyleSheet("background-color:#fe6f5e;")
        self.testline_35.setFrameShape(QtWidgets.QFrame.VLine)
        self.testline_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_35.setLineWidth(0)
        self.testline_35.setMidLineWidth(0)
        self.testline_35.setObjectName("testline_35")
        self.toolButton_8 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_8.setGeometry(QtCore.QRect(486, 240, 31, 21))
        self.toolButton_8.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_8.setArrowType(QtCore.Qt.DownArrow)
        self.toolButton_8.setObjectName("toolButton_8")
        self.toolButton_9 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_9.setGeometry(QtCore.QRect(487, 135, 31, 21))
        self.toolButton_9.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_9.setArrowType(QtCore.Qt.UpArrow)
        self.toolButton_9.setObjectName("toolButton_9")
        self.toolButton_10 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_10.setGeometry(QtCore.QRect(432, 272, 31, 21))
        self.toolButton_10.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_10.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_10.setObjectName("toolButton_10")
        self.toolButton_11 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_11.setGeometry(QtCore.QRect(488, 635, 31, 21))
        self.toolButton_11.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_11.setArrowType(QtCore.Qt.DownArrow)
        self.toolButton_11.setObjectName("toolButton_11")
        self.toolButton_12 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_12.setGeometry(QtCore.QRect(542, 462, 31, 21))
        self.toolButton_12.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_12.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_12.setObjectName("toolButton_12")
        self.toolButton_13 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_13.setGeometry(QtCore.QRect(587, 437, 31, 21))
        self.toolButton_13.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_13.setArrowType(QtCore.Qt.DownArrow)
        self.toolButton_13.setObjectName("toolButton_13")
        self.testline_36 = QtWidgets.QFrame(self.MainPannel)
        self.testline_36.setGeometry(QtCore.QRect(600, 680, 331, 3))
        self.testline_36.setMaximumSize(QtCore.QSize(16777215, 3))
        self.testline_36.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_36.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_36.setStyleSheet("background-color:#fe6f5e;")
        self.testline_36.setFrameShape(QtWidgets.QFrame.HLine)
        self.testline_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_36.setLineWidth(0)
        self.testline_36.setMidLineWidth(0)
        self.testline_36.setObjectName("testline_36")
        self.toolButton_14 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_14.setGeometry(QtCore.QRect(647, 672, 31, 21))
        self.toolButton_14.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_14.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_14.setObjectName("toolButton_14")
        self.toolButton_45 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_45.setGeometry(QtCore.QRect(697, 697, 31, 21))
        self.toolButton_45.setStyleSheet("color:#fe6f5e;\n"
                                         "background-color: rgba(0, 0, 0, 0);\n"
                                         "")
        self.toolButton_45.setArrowType(QtCore.Qt.UpArrow)
        self.toolButton_45.setObjectName("toolButton_45")
        self.toolButton_15 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_15.setGeometry(QtCore.QRect(863, 671, 31, 21))
        self.toolButton_15.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_15.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_15.setObjectName("toolButton_15")
        self.toolButton_16 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_16.setGeometry(QtCore.QRect(648, 582, 31, 21))
        self.toolButton_16.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_16.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_16.setObjectName("toolButton_16")
        self.toolButton_17 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_17.setGeometry(QtCore.QRect(758, 583, 31, 21))
        self.toolButton_17.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_17.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_17.setObjectName("toolButton_17")
        self.testline_37 = QtWidgets.QFrame(self.MainPannel)
        self.testline_37.setGeometry(QtCore.QRect(930, 680, 3, 71))
        self.testline_37.setMinimumSize(QtCore.QSize(3, 0))
        self.testline_37.setMaximumSize(QtCore.QSize(3, 16777215))
        self.testline_37.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_37.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_37.setStyleSheet("background-color:#fe6f5e;")
        self.testline_37.setFrameShape(QtWidgets.QFrame.VLine)
        self.testline_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_37.setLineWidth(0)
        self.testline_37.setMidLineWidth(0)
        self.testline_37.setObjectName("testline_37")
        self.testline_38 = QtWidgets.QFrame(self.MainPannel)
        self.testline_38.setGeometry(QtCore.QRect(930, 750, 641, 3))
        self.testline_38.setMaximumSize(QtCore.QSize(16777215, 3))
        self.testline_38.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_38.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_38.setStyleSheet("background-color:#fe6f5e;")
        self.testline_38.setFrameShape(QtWidgets.QFrame.HLine)
        self.testline_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_38.setLineWidth(0)
        self.testline_38.setMidLineWidth(0)
        self.testline_38.setObjectName("testline_38")
        self.toolButton_18 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_18.setGeometry(QtCore.QRect(970, 742, 31, 21))
        self.toolButton_18.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_18.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_18.setObjectName("toolButton_18")
        self.toolButton_19 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_19.setGeometry(QtCore.QRect(808, 555, 31, 21))
        self.toolButton_19.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_19.setArrowType(QtCore.Qt.DownArrow)
        self.toolButton_19.setObjectName("toolButton_19")
        self.toolButton_20 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_20.setGeometry(QtCore.QRect(1027, 555, 31, 21))
        self.toolButton_20.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_20.setArrowType(QtCore.Qt.DownArrow)
        self.toolButton_20.setObjectName("toolButton_20")
        self.toolButton_21 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_21.setGeometry(QtCore.QRect(970, 350, 31, 21))
        self.toolButton_21.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_21.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_21.setObjectName("toolButton_21")
        self.toolButton_22 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_22.setGeometry(QtCore.QRect(697, 385, 31, 21))
        self.toolButton_22.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_22.setArrowType(QtCore.Qt.UpArrow)
        self.toolButton_22.setObjectName("toolButton_22")
        self.toolButton_23 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_23.setGeometry(QtCore.QRect(1078, 192, 31, 21))
        self.toolButton_23.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_23.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_23.setObjectName("toolButton_23")
        self.toolButton_24 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_24.setGeometry(QtCore.QRect(1290, 192, 31, 21))
        self.toolButton_24.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_24.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_24.setObjectName("toolButton_24")
        self.toolButton_25 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_25.setGeometry(QtCore.QRect(1080, 272, 31, 21))
        self.toolButton_25.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_25.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_25.setObjectName("toolButton_25")
        self.toolButton_26 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_26.setGeometry(QtCore.QRect(1184, 352, 31, 21))
        self.toolButton_26.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_26.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_26.setObjectName("toolButton_26")
        self.toolButton_27 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_27.setGeometry(QtCore.QRect(1237, 307, 31, 21))
        self.toolButton_27.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_27.setArrowType(QtCore.Qt.UpArrow)
        self.toolButton_27.setObjectName("toolButton_27")
        self.toolButton_28 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_28.setGeometry(QtCore.QRect(1237, 387, 31, 21))
        self.toolButton_28.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_28.setArrowType(QtCore.Qt.UpArrow)
        self.toolButton_28.setObjectName("toolButton_28")
        self.toolButton_29 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_29.setGeometry(QtCore.QRect(1400, 112, 31, 21))
        self.toolButton_29.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_29.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_29.setObjectName("toolButton_29")
        self.toolButton_30 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_30.setGeometry(QtCore.QRect(1510, 402, 31, 21))
        self.toolButton_30.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_30.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_30.setObjectName("toolButton_30")
        self.toolButton_31 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_31.setGeometry(QtCore.QRect(1617, 402, 31, 21))
        self.toolButton_31.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_31.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_31.setObjectName("toolButton_31")
        self.toolButton_32 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_32.setGeometry(QtCore.QRect(1722, 402, 31, 21))
        self.toolButton_32.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_32.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_32.setObjectName("toolButton_32")
        self.toolButton_33 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_33.setGeometry(QtCore.QRect(1558, 430, 31, 21))
        self.toolButton_33.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_33.setArrowType(QtCore.Qt.UpArrow)
        self.toolButton_33.setObjectName("toolButton_33")
        self.toolButton_34 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_34.setGeometry(QtCore.QRect(1557, 370, 31, 21))
        self.toolButton_34.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_34.setArrowType(QtCore.Qt.DownArrow)
        self.toolButton_34.setObjectName("toolButton_34")
        self.testline_39 = QtWidgets.QFrame(self.MainPannel)
        self.testline_39.setGeometry(QtCore.QRect(1790, 590, 101, 3))
        self.testline_39.setMaximumSize(QtCore.QSize(16777215, 3))
        self.testline_39.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_39.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_39.setStyleSheet("background-color:#fe6f5e;")
        self.testline_39.setFrameShape(QtWidgets.QFrame.HLine)
        self.testline_39.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_39.setLineWidth(0)
        self.testline_39.setMidLineWidth(0)
        self.testline_39.setObjectName("testline_39")
        self.testline_40 = QtWidgets.QFrame(self.MainPannel)
        self.testline_40.setGeometry(QtCore.QRect(1790, 670, 161, 3))
        self.testline_40.setMaximumSize(QtCore.QSize(16777215, 3))
        self.testline_40.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_40.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_40.setStyleSheet("background-color:#fe6f5e;")
        self.testline_40.setFrameShape(QtWidgets.QFrame.HLine)
        self.testline_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_40.setLineWidth(0)
        self.testline_40.setMidLineWidth(0)
        self.testline_40.setObjectName("testline_40")
        self.testline_41 = QtWidgets.QFrame(self.MainPannel)
        self.testline_41.setGeometry(QtCore.QRect(1950, 450, 3, 221))
        self.testline_41.setMinimumSize(QtCore.QSize(3, 0))
        self.testline_41.setMaximumSize(QtCore.QSize(3, 16777215))
        self.testline_41.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_41.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_41.setStyleSheet("background-color:#fe6f5e;")
        self.testline_41.setFrameShape(QtWidgets.QFrame.VLine)
        self.testline_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_41.setLineWidth(0)
        self.testline_41.setMidLineWidth(0)
        self.testline_41.setObjectName("testline_41")
        self.toolButton_35 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_35.setGeometry(QtCore.QRect(1940, 440, 31, 21))
        self.toolButton_35.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_35.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_35.setObjectName("toolButton_35")
        self.toolButton_36 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_36.setGeometry(QtCore.QRect(1830, 580, 31, 21))
        self.toolButton_36.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_36.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_36.setObjectName("toolButton_36")
        self.toolButton_37 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_37.setGeometry(QtCore.QRect(1830, 660, 31, 21))
        self.toolButton_37.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_37.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_37.setObjectName("toolButton_37")
        self.testline_42 = QtWidgets.QFrame(self.MainPannel)
        self.testline_42.setGeometry(QtCore.QRect(1890, 390, 3, 201))
        self.testline_42.setMinimumSize(QtCore.QSize(3, 0))
        self.testline_42.setMaximumSize(QtCore.QSize(3, 16777215))
        self.testline_42.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_42.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_42.setStyleSheet("background-color:#fe6f5e;")
        self.testline_42.setFrameShape(QtWidgets.QFrame.VLine)
        self.testline_42.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_42.setLineWidth(0)
        self.testline_42.setMidLineWidth(0)
        self.testline_42.setObjectName("testline_42")
        self.testline_43 = QtWidgets.QFrame(self.MainPannel)
        self.testline_43.setGeometry(QtCore.QRect(1890, 390, 111, 3))
        self.testline_43.setMaximumSize(QtCore.QSize(16777215, 3))
        self.testline_43.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_43.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_43.setStyleSheet("background-color:#fe6f5e;")
        self.testline_43.setFrameShape(QtWidgets.QFrame.HLine)
        self.testline_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_43.setLineWidth(0)
        self.testline_43.setMidLineWidth(0)
        self.testline_43.setObjectName("testline_43")
        self.testline_44 = QtWidgets.QFrame(self.MainPannel)
        self.testline_44.setGeometry(QtCore.QRect(2000, 390, 3, 351))
        self.testline_44.setMinimumSize(QtCore.QSize(3, 0))
        self.testline_44.setMaximumSize(QtCore.QSize(3, 16777215))
        self.testline_44.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_44.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_44.setStyleSheet("background-color:#fe6f5e;")
        self.testline_44.setFrameShape(QtWidgets.QFrame.VLine)
        self.testline_44.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_44.setLineWidth(0)
        self.testline_44.setMidLineWidth(0)
        self.testline_44.setObjectName("testline_44")
        self.toolButton_38 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_38.setGeometry(QtCore.QRect(1987, 700, 31, 21))
        self.toolButton_38.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_38.setArrowType(QtCore.Qt.DownArrow)
        self.toolButton_38.setObjectName("toolButton_38")
        self.toolButton_39 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_39.setGeometry(QtCore.QRect(1987, 405, 31, 21))
        self.toolButton_39.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_39.setArrowType(QtCore.Qt.DownArrow)
        self.toolButton_39.setObjectName("toolButton_39")
        self.toolButton_40 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_40.setGeometry(QtCore.QRect(1987, 465, 31, 21))
        self.toolButton_40.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_40.setArrowType(QtCore.Qt.DownArrow)
        self.toolButton_40.setObjectName("toolButton_40")
        self.testline_45 = QtWidgets.QFrame(self.MainPannel)
        self.testline_45.setGeometry(QtCore.QRect(2000, 740, 111, 3))
        self.testline_45.setMaximumSize(QtCore.QSize(16777215, 3))
        self.testline_45.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_45.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_45.setStyleSheet("background-color:#fe6f5e;")
        self.testline_45.setFrameShape(QtWidgets.QFrame.HLine)
        self.testline_45.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_45.setLineWidth(0)
        self.testline_45.setMidLineWidth(0)
        self.testline_45.setObjectName("testline_45")
        self.testline_46 = QtWidgets.QFrame(self.MainPannel)
        self.testline_46.setGeometry(QtCore.QRect(2110, 450, 3, 291))
        self.testline_46.setMinimumSize(QtCore.QSize(3, 0))
        self.testline_46.setMaximumSize(QtCore.QSize(3, 16777215))
        self.testline_46.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_46.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_46.setStyleSheet("background-color:#fe6f5e;")
        self.testline_46.setFrameShape(QtWidgets.QFrame.VLine)
        self.testline_46.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_46.setLineWidth(0)
        self.testline_46.setMidLineWidth(0)
        self.testline_46.setObjectName("testline_46")
        self.toolButton_41 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_41.setGeometry(QtCore.QRect(2096, 525, 31, 21))
        self.toolButton_41.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_41.setArrowType(QtCore.Qt.UpArrow)
        self.toolButton_41.setObjectName("toolButton_41")
        self.toolButton_42 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_42.setGeometry(QtCore.QRect(2096, 465, 31, 21))
        self.toolButton_42.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_42.setArrowType(QtCore.Qt.UpArrow)
        self.toolButton_42.setObjectName("toolButton_42")
        self.testline_47 = QtWidgets.QFrame(self.MainPannel)
        self.testline_47.setGeometry(QtCore.QRect(2110, 450, 101, 3))
        self.testline_47.setMaximumSize(QtCore.QSize(16777215, 3))
        self.testline_47.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_47.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_47.setStyleSheet("background-color:#fe6f5e;")
        self.testline_47.setFrameShape(QtWidgets.QFrame.HLine)
        self.testline_47.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_47.setLineWidth(0)
        self.testline_47.setMidLineWidth(0)
        self.testline_47.setObjectName("testline_47")
        self.toolButton_43 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_43.setGeometry(QtCore.QRect(2150, 443, 31, 21))
        self.toolButton_43.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_43.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_43.setObjectName("toolButton_43")
        self.testline_48 = QtWidgets.QFrame(self.MainPannel)
        self.testline_48.setGeometry(QtCore.QRect(2210, 360, 3, 91))
        self.testline_48.setMinimumSize(QtCore.QSize(3, 0))
        self.testline_48.setMaximumSize(QtCore.QSize(3, 16777215))
        self.testline_48.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_48.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_48.setStyleSheet("background-color:#fe6f5e;")
        self.testline_48.setFrameShape(QtWidgets.QFrame.VLine)
        self.testline_48.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_48.setLineWidth(0)
        self.testline_48.setMidLineWidth(0)
        self.testline_48.setObjectName("testline_48")
        self.testline_49 = QtWidgets.QFrame(self.MainPannel)
        self.testline_49.setGeometry(QtCore.QRect(2210, 360, 101, 3))
        self.testline_49.setMaximumSize(QtCore.QSize(16777215, 3))
        self.testline_49.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_49.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_49.setStyleSheet("background-color:#fe6f5e;")
        self.testline_49.setFrameShape(QtWidgets.QFrame.HLine)
        self.testline_49.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_49.setLineWidth(0)
        self.testline_49.setMidLineWidth(0)
        self.testline_49.setObjectName("testline_49")
        self.testline_50 = QtWidgets.QFrame(self.MainPannel)
        self.testline_50.setGeometry(QtCore.QRect(2310, 360, 3, 51))
        self.testline_50.setMinimumSize(QtCore.QSize(3, 0))
        self.testline_50.setMaximumSize(QtCore.QSize(3, 16777215))
        self.testline_50.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_50.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_50.setStyleSheet("background-color:#fe6f5e;")
        self.testline_50.setFrameShape(QtWidgets.QFrame.VLine)
        self.testline_50.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_50.setLineWidth(0)
        self.testline_50.setMidLineWidth(0)
        self.testline_50.setObjectName("testline_50")
        self.toolButton_44 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_44.setGeometry(QtCore.QRect(2297, 370, 31, 21))
        self.toolButton_44.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_44.setArrowType(QtCore.Qt.DownArrow)
        self.toolButton_44.setObjectName("toolButton_44")
        self.testline_51 = QtWidgets.QFrame(self.MainPannel)
        self.testline_51.setGeometry(QtCore.QRect(2310, 410, 541, 3))
        self.testline_51.setMaximumSize(QtCore.QSize(16777215, 3))
        self.testline_51.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testline_51.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.testline_51.setStyleSheet("background-color:#fe6f5e;")
        self.testline_51.setFrameShape(QtWidgets.QFrame.HLine)
        self.testline_51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testline_51.setLineWidth(0)
        self.testline_51.setMidLineWidth(0)
        self.testline_51.setObjectName("testline_51")
        self.label_36 = QtWidgets.QLabel(self.MainPannel)
        self.label_36.setGeometry(QtCore.QRect(2125, 480, 28, 28))
        self.label_36.setMinimumSize(QtCore.QSize(0, 0))
        self.label_36.setText("")
        self.label_36.setPixmap(QtGui.QPixmap(image))
        self.label_36.setScaledContents(True)
        self.label_36.setObjectName("label_36")
        self.toolButton_46 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_46.setGeometry(QtCore.QRect(2360, 402, 31, 21))
        self.toolButton_46.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_46.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_46.setObjectName("toolButton_46")
        self.toolButton_47 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_47.setGeometry(QtCore.QRect(2461, 402, 31, 21))
        self.toolButton_47.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_47.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_47.setObjectName("toolButton_47")
        self.toolButton_48 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_48.setGeometry(QtCore.QRect(2570, 402, 31, 21))
        self.toolButton_48.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_48.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_48.setObjectName("toolButton_48")
        self.toolButton_49 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_49.setGeometry(QtCore.QRect(2677, 402, 31, 21))
        self.toolButton_49.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_49.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_49.setObjectName("toolButton_49")
        self.toolButton_50 = QtWidgets.QToolButton(self.MainPannel)
        self.toolButton_50.setGeometry(QtCore.QRect(2788, 402, 31, 21))
        self.toolButton_50.setStyleSheet("color:#fe6f5e;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.toolButton_50.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_50.setObjectName("toolButton_50")
        self.testline_51.raise_()
        self.testline_50.raise_()
        self.testline_52.raise_()
        self.testline_54.raise_()
        self.testline_48.raise_()
        self.testline_47.raise_()
        self.testline_46.raise_()
        self.testline_45.raise_()
        self.testline_44.raise_()
        self.testline_42.raise_()
        self.testline_40.raise_()
        self.testline_39.raise_()
        self.testline_33.raise_()
        self.testline_29.raise_()
        self.testline_32.raise_()
        self.testline_31.raise_()
        self.testline_30.raise_()
        self.testline_23.raise_()
        self.testline_22.raise_()
        self.testline_27.raise_()
        self.testline_25.raise_()
        self.testline_24.raise_()
        self.testline_8.raise_()
        self.testline_26.raise_()
        self.testline_15.raise_()
        self.testline_20.raise_()
        self.testline_21.raise_()
        self.testline_17.raise_()
        self.testline_38.raise_()
        self.testline_37.raise_()
        self.testline_18.raise_()
        self.testline_36.raise_()
        self.testline_12.raise_()
        self.testline_4.raise_()
        self.testline_14.raise_()
        self.testline_7.raise_()
        self.testline_35.raise_()
        self.testline_11.raise_()
        self.testline_9.raise_()
        self.testline_5.raise_()
        self.testline_34.raise_()
        self.DottedLine1_8.raise_()
        self.DottedLine1_5.raise_()
        self.DottedLine1_6.raise_()
        self.DottedLine1.raise_()
        self.DottedLine1_4.raise_()
        self.DottedLine1_7.raise_()
        self.horizontalLayoutWidget.raise_()
        self.DottedLine1_3.raise_()
        self.DottedLine1_2.raise_()
        self.V1.raise_()
        self.V2.raise_()
        self.V4.raise_()
        self.V9.raise_()
        self.V5.raise_()
        self.V10.raise_()
        self.V11.raise_()
        self.V12.raise_()
        self.V6.raise_()
        self.V7.raise_()
        self.V8.raise_()
        self.V3.raise_()
        self.V12_2.raise_()
        self.V12_3.raise_()
        self.V12_4.raise_()
        self.V12_5.raise_()
        self.V12_6.raise_()
        self.V12_7.raise_()
        self.V12_8.raise_()
        self.V12_9.raise_()
        self.V12_10.raise_()
        self.V12_11.raise_()
        self.V12_12.raise_()
        self.V12_13.raise_()
        self.DottedLine1_9.raise_()
        self.INO.raise_()
        self.INI.raise_()
        self.PFP.raise_()
        self.FWT.raise_()
        self.EWC.raise_()
        self.EWC1.raise_()
        self.EXE.raise_()
        self.INS.raise_()
        self.CPI.raise_()
        self.FIF.raise_()
        self.UNE.raise_()
        self.SBD.raise_()
        self.UWC.raise_()
        self.FIE.raise_()
        self.FIW.raise_()
        self.FCE.raise_()
        self.SIW.raise_()
        self.SIE.raise_()
        self.SCE.raise_()
        self.CWC.raise_()
        self.COT.raise_()
        self.HPT.raise_()
        self.REC.raise_()
        self.ITN.raise_()
        self.UND.raise_()
        self.TUK.raise_()
        self.WEG.raise_()
        self.WCT.raise_()
        self.GAU.raise_()
        self.PPR.raise_()
        self.SWT.raise_()
        self.CUP.raise_()
        self.CUR.raise_()
        self.SCS.raise_()
        self.DCS.raise_()
        self.PSI.raise_()
        self.DEL.raise_()
        self.label_34.raise_()
        self.label_42.raise_()
        self.label_43.raise_()
        self.label_44.raise_()
        self.label_35.raise_()
        self.label_37.raise_()
        self.label_38.raise_()
        self.label_39.raise_()
        self.widget.raise_()
        self.testline_10.raise_()
        self.testline_13.raise_()
        self.testline_16.raise_()
        self.testline_19.raise_()
        self.testline_28.raise_()
        self.toolButton_6.raise_()
        self.toolButton_5.raise_()
        self.toolButton_7.raise_()
        self.toolButton_8.raise_()
        self.toolButton_9.raise_()
        self.toolButton_10.raise_()
        self.toolButton_11.raise_()
        self.toolButton_12.raise_()
        self.toolButton_13.raise_()
        self.toolButton_14.raise_()
        self.toolButton_15.raise_()
        self.toolButton_16.raise_()
        self.toolButton_17.raise_()
        self.toolButton_18.raise_()
        self.toolButton_19.raise_()
        self.toolButton_20.raise_()
        self.toolButton_21.raise_()
        self.toolButton_22.raise_()
        self.HE1.raise_()
        self.toolButton_23.raise_()
        self.toolButton_24.raise_()
        self.toolButton_25.raise_()
        self.toolButton_26.raise_()
        self.toolButton_27.raise_()
        self.toolButton_28.raise_()
        self.toolButton_29.raise_()
        self.toolButton_30.raise_()
        self.toolButton_31.raise_()
        self.toolButton_32.raise_()
        self.toolButton_33.raise_()
        self.toolButton_34.raise_()
        self.testline_41.raise_()
        self.toolButton_35.raise_()
        self.toolButton_36.raise_()
        self.toolButton_37.raise_()
        self.testline_43.raise_()
        self.toolButton_38.raise_()
        self.toolButton_39.raise_()
        self.toolButton_40.raise_()
        self.toolButton_41.raise_()
        self.toolButton_42.raise_()
        self.toolButton_43.raise_()
        self.testline_49.raise_()
        self.toolButton_44.raise_()
        self.label_36.raise_()
        self.toolButton_45.raise_()
        self.toolButton_46.raise_()
        self.toolButton_47.raise_()
        self.toolButton_48.raise_()
        self.toolButton_49.raise_()
        self.toolButton_50.raise_()
        self.verticalLayout_2.addWidget(self.MainPannel)
        self.ScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.ScrollArea)
        Main.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)



    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", f"Chicago CTA7000 {car_num}"))
        self.Label1.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">卸车</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Unloading</span></p></body></html>"))
        self.label_26.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">内装拆卸</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Furnish Removal</span></p></body></html>"))
        self.label_24.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">接车检查</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Incoming Insp</span></p></body></html>"))
        self.label_23.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">外设</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Ext. Equipment</span></p></body></html>"))
        self.label_21.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">一次淋雨</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">1st Water Test</span></p></body></html>"))
        self.label_22.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">防寒</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Insulation</span></p></body></html>"))
        self.label_20.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">侧墙</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Side Wall</span></p></body></html>"))
        self.label_17.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">客设1</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Int Equipment 1</span></p></body></html>"))
        self.label_16.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">客设2</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Int Equipment 2</span></p></body></html>"))
        self.label_19.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">客设3</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Int Equipment 3</span></p></body></html>"))
        self.label_15.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">客室接线1</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Saloon Wire Con1</span></p></body></html>"))
        self.label_18.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">客室接线2</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Saloon Wire Con2</span></p></body></html>"))
        self.label_14.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">司机室接线4</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Cab Wire Conn 4</span></p></body></html>"))
        self.label_13.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">校线</span></p><p align=\"center\"><span style=\" font-size:9pt;\">Continuity Test</span></p></body></html>"))
        self.label_12.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">耐压</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Hi-pot Test</span></p></body></html>"))
        self.label_11.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">耐压后恢复</span></p><p align=\"center\">Recovery After Hipot</p></body></html>"))
        self.label_10.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">细检</span></p><p align=\"center\"><span style=\" font-size:9pt;\">Detail Inspection</span></p></body></html>"))
        self.label_28.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">落车</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Trucking</span></p></body></html>"))
        self.label_29.setText(_translate("Main", "<html><head/><body><table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\"><tr><td width=\"200\"><p align=\"center\"><span style=\" font-size:9pt;\">二次淋雨<br/>2nd Water Test</span></p></td></tr></table></body></html>"))
        self.label_31.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">编组</span></p><p align=\"center\"><span style=\" font-size:9pt;\">Coupling</span></p></body></html>"))
        self.label_27.setText(_translate("Main", "<html><head/><body><table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\"><tr><td width=\"200\"><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">静调<br/>Static Test</span></p></td></tr></table></body></html>"))
        self.label_25.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">动调</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Dynamic Test</span></p></body></html>"))
        self.label_32.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">最终交检</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">PSI</span></p></body></html>"))
        self.label_30.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">发运前检查</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Loading Insp</span></p></body></html>"))
        self.INO.setText(_translate("Main", "IN0\n"
"入库检查"))
        self.INI.setText(_translate("Main", "INI\n"
"接车检查"))
        self.PFP.setText(_translate("Main", "PFP\n"
"管路清洗保压"))
        self.FWT.setText(_translate("Main", "1WT\n"
"一次淋雨实验"))
        self.EWC.setText(_translate("Main", "EWC\n"
"车外接线"))
        self.EWC1.setText(_translate("Main", "EWC\n"
"车外接线"))
        self.EXE.setText(_translate("Main", "EXE\n"
"外部设备"))
        self.HE1.setText(_translate("Main", "HE1\n"
"电加热1"))
        self.INS.setText(_translate("Main", "INS\n"
"防寒"))
        self.CPI.setText(_translate("Main", "CPI\n"
"车钩安装"))
        self.FIF.setText(_translate("Main", "1IF\n"
"内装一次交检"))
        self.UNE.setText(_translate("Main", "UNE\n"
"车下设备"))
        self.SBD.setText(_translate("Main", "SBD\n"
"踢脚板"))
        self.UWC.setText(_translate("Main", "UWC\n"
"车下接线"))
        self.FIE.setText(_translate("Main", "1IE\n"
"车内设备一次交检"))
        self.FIW.setText(_translate("Main", "1IW\n"
"室内一次接线"))
        self.FCE.setText(_translate("Main", "1CE\n"
"一次司机室设备"))
        self.SIW.setText(_translate("Main", "2IW\n"
"室内二次接线"))
        self.SIE.setText(_translate("Main", "2IE\n"
"车内设备二次交检"))
        self.SCE.setText(_translate("Main", "2CE\n"
"二次司机室设备"))
        self.CWC.setText(_translate("Main", "CWC\n"
"司机室接线"))
        self.COT.setText(_translate("Main", "COT\n"
"校线"))
        self.HPT.setText(_translate("Main", "HPT\n"
"绝缘耐压"))
        self.REC.setText(_translate("Main", "REC\n"
"耐压后接线恢复"))
        self.ITN.setText(_translate("Main", "ITN\n"
"车内细检"))
        self.UND.setText(_translate("Main", "UND\n"
"车下细检"))
        self.TUK.setText(_translate("Main", "TUK\n"
"落车"))
        self.WEG.setText(_translate("Main", "WEG\n"
"称重"))
        self.WCT.setText(_translate("Main", "WCT\n"
"落车后转向架接线"))
        self.GAU.setText(_translate("Main", "GAU\n"
"界限"))
        self.PPR.setText(_translate("Main", "PPR\n"
"管路注油排气"))
        self.SWT.setText(_translate("Main", "2WT\n"
"二次淋雨"))
        self.CUP.setText(_translate("Main", "CUP\n"
"编组"))
        self.CUR.setText(_translate("Main", "CUR\n"
"小曲线实验"))
        self.SCS.setText(_translate("Main", "SCS\n"
"静态调试"))
        self.DCS.setText(_translate("Main", "DCS\n"
"动态调试"))
        self.PSI.setText(_translate("Main", "PSI\n"
"最终检查"))
        self.DEL.setText(_translate("Main", "DEL\n"
"包装发运"))
        self.label_61.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">流程</span></p><p align=\"center\"><span style=\" font-weight:600;\">Major Process</span></p></body></html>"))
        self.label_62.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">司机室电气</span></p><p align=\"center\"><span style=\" font-weight:600;\">Cab Electrical</span></p></body></html>"))
        self.label_63.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">司机室</span></p><p align=\"center\"><span style=\" font-weight:600;\">Cab</span></p></body></html>"))
        self.label_64.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">车内电气</span></p><p align=\"center\"><span style=\" font-weight:600;\">Interior Electrical</span></p></body></html>"))
        self.label_65.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">内设</span></p><p align=\"center\"><span style=\" font-weight:600;\">Interior Equipment</span></p></body></html>"))
        self.label_66.setText(_translate("Main", "<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">落车试验</span></p><p align=\"center\"><span style=\" font-weight:600;\">Trucking </span></p><p align=\"center\"><br/></p></body></html>"))
        self.label_67.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">内装</span></p><p align=\"center\"><span style=\" font-weight:600;\">Interior Furnishing</span></p></body></html>"))
        self.label_68.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">车外</span></p><p align=\"center\"><span style=\" font-weight:600;\">Exterior Equipment</span></p></body></html>"))
        self.label.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">车下电气</span></p><p align=\"center\"><span style=\" font-weight:600;\">Exterior Electrical</span></p></body></html>"))
        self.toolButton_5.setText(_translate("Main", "..."))
        self.toolButton_6.setText(_translate("Main", "..."))
        self.toolButton_7.setText(_translate("Main", "..."))
        self.toolButton_8.setText(_translate("Main", "..."))
        self.toolButton_9.setText(_translate("Main", "..."))
        self.toolButton_10.setText(_translate("Main", "..."))
        self.toolButton_11.setText(_translate("Main", "..."))
        self.toolButton_12.setText(_translate("Main", "..."))
        self.toolButton_13.setText(_translate("Main", "..."))
        self.toolButton_14.setText(_translate("Main", "..."))
        self.toolButton_15.setText(_translate("Main", "..."))
        self.toolButton_16.setText(_translate("Main", "..."))
        self.toolButton_17.setText(_translate("Main", "..."))
        self.toolButton_18.setText(_translate("Main", "..."))
        self.toolButton_19.setText(_translate("Main", "..."))
        self.toolButton_20.setText(_translate("Main", "..."))
        self.toolButton_21.setText(_translate("Main", "..."))
        self.toolButton_22.setText(_translate("Main", "..."))
        self.toolButton_23.setText(_translate("Main", "..."))
        self.toolButton_24.setText(_translate("Main", "..."))
        self.toolButton_25.setText(_translate("Main", "..."))
        self.toolButton_26.setText(_translate("Main", "..."))
        self.toolButton_27.setText(_translate("Main", "..."))
        self.toolButton_28.setText(_translate("Main", "..."))
        self.toolButton_29.setText(_translate("Main", "..."))
        self.toolButton_30.setText(_translate("Main", "..."))
        self.toolButton_31.setText(_translate("Main", "..."))
        self.toolButton_32.setText(_translate("Main", "..."))
        self.toolButton_33.setText(_translate("Main", "..."))
        self.toolButton_34.setText(_translate("Main", "..."))
        self.toolButton_35.setText(_translate("Main", "..."))
        self.toolButton_36.setText(_translate("Main", "..."))
        self.toolButton_37.setText(_translate("Main", "..."))
        self.toolButton_38.setText(_translate("Main", "..."))
        self.toolButton_39.setText(_translate("Main", "..."))
        self.toolButton_40.setText(_translate("Main", "..."))
        self.toolButton_41.setText(_translate("Main", "..."))
        self.toolButton_42.setText(_translate("Main", "..."))
        self.toolButton_43.setText(_translate("Main", "..."))
        self.toolButton_44.setText(_translate("Main", "..."))
        # self.toolButton_45.setText(_translate("Main", "..."))
        self.toolButton_46.setText(_translate("Main", "..."))
        self.toolButton_47.setText(_translate("Main", "..."))
        self.toolButton_48.setText(_translate("Main", "..."))
        self.toolButton_49.setText(_translate("Main", "..."))
        self.toolButton_50.setText(_translate("Main", "..."))
        self.toolButton_45.setText(_translate("Main", "..."))


        self.cist = [self.INO, self.INI, self.PFP, self.EXE, self.EWC, self.EWC1, self.FWT, self.INS, self.FIF, self.SBD, self.HE1,
                     self.FIE, self.SIE, self.FIW, self.SIW, self.FCE, self.SCE, self.CPI, self.UNE, self.UWC, self.CWC,
                     self.COT, self.HPT, self.REC, self.UND, self.ITN, self.TUK, self.WEG, self.WCT, self.GAU, self.SWT,
                     self.PPR, self.CUP, self.CUR, self.SCS, self.DCS, self.PSI, self.DEL]


class InspOverview():
    #
    # def __init__(self):
    #     self.signal = InspOverviewSignal()
    #     self.signal.insp_overview_requested.connect(self.main)

    def main(self, carNum, Insp):

        # The rest of the method remains unchanged
        # print(carNum, Insp, "CarNum, INSP")
        insp = carNum.upper() + Insp.upper()

        exr, er, rrn = [], [], []
        exrS, erS = [], []
        ppi = ""

        '''get current rrn, exr, er, ppi status'''


        print("current insp is ", insp)
        cur.execute(f"""Select RRN, EXR, ER, PPI from CarInsp where Car_INSP_Point = '{insp}'""")
        # cur.execute(f"""Select RRN, EXR, ER, PPI from CarInsp where Car_INSP_Point = '7090IN0'""")

        inspDetail = cur.fetchone()
        print(inspDetail)
        if inspDetail:
            # print("!!!!!!!!!!!1", inspDetail)
                # '''rrn portion'''
            if inspDetail[0]:
                try:
                    rrn = inspDetail[0].split(",")
                except AttributeError:
                    rrn = rrn.append(inspDetail[0])
                    print("Only one rrn available")
                else:
                    print("rrn successfully extracted")

                #exr portion
            if inspDetail[1]:
                # print(inspDetail)
                try:
                    exr = inspDetail[1].split(",")
                    print(exr)
                except AttributeError:
                    exr = rrn.append(inspDetail[1])
                    print("Only one exr available")
                else:
                    print("exr successfully extracted")

                for i in exr:
                    cur.execute(f"""Select EXR_Status from EXR where EXR_Num = '{i.strip()}'""")

                    status = cur.fetchone()
                    # print("current status for this exr is", status)
                    try:
                        # print(f"trying for exr, {i}")
                        exrS.append(status[0])
                    except:
                        print("exception for exr", i, status)
                        exrS.append("Open")
                #er portion
            if inspDetail[2]:
                print(inspDetail[2])
                try:
                    er = inspDetail[2].split(",")
                    print("check12")
                except AttributeError:
                    er.append(inspDetail[2])
                    print("Only one er available")
                else:
                    print("er successfully extracted")

                for i in er:
                    cur.execute(f"""Select ER_Status from ER where ER_Num = '{i.strip()}'""")
                    status = cur.fetchone()
                    try:
                        erS.append(status[0])
                    except:
                        erS.append("Open")
            if inspDetail[3]:
                ppi = inspDetail[3]
            else:
                ppi = None

            #jump to memory block 3

            # print(er)
            # print(erS)
            # print(exr)
            # print(exrS)
        else:
            messagebox.showerror(title=f"Inspection point: {carNum} {Insp}", message=f"Car_INSP_Point is not allocated yet.")
            return False

        # app = QApplication([])
        # window = QWidget()
        window = QDialog()
        window.setWindowTitle(f"{carNum} {Insp} Overview")

        # Create a QGridLayout with two columns
        layout = QGridLayout(window)
        layout.setColumnStretch(1, 1)

        # Create labels and text for the first column
        rrn_label = QLabel("RRN:", window)
        exr_label = QLabel("EXR Stop Point:", window)
        er_label = QLabel("ER Stop Point:", window)
        ppi_label = QLabel("PPI:", window)
        rrn_text = QLabel("", window)

        #get the recent path location of those rrns
        for x in rrn:
            current = rrn_text.text()
            try:
                path = SearchFile.Search.searchRRN(x, carNum, Insp)

                if path is None:
                    rrn_text.setText(current + f"{x}\t")
                else:
                    rrn_text.setText(current + f"<a href='file:///{path}'>{x}</a>\t")

            except Exception as e:
                    print(f"An exception occurred: {e}")
                    rrn_text.setText(current + f"{x}\t")

        rrn_text.setOpenExternalLinks(True)
        rrn_text.setTextFormat(Qt.RichText)


        '''exr text if closed, then strike out'''
        exr_text = QLabel(window)
        exr_text.setText("")
        for y, z in zip(exr, exrS):
            current = exr_text.text()
            try:
                path = SearchFile.Search.searchEXR(y, carNum, Insp)
                if z.upper() == "CLOSED":
                    print(path)
                    # exr_text.setText(current + f"<a href='file:///{path}'><strike>{y}</strike></a>\t")
                    exr_text.setText(current + f"<a href='file:///{path}'><s>{y}</s></a>\t")

                elif z.upper() == "OPEN":
                    print("check3")
                    print(path)
                    print(type(path))
                    # exr_text.setText(current + f"<a href='file:///{path}'>{y}</a>\t")
                    if path is None:
                        exr_text.setText(current + f"{y}\t")
                    else:
                        exr_text.setText(current + f"<a href='file:///{path}'>{y}</a>\t")

            except Exception as e:
                if z is None:
                    messagebox.showinfo(message=f"no information about {z} in EXR Database")
                    return False
                elif z.upper() == "CLOSED":
                    exr_text.setText(current + f"<strike>{y}</strike>\t")
                elif z.upper == "OPEN":
                    exr_text.setText(current + f"{y}\t")


        exr_text.setTextFormat(Qt.RichText)
        exr_text.setOpenExternalLinks(True)

        # Create a label for the ER Stop Point with a hyperlink for "56.78"
        er_text = QLabel(window)
        er_text.setText("")
        for y, z in zip(er, erS):
            current = er_text.text()
            try:
                path = SearchFile.Search.searchER(y, carNum, Insp)
                if z.upper() == "CLOSED":
                    er_text.setText(current + f"<a href='file:///{path}'><strike>{y}</strike></a>\t")
                elif z.upper() == "OPEN":
                    er_text.setText(current + f"<a href='file:///{path}'>{y}</a>\t")

            except Exception as e:
                if z is None:
                    messagebox.showinfo(message=f"no information about {z} in ER Database")
                    return False
                elif z.upper() == "CLOSED":
                    er_text.setText(current + f"<strike>{y}</strike>\t")
                elif z.upper() == "OPEN":
                    er_text.setText(current + f"{y}\t")
        er_text.setTextFormat(Qt.RichText)
        er_text.setOpenExternalLinks(True)



        ppi_text = QLabel(window)
        if ppi is None:
            ppi_text.setText("")
        else:
            path = SearchFile.Search.searchPPI(carNum, Insp)
            if path:
                ppi_text.setText(f"<a href='file:///{path}'>{ppi}</a>")
            else:
                ppi_text.setText(f"{ppi}")
        ppi_text.setOpenExternalLinks(True)
        # Set the size policy of the text widgets to Expanding

        rrn_text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        exr_text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        er_text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        ppi_text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Add the labels and text to the layout
        layout.addWidget(rrn_label, 0, 0)
        layout.addWidget(exr_label, 1, 0)
        layout.addWidget(er_label, 2, 0)
        layout.addWidget(ppi_label, 3, 0)

        layout.addWidget(rrn_text, 0, 1)
        layout.addWidget(exr_text, 1, 1)
        layout.addWidget(er_text, 2, 1)
        layout.addWidget(ppi_text, 3, 1)

        # Set the window size
        window.resize(500, 300)

        window.show()
        # app.exec_()
        window.exec_()

def main(carnum, SList):
    import sys
    '''grab the function by values'''

    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main(car_num=carnum)
    ui.setupUi(Main)


    '''car number shows the location of the inspection point'''
    itemNum = 0
    IList = ["IN0", "INI", "PFP", "EXE", "EWC", "EWC1", "1WT", "INS", "1IF", "SBD",
             "HE1", "1IE", "2IE", "1IW", "2IW", "1CE", "2CE", "CPI", "UNE", "UWC",
             "CWC", "COT", "HPT", "REC", "UND", "ITN", "TUK", "WEG", "WCT", "GAU",
             "2WT", "PPR", "CUP", "CUR", "SCS", "DCS", "PSI", "DEL"]

    # for i, j in zip(ui.cist, IList):
            # print(i.objectName(), j)
    '''dont know why i can't make a loop to iterate over it, i decided to hardcode it'''
    insp_overview = InspOverview()
    ui.cist[0].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[0]))
    ui.cist[1].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[1]))
    ui.cist[2].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[2]))
    ui.cist[3].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[3]))
    ui.cist[4].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[4]))
    ui.cist[5].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[4]))
    ui.cist[6].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[6]))
    ui.cist[7].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[7]))
    ui.cist[8].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[8]))
    ui.cist[9].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[9]))
    ui.cist[10].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[10]))
    ui.cist[11].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[11]))
    ui.cist[12].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[12]))
    ui.cist[13].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[13]))
    ui.cist[14].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[14]))
    ui.cist[15].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[15]))
    ui.cist[16].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[16]))
    ui.cist[17].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[17]))
    ui.cist[18].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[18]))
    ui.cist[19].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[19]))
    ui.cist[20].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[20]))
    ui.cist[21].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[21]))
    ui.cist[22].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[22]))
    ui.cist[23].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[23]))
    ui.cist[24].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[24]))
    ui.cist[25].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[25]))
    ui.cist[26].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[26]))
    ui.cist[27].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[27]))
    ui.cist[28].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[28]))
    ui.cist[29].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[29]))
    ui.cist[30].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[30]))
    ui.cist[31].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[31]))
    ui.cist[32].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[32]))
    ui.cist[33].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[33]))
    ui.cist[34].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[34]))
    ui.cist[35].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[35]))
    ui.cist[36].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[36]))
    ui.cist[37].clicked.connect(lambda: insp_overview.main(ui.car_num, IList[37]))
    print(len(SList), len(IList), len(ui.cist))
    for i in SList:
        # print(ui.cist[itemNum].objectName())
        if i.upper() == "COMPLETED":
            ui.cist[itemNum].setStyleSheet("background-color: #90ee90;")
        elif i.upper() == "PENDING":
            ui.cist[itemNum].setStyleSheet("background-color: #ffffe0;")
        elif i.upper() == "STOP":
            ui.cist[itemNum].setStyleSheet("background-color: #ffcccb;")
        elif i.upper() == "WORKED":
            ui.cist[itemNum].setStyleSheet("background-color: #CBC3E3;")
        # else:
        #     ui.cist[itemNum].setStyleSheet("background-color: #FFFFFF;")
        '''Error position'''
        # print(IList[itemNum], ui.cist[itemNum].objectName(), SList[itemNum], itemNum)

        itemNum += 1
        # if itemNum == 37:
        #     itemNum = 36
    Main.show()
    sys.exit(app.exec_())

import sys
# print(sys.argv)
if len(sys.argv) > 1:
    car_num = sys.argv[1]
    StatusList = sys.argv[2].split(",")
    main(car_num, StatusList)
