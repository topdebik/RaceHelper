# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'toolGeneratePlacesWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_toolGeneratePlacesWindow(object):
    def setupUi(self, toolGeneratePlacesWindow):
        toolGeneratePlacesWindow.setObjectName("toolGeneratePlacesWindow")
        toolGeneratePlacesWindow.resize(400, 200)
        self.centralwidget = QtWidgets.QWidget(toolGeneratePlacesWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.boxGenerateMethod = QtWidgets.QComboBox(self.centralwidget)
        self.boxGenerateMethod.setGeometry(QtCore.QRect(190, 10, 201, 22))
        self.boxGenerateMethod.setObjectName("boxGenerateMethod")
        self.boxGenerateMethod.addItem("")
        self.boxGenerateMethod.addItem("")
        self.boxGenerateMethod.addItem("")
        self.textGenerateMethod = QtWidgets.QLabel(self.centralwidget)
        self.textGenerateMethod.setGeometry(QtCore.QRect(10, 10, 101, 21))
        self.textGenerateMethod.setObjectName("textGenerateMethod")
        self.textMaxKarts = QtWidgets.QLabel(self.centralwidget)
        self.textMaxKarts.setGeometry(QtCore.QRect(10, 40, 181, 21))
        self.textMaxKarts.setObjectName("textMaxKarts")
        self.boxMaxKarts = QtWidgets.QSpinBox(self.centralwidget)
        self.boxMaxKarts.setGeometry(QtCore.QRect(190, 40, 42, 22))
        self.boxMaxKarts.setMinimum(1)
        self.boxMaxKarts.setObjectName("boxMaxKarts")
        self.textMinKarts = QtWidgets.QLabel(self.centralwidget)
        self.textMinKarts.setGeometry(QtCore.QRect(10, 70, 181, 21))
        self.textMinKarts.setObjectName("textMinKarts")
        self.boxMinKarts = QtWidgets.QSpinBox(self.centralwidget)
        self.boxMinKarts.setGeometry(QtCore.QRect(190, 70, 42, 22))
        self.boxMinKarts.setMinimum(0)
        self.boxMinKarts.setObjectName("boxMinKarts")
        self.textRunsPerParticipant = QtWidgets.QLabel(self.centralwidget)
        self.textRunsPerParticipant.setGeometry(QtCore.QRect(10, 100, 181, 21))
        self.textRunsPerParticipant.setObjectName("textRunsPerParticipant")
        self.boxRunsPerParticipant = QtWidgets.QSpinBox(self.centralwidget)
        self.boxRunsPerParticipant.setGeometry(QtCore.QRect(190, 100, 42, 22))
        self.boxRunsPerParticipant.setMinimum(1)
        self.boxRunsPerParticipant.setObjectName("boxRunsPerParticipant")
        self.btnGenerate = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenerate.setGeometry(QtCore.QRect(280, 130, 111, 41))
        self.btnGenerate.setObjectName("btnGenerate")
        toolGeneratePlacesWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(toolGeneratePlacesWindow)
        self.statusbar.setObjectName("statusbar")
        toolGeneratePlacesWindow.setStatusBar(self.statusbar)

        self.retranslateUi(toolGeneratePlacesWindow)
        QtCore.QMetaObject.connectSlotsByName(toolGeneratePlacesWindow)

    def retranslateUi(self, toolGeneratePlacesWindow):
        _translate = QtCore.QCoreApplication.translate
        toolGeneratePlacesWindow.setWindowTitle(_translate("toolGeneratePlacesWindow", "MainWindow"))
        self.boxGenerateMethod.setCurrentText(_translate("toolGeneratePlacesWindow", "Случайно"))
        self.boxGenerateMethod.setItemText(0, _translate("toolGeneratePlacesWindow", "Случайно"))
        self.boxGenerateMethod.setItemText(1, _translate("toolGeneratePlacesWindow", "По алфавиту"))
        self.boxGenerateMethod.setItemText(2, _translate("toolGeneratePlacesWindow", "По алфавиту, в обратном порядке"))
        self.textGenerateMethod.setText(_translate("toolGeneratePlacesWindow", "Способ генерации"))
        self.textMaxKarts.setText(_translate("toolGeneratePlacesWindow", "Максимальное количество картов"))
        self.textMinKarts.setText(_translate("toolGeneratePlacesWindow", "Минимальное количество картов"))
        self.textRunsPerParticipant.setText(_translate("toolGeneratePlacesWindow", "Количество заездов участника"))
        self.btnGenerate.setText(_translate("toolGeneratePlacesWindow", "Сгенерировать"))