# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms\calc.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(448, 170)
        MainWindow.setMinimumSize(QtCore.QSize(448, 169))
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setToolTip("")
        MainWindow.setToolTipDuration(-1)
        MainWindow.setStyleSheet("")
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridFrame = QtWidgets.QFrame(self.centralwidget)
        self.gridFrame.setMinimumSize(QtCore.QSize(281, 151))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.gridFrame.setPalette(palette)
        self.gridFrame.setAutoFillBackground(True)
        self.gridFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.gridFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.gridFrame)
        self.lineEdit.setMaximumSize(QtCore.QSize(29, 20))
        self.lineEdit.setToolTip("")
        self.lineEdit.setToolTipDuration(1500)
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(3)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridFrame)
        self.label_11.setMinimumSize(QtCore.QSize(71, 20))
        self.label_11.setMaximumSize(QtCore.QSize(71, 20))
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridFrame)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(29, 20))
        self.lineEdit_4.setToolTip("")
        self.lineEdit_4.setToolTipDuration(1500)
        self.lineEdit_4.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setMaxLength(3)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_3.addWidget(self.lineEdit_4, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridFrame)
        self.label_9.setMaximumSize(QtCore.QSize(71, 20))
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridFrame)
        self.lineEdit_5.setMaximumSize(QtCore.QSize(29, 20))
        self.lineEdit_5.setToolTip("")
        self.lineEdit_5.setToolTipDuration(1500)
        self.lineEdit_5.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setMaxLength(2)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_3.addWidget(self.lineEdit_5, 1, 3, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridFrame)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_3.addWidget(self.comboBox, 2, 1, 1, 6)
        self.label_5 = QtWidgets.QLabel(self.gridFrame)
        self.label_5.setMaximumSize(QtCore.QSize(14, 36))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 4, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridFrame)
        self.lineEdit_6.setMaximumSize(QtCore.QSize(29, 20))
        self.lineEdit_6.setToolTip("")
        self.lineEdit_6.setToolTipDuration(1500)
        self.lineEdit_6.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_6.setText("")
        self.lineEdit_6.setMaxLength(2)
        self.lineEdit_6.setFrame(True)
        self.lineEdit_6.setCursorPosition(0)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setDragEnabled(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_3.addWidget(self.lineEdit_6, 1, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridFrame)
        self.label_6.setMaximumSize(QtCore.QSize(14, 36))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 4, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridFrame)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(29, 20))
        self.lineEdit_2.setToolTip("")
        self.lineEdit_2.setToolTipDuration(1500)
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setMaxLength(2)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 0, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridFrame)
        self.label_8.setMinimumSize(QtCore.QSize(0, 20))
        self.label_8.setMaximumSize(QtCore.QSize(14, 36))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 6, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridFrame)
        self.label_7.setMaximumSize(QtCore.QSize(14, 36))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 6, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridFrame)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(29, 20))
        self.lineEdit_3.setToolTip("")
        self.lineEdit_3.setToolTipDuration(1500)
        self.lineEdit_3.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setMaxLength(2)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 0, 5, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridFrame)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_2, 3, 1, 1, 6)
        self.label_12 = QtWidgets.QLabel(self.gridFrame)
        self.label_12.setMinimumSize(QtCore.QSize(71, 20))
        self.label_12.setMaximumSize(QtCore.QSize(71, 20))
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridFrame)
        self.label_10.setMaximumSize(QtCore.QSize(71, 20))
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 3, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridFrame)
        self.lineEdit_7.setText("")
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_3.addWidget(self.lineEdit_7, 4, 0, 1, 4)
        self.pushButton = QtWidgets.QPushButton(self.gridFrame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 4, 4, 1, 3)
        self.label_16 = QtWidgets.QLabel(self.gridFrame)
        self.label_16.setMaximumSize(QtCore.QSize(14, 36))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 0, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridFrame)
        self.label_17.setMaximumSize(QtCore.QSize(14, 36))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 1, 2, 1, 1)
        self.horizontalLayout.addWidget(self.gridFrame)
        self.gridFrame1 = QtWidgets.QFrame(self.centralwidget)
        self.gridFrame1.setMinimumSize(QtCore.QSize(141, 151))
        self.gridFrame1.setMaximumSize(QtCore.QSize(141, 151))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.gridFrame1.setPalette(palette)
        self.gridFrame1.setAutoFillBackground(True)
        self.gridFrame1.setFrameShape(QtWidgets.QFrame.Box)
        self.gridFrame1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridFrame1.setObjectName("gridFrame1")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame1)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.gridFrame1)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(68, 20))
        self.lineEdit_9.setMaximumSize(QtCore.QSize(71, 20))
        self.lineEdit_9.setText("")
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridFrame1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.gridFrame1)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(68, 20))
        self.lineEdit_10.setMaximumSize(QtCore.QSize(71, 20))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 2, 1, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.gridFrame1)
        self.lineEdit_11.setMinimumSize(QtCore.QSize(68, 20))
        self.lineEdit_11.setMaximumSize(QtCore.QSize(71, 20))
        self.lineEdit_11.setText("")
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 3, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridFrame1)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 2, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridFrame1)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 3, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.gridFrame1)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(68, 20))
        self.lineEdit_8.setMaximumSize(QtCore.QSize(71, 20))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridFrame1)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.gridFrame1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        MainWindow.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        MainWindow.setTabOrder(self.lineEdit_5, self.lineEdit_6)
        MainWindow.setTabOrder(self.lineEdit_6, self.comboBox)
        MainWindow.setTabOrder(self.comboBox, self.comboBox_2)
        MainWindow.setTabOrder(self.comboBox_2, self.lineEdit_7)
        MainWindow.setTabOrder(self.lineEdit_7, self.pushButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Map code calculator"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_11.setText(_translate("MainWindow", "Longitude"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "Hemisphere"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "0"))
        self.comboBox.setItemText(0, _translate("MainWindow", "NE"))
        self.comboBox.setItemText(1, _translate("MainWindow", "NW"))
        self.comboBox.setItemText(2, _translate("MainWindow", "SE"))
        self.comboBox.setItemText(3, _translate("MainWindow", "SW"))
        self.label_5.setText(_translate("MainWindow", "′"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "′"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "′′"))
        self.label_7.setText(_translate("MainWindow", "′′"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "0"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "1: 1 000 000"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "1: 500 000"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "1: 200 000"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "1: 100 000"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "1: 50 000"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "1: 25 000"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "1: 10 000"))
        self.label_12.setText(_translate("MainWindow", "Latitude"))
        self.label_10.setText(_translate("MainWindow", "Scale"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.label_16.setText(_translate("MainWindow", "°"))
        self.label_17.setText(_translate("MainWindow", "°"))
        self.label_2.setText(_translate("MainWindow", "South"))
        self.label_14.setText(_translate("MainWindow", "East"))
        self.label_15.setText(_translate("MainWindow", "West"))
        self.label_13.setText(_translate("MainWindow", "North"))

