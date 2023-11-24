from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTableWidgetItem
from PyQt5 import uic
import sys
import sqlite3

class CoffeeViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.updateButton = QPushButton('Update')
        self.statusBar().addWidget(self.updateButton)
        self.con = sqlite3.connect('coffee.sqlite')
        self.refresh()

        self.updateButton.clicked.connect(self.refresh)

    def refresh(self):
        data = self.con.execute('SELECT * from item_list').fetchall()
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['id', 'название сорта', 'степень обжарки', 'молотый/в зернах',
                                                   'описание вкуса', 'цена', ' объем мл'])
        for i, row in enumerate(data):
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))        


def main():
    app = QApplication(sys.argv)
    window = CoffeeViewer()
    window.show()
    sys.exit(app.exec())

main()