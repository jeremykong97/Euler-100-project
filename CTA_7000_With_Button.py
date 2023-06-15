import sys
import tkinter.filedialog

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QFrame, QLineEdit
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QPixmap, QDragEnterEvent, QDragMoveEvent, QDropEvent
import subprocess
import sqlite3
from tkinter import messagebox
import DiagonstingDocuments

class DragButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            print("File moved to button region Drop Folder")
            print(event.mimeData().urls())
    def dragMoveEvent(self, event: QDragMoveEvent):

        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        urls = event.mimeData().urls()
        for url in urls:
            examination = DiagonstingDocuments.initialDocuments()
            file = url.toLocalFile()
            '''wrong examination file to regonize which documents is that'''
            '''this file will also debug any documentation errors'''
            examination.documents(file)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(620, 270)
        self.setAcceptDrops(True)
        self.setWindowTitle("CRRC Chicago CTA-7000 Project Manage Console")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a vertical layout to hold the left-side buttons
        button_layout = QVBoxLayout()

        self.InspectionInput = QLineEdit()
        self.InspectionInput.setSizePolicy(self.InspectionInput.sizePolicy().Fixed, self.InspectionInput.sizePolicy().Fixed)
        self.InspectionInput.setMinimumSize(220, 20)
        self.InspectionInput.setStyleSheet("font-family: Arial; font-size: 12pt; color: blue; font-style: italic;")
        self.InspectionInput.setPlaceholderText("Enter Car Number")

        InspectionView = QPushButton("Inspection Overview")
        InspectionView.setSizePolicy(InspectionView.sizePolicy().Fixed, InspectionView.sizePolicy().Fixed)
        InspectionView.setMinimumSize(220, 60)

        '''code for main Upload Function'''
        Uploadbutton = DragButton("Drop Folder")
        Uploadbutton.setSizePolicy(Uploadbutton.sizePolicy().Fixed, Uploadbutton.sizePolicy().Fixed)
        Uploadbutton.setMinimumSize(220, 60)
        # Uploadbutton.setText("Drop Folder")


        button_layout.addWidget(self.InspectionInput)
        button_layout.addWidget(InspectionView)
        button_layout.addWidget(Uploadbutton)


        main_layout = QHBoxLayout(central_widget)

        main_layout.addLayout(button_layout)

        pixmap = QPixmap(r"M:\QA 11122019\24_JeremyProgrammingFolder\EmailPic.png")
        pixmap_label = QLabel()
        pixmap_label.setPixmap(pixmap)
        main_layout.addWidget(pixmap_label)
        InspectionView.clicked.connect(self.InspectionOverviewClickMethod)

        # Connect the returnPressed signal of the QLineEdit to the click slot of the InspectionView button
        self.InspectionInput.returnPressed.connect(InspectionView.click)

    def InspectionOverviewClickMethod(self):
        # tkinter.filedialog.askopenfiles()
        CarNumber = self.InspectionInput.text()

        '''find current status of the carnumber'''
        statusList = self.CurrenctStatus(CarNumber)
        if CarNumber.isdigit():
            if CarNumber:
                # subprocess.call(['python', 'CTA_7000_Main.py', CarNumber, statusList])
                # print("check carnumber")
                subprocess.call(['python', 'CTA_7000_RevisedMain.py', CarNumber, statusList])
                # import CTA_7000_RevisedMain
                # StatusList = statusList.split(",")
                # CTA_7000_RevisedMain.main(CarNumber, StatusList)

            # else:
            #     subprocess.call(['python', 'CTA_7000_Main.py', '7022'])
        else:
            messagebox.showerror(message="please input car number only")
    '''this function is to find the current status of the car'''
    
    def CurrenctStatus(self, Car):
        import UpdateDatabase
        result = ""
        con = sqlite3.connect(UpdateDatabase.path)
        cur = con.cursor()

        #IN0    0-number zero
        IList = ["IN0", "INI", "PFP", "EXE", "EWC", "EWC", "1WT", "INS", "1IF", "SBD",
                 "HE1", "1IE", "2IE", "1IW", "2IW", "1CE", "2CE", "CPI", "UNE", "UWC",
                 "CWC", "COT", "HPT", "REC", "UND", "ITN", "TUK", "WEG", "WCT", "GAU",
                 "2WT", "PPR", "CUP", "CUR", "SCS", "DCS", "PSI", "DEL"]

        for i in IList:
            cur.execute(f"SELECT Status from CarInsp where Car_INSP_Point = '{Car}{i}'")
            CStatus = cur.fetchone()
            if CStatus:
                result += f"{CStatus[0]},"
                print(",,,,", i, CStatus[0])

            else:
                result += f"None,"

        return result[:-1]


app = QApplication(sys.argv)
demo = MainWindow()
demo.show()
sys.exit(app.exec_())

