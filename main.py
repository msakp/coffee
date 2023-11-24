from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTableWidgetItem, QAbstractItemView
from PyQt5 import uic
import sys
import sqlite3

class CoffeeViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.labels = ['id', 'название сорта', 'степень обжарки', 'молотый/в зернах',
                                                   'описание вкуса', 'цена', 'объем мл']
        
        self.addButton = QPushButton('Add')
        self.statusBar().addWidget(self.addButton)
        
        self.con = sqlite3.connect('coffee.sqlite')
        self.addEditWindow = addEditWindow(self)

        self.refresh()
        self.tableWidget.cellDoubleClicked.connect(self.edit)
        self.addButton.clicked.connect(self.add)

    def refresh(self):
        data = self.con.execute('SELECT * from item_list').fetchall()
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        for i, row in enumerate(data):
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))        

    def edit(self):
        self.addEditWindow.hide()
        row, col = self.sender().currentRow(), self.sender().currentColumn()
        self.addEditWindow.loadEdit(row, col)
        self.addEditWindow.show()

    def add(self):
        self.addEditWindow.hide()
        self.addEditWindow.loadAdd()
        self.addEditWindow.show()
        


class addEditWindow(QMainWindow):
    column_map = {'id': 'ID',
                  'название сорта': 'title',
                  'степень обжарки': 'degree',
                  'молотый/в зернах': 'type', 
                  'описание вкуса': 'description',
                  'цена': 'cost',
                  'объем мл': 'volume'}
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        uic.loadUi('addEditCoffeeForm.ui', self)
    
    def loadEdit(self, row, col):
        self.tableWidget.clear()
        self.currentRow = row
        self.currentCol = col
        self.refreshButton.clicked.connect(self.saveEdit)
        self.refreshButton.setText('Edit')
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setVerticalHeaderLabels([''])
        self.tableWidget.setHorizontalHeaderLabels([self.parent.labels[col]])
        self.tableWidget.setItem(0, 0, self.parent.tableWidget.item(row, col).clone())
        

    def loadAdd(self):
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setHorizontalHeaderLabels(self.parent.labels[1:])
        self.tableWidget.setVerticalHeaderLabels([''])
        self.refreshButton.clicked.connect(self.saveAdd)
        self.refreshButton.setText('Add')

    def saveEdit(self):
        request = f'''UPDATE item_list
                     SET '{self.column_map[self.parent.labels[self.currentCol]]}' = '{self.tableWidget.item(0, 0).text()}'
                     WHERE id = {self.currentRow + 1}'''
        self.parent.con.execute(request)
        self.parent.con.commit()
        self.hide()
        self.parent.refresh()

    def saveAdd(self):
        values = [self.tableWidget.item(0, i).text() for i in range(6) if self.tableWidget.item(0, i)]
        if len(values) != 6:
            self.statusBar().showMessage('table values cannot be NULL')
            return
        values = ','.join(list(map(lambda el: f"'{el}'", values[:-2])) + values[-2:])
        request = f"""INSERT INTO item_list(title,degree,type,description,cost,volume) VALUES({values})"""
        self.parent.con.execute(request)
        self.parent.con.commit()
        self.hide()
        self.parent.refresh()
        
   

def main():
    app = QApplication(sys.argv)
    window = CoffeeViewer()
    window.show()
    sys.exit(app.exec())

main()
