# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'toolGenerateResultsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_toolGenerateResultsWindow(object):
    def setupUi(self, toolGenerateResultsWindow):
        toolGenerateResultsWindow.setObjectName("toolGenerateResultsWindow")
        toolGenerateResultsWindow.resize(520, 200)
        self.centralwidget = QtWidgets.QWidget(toolGenerateResultsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnGenerate = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenerate.setGeometry(QtCore.QRect(400, 130, 111, 41))
        self.btnGenerate.setObjectName("btnGenerate")
        self.btnChooseCurrentPath = QtWidgets.QPushButton(self.centralwidget)
        self.btnChooseCurrentPath.setGeometry(QtCore.QRect(10, 10, 501, 31))
        self.btnChooseCurrentPath.setObjectName("btnChooseCurrentPath")
        self.textCurrentPath = QtWidgets.QLabel(self.centralwidget)
        self.textCurrentPath.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.textCurrentPath.setObjectName("textCurrentPath")
        self.textChosenCurrentPath = QtWidgets.QLabel(self.centralwidget)
        self.textChosenCurrentPath.setGeometry(QtCore.QRect(90, 50, 421, 16))
        self.textChosenCurrentPath.setObjectName("textChosenCurrentPath")
        toolGenerateResultsWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(toolGenerateResultsWindow)
        self.statusbar.setObjectName("statusbar")
        toolGenerateResultsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(toolGenerateResultsWindow)
        QtCore.QMetaObject.connectSlotsByName(toolGenerateResultsWindow)

    def retranslateUi(self, toolGenerateResultsWindow):
        _translate = QtCore.QCoreApplication.translate
        toolGenerateResultsWindow.setWindowTitle(_translate("toolGenerateResultsWindow", "MainWindow"))
        self.btnGenerate.setText(_translate("toolGenerateResultsWindow", "Сгенерировать"))
        self.btnChooseCurrentPath.setText(_translate("toolGenerateResultsWindow", "Указать путь к файлу с конфигурацией очков"))
        self.textCurrentPath.setText(_translate("toolGenerateResultsWindow", "Текущий путь:"))
        self.textChosenCurrentPath.setText(_translate("toolGenerateResultsWindow", "Выберите файл с конфигурацией очков"))