# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_Form(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(parent)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(452, 166)
        self.refreshButton = QtWidgets.QPushButton(Form)
        self.refreshButton.setGeometry(QtCore.QRect(20, 110, 151, 31))
        self.refreshButton.setText("")
        self.refreshButton.setObjectName("refreshButton")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 421, 71))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
