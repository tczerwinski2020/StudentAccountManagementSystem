# This code represents the code generated using PyQt Designer for your main UI.
# Note that the code will be missing several parts such as call to the constructor
# and setup methods.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
from add_student_window import Add_Student # generated after adding graphics to your UI in Pyqt Designer
from db_manager import DBManager
from student_account import StudentAccount
from search_by_id_dialog import Search_ID_Dialog
from search_by_name_dialog import Search_Name_Dialog
from thank_you_dialog import Thank_You_Dialog
import sys
import urllib.request

# Make sure to use a valid class name and 
# import QMainWindow for your main UI and QDialog for the dialogs
# instead of a generic object

# Class of the main window in this application
class MainUI(QMainWindow):
    # Constructor for a MainUI object
    def __init__(self):
        # This is needed here to inherit methods and data from QMainWindow
        super(MainUI, self).__init__()
        self._system_name = "Student Account Management System (SAMS)"
        self.setup_ui(self)  # This method was provided by PyQt Designer. Note the snake_case update
        self.retranslate_ui(self)  # This method was provided by PyQt Designer. Note the snake_case update
        self.load_records()

    # Constructs the main window's attributes
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(723, 518)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.quit = QtWidgets.QPushButton(self.centralwidget)
        self.quit.setGeometry(QtCore.QRect(560, 430, 113, 32))
        self.quit.setObjectName("quit")
        self.quit.clicked.connect(self.close_application)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 320, 471, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_student = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.add_student.setObjectName("add_student")
        self.horizontalLayout.addWidget(self.add_student)
        self.add_student.clicked.connect(self.open_add_student)
        self.search_by_id = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.search_by_id.setObjectName("search_by_id")
        self.horizontalLayout.addWidget(self.search_by_id)
        self.search_by_id.clicked.connect(self.search_student_by_id)
        self.search_by_name = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.search_by_name.setObjectName("search_by_name")
        self.horizontalLayout.addWidget(self.search_by_name)
        self.search_by_name.clicked.connect(self.search_student_by_name)
        self.panther_image = QtWidgets.QLabel(self.centralwidget)
        self.panther_image.setGeometry(QtCore.QRect(-20, 10, 741, 231))
        self.panther_image.setAutoFillBackground(False)
        self.panther_image.setText("")
        self.panther_image.setPixmap(self.load_image("https://www.fit.edu/media/site-specific/header-images/panther.jpg"))
        self.panther_image.setScaledContents(True)
        self.panther_image.setObjectName("panther_image")
        self.SAMS_label = QtWidgets.QLabel(self.centralwidget)
        self.SAMS_label.setGeometry(QtCore.QRect(130, 260, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setKerning(True)
        self.SAMS_label.setFont(font)
        self.SAMS_label.setAlignment(QtCore.Qt.AlignCenter)
        self.SAMS_label.setObjectName("SAMS_label")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 440, 161, 21))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 723, 24))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuImportant = QtWidgets.QMenu(self.menuBar)
        self.menuImportant.setObjectName("menuImportant")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAdd_Student = QtWidgets.QAction(MainWindow)
        self.actionAdd_Student.setObjectName("actionAdd_Student")
        self.actionAdd_Student.triggered.connect(self.open_add_student)
        self.actionSearch_By_ID = QtWidgets.QAction(MainWindow)
        self.actionSearch_By_ID.setObjectName("actionSearch_By_ID")
        self.actionSearch_By_ID.triggered.connect(self.search_student_by_id)
        self.actionSearch_By_Name = QtWidgets.QAction(MainWindow)
        self.actionSearch_By_Name.setObjectName("actionSearch_By_Name")
        self.actionSearch_By_Name.triggered.connect(self.search_student_by_name)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.triggered.connect(self.close_application)
        self.actionThank_You = QtWidgets.QAction(MainWindow)
        self.actionThank_You.setObjectName("actionThank_You")
        self.actionThank_You.triggered.connect(self.open_thank_you)
        self.menuFile.addAction(self.actionAdd_Student)
        self.menuFile.addAction(self.actionSearch_By_ID)
        self.menuFile.addAction(self.actionSearch_By_Name)
        self.menuFile.addAction(self.actionQuit)
        self.menuImportant.addSeparator()
        self.menuImportant.addAction(self.actionThank_You)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuImportant.menuAction())

        self.retranslate_ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Translate main window's attributes
    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.quit.setText(_translate("MainWindow", "Quit"))
        self.add_student.setText(_translate("MainWindow", "Add Student"))
        self.search_by_id.setText(_translate("MainWindow", "Search by ID"))
        self.search_by_name.setText(_translate("MainWindow", "Search by Name"))
        self.SAMS_label.setText(_translate("MainWindow", "Student Account Management System (SAMS)"))
        self.label.setText(_translate("MainWindow", "Check out the menu bar!"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuImportant.setTitle(_translate("MainWindow", "Important"))
        self.actionAdd_Student.setText(_translate("MainWindow", "Add Student"))
        self.actionAdd_Student.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSearch_By_ID.setText(_translate("MainWindow", "Search By ID"))
        self.actionSearch_By_ID.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionSearch_By_Name.setText(_translate("MainWindow", "Search By Name"))
        self.actionSearch_By_Name.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionThank_You.setText(_translate("MainWindow", "Thank You"))
        self.actionThank_You.setShortcut(_translate("MainWindow", "Ctrl+T"))


    # Opens the search-by-student-name dialog.
    def search_student_by_name(self):
        dialog = Search_Name_Dialog(self)
        dialog.exec_()
        dialog.show()

    # Opens the search-by-student-id dialog.
    def search_student_by_id(self):
        dialog = Search_ID_Dialog(self)
        dialog.exec_()
        dialog.show()

    # Opens add-student dialog
    def open_add_student(self):
        dialog = Add_Student(self)
        dialog.exec_()
        dialog.show()

    # Opens thank-you dialog
    def open_thank_you(self):
        dialog = Thank_You_Dialog(self)
        dialog.exec_()
        dialog.show()

    # Closes the application
    def close_application(self):
        self.close()

    # Loads an image from a link into a pixmap
    def load_image(self, link):
        img = QImage()
        img.loadFromData(self.read_img(link))

        pixmap = QPixmap.fromImage(img)
        return pixmap

    # Reads image from website, returns in bytes
    def read_img(self, link):
        img_bytes = urllib.request.urlopen(link).read()
        return img_bytes

    # Loads the initial student records into the database
    def load_records(self):
        db_manager = DBManager()
        db_manager.init_tables()  # initialize your init_tables
        # process the lists and load data into your DB
        names = ["Willena Shupe", "Jolanda Agin", "Leta Stacker", "Leonora Oliverio", "Birgit Stoudt", "Aron Valtierra",
                 "Vi Buschman", "Janee Barnwell", "Agnus Flower", "Byron Mccartney", "Victoria Crabill", "Amy Swinton",
                 "Arla Mohamed", "Bryon Vester", "Lue Benway", "Mozelle Macauley", "Suzann Galindo", "Delicia Barriere",
                 "Marcella Uyehara", "Jane Curley"]
        admittance_years = [2020, 2019, 2016, 2019, 2013, 2014, 2014, 2018, 2016, 2012, 2014, 2015, 2018, 2013, 2019,
                            2017, 2019, 2020, 2015, 2013]
        for i in range(len(names)):
            first = names[i].split(" ")[0]
            second = names[i].split(" ")[1]
            student = StudentAccount(first, second, admittance_years[i])
            student.set_photo(first + "_" + second + "_" + str(student.get_student_id()) + ".png")
            record = student.get_record()
            db_manager.add_record(record)

def main():
    app = QApplication(sys.argv)
    ui = MainUI()  # creates an instance of the MainUI
    ui.show()
    sys.exit(app.exec())

main()