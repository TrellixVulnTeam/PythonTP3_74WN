from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Client")
        self.setFixedSize(1000, 400)
        self.label1 = QLabel("Enter your hostname IP:", self)
        self.label1.move(10, 10)
        self.text = QLineEdit(self)
        self.text.move(10, 30)
        
        self.label2 = QLabel("Enter the website IP:", self)
        self.label2.move(10, 100)
        self.text2 = QLineEdit(self)
        self.text2.move(10, 120)

        self.label3 = QLabel("Enter your API key:", self)
        self.label3.move(10, 190)
        self.text3 = QLineEdit(self)
        self.text3.move(10, 210)

        self.button = QPushButton("Send", self)
        self.button.move(10, 240)

        self.label4 = QLabel("Answer:", self)
        self.label4.move(10, 300)

        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()

    def on_click(self):
        hostname = self.text.text()
        addip = self.text2.text()
        apikey = self.text3.text()

        if hostname == "" or addip == "" or apikey == "":
            QMessageBox.about(self, "Error", "Please fill the fields")
        else:
            res = self.__query(hostname, addip, apikey)
            if res:
                self.label4.setText(str(res))
                self.label4.adjustSize()
                self.show()

    def __query(self, hostname, addip, apikey):
        url = "http://" + hostname + "/ip/" + addip + "?key=" + apikey
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()