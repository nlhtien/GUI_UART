# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uart_tool.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class SecondMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(789, 845)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 201, 201))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 20, 93, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox_uart = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_uart.setObjectName("comboBox_uart")
        self.comboBox_uart.addItem("")
        self.comboBox_uart.addItem("")
        self.comboBox_uart.addItem("")
        self.comboBox_uart.addItem("")
        self.comboBox_uart.addItem("")
        self.comboBox_uart.addItem("")
        self.comboBox_uart.addItem("")
        self.comboBox_uart.addItem("")
        self.comboBox_uart.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_uart)
        self.comboBox_baud = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_baud.setObjectName("comboBox_baud")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_baud)
        self.comboBox_databit = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_databit.setObjectName("comboBox_databit")
        self.comboBox_databit.addItem("")
        self.comboBox_databit.addItem("")
        self.comboBox_databit.addItem("")
        self.comboBox_databit.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_databit)
        self.comboBox_polarity = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_polarity.setObjectName("comboBox_polarity")
        self.comboBox_polarity.addItem("")
        self.comboBox_polarity.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_polarity)
        self.comboBox_stopbit = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_stopbit.setObjectName("comboBox_stopbit")
        self.comboBox_stopbit.addItem("")
        self.comboBox_stopbit.addItem("")
        self.comboBox_stopbit.addItem("")
        self.comboBox_stopbit.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_stopbit)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 20, 81, 171))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 200, 201, 131))
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_recvascii = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_recvascii.setGeometry(QtCore.QRect(20, 20, 61, 16))
        self.radioButton_recvascii.setObjectName("radioButton_recvascii")
        self.radioButton_recvhex = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_recvhex.setGeometry(QtCore.QRect(120, 20, 51, 16))
        self.radioButton_recvhex.setObjectName("radioButton_recvhex")
        self.checkBox_autoline = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_autoline.setGeometry(QtCore.QRect(20, 40, 151, 21))
        self.checkBox_autoline.setObjectName("checkBox_autoline")
        self.checkBox_showsend = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_showsend.setGeometry(QtCore.QRect(20, 70, 151, 21))
        self.checkBox_showsend.setObjectName("checkBox_showsend")
        self.checkBox_showtime = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_showtime.setGeometry(QtCore.QRect(20, 100, 151, 21))
        self.checkBox_showtime.setObjectName("checkBox_showtime")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 330, 201, 111))
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioButton_sendascii = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_sendascii.setGeometry(QtCore.QRect(20, 20, 61, 16))
        self.radioButton_sendascii.setObjectName("radioButton_sendascii")
        self.radioButton_sendhex = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_sendhex.setGeometry(QtCore.QRect(120, 20, 51, 16))
        self.radioButton_sendhex.setObjectName("radioButton_sendhex")
        self.checkBox_repeatsend = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_repeatsend.setGeometry(QtCore.QRect(20, 50, 71, 21))
        self.checkBox_repeatsend.setObjectName("checkBox_repeatsend")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(150, 80, 51, 21))
        self.label_7.setObjectName("label_7")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox.setGeometry(QtCore.QRect(20, 80, 121, 22))
        self.spinBox.setMaximum(10000)
        self.spinBox.setObjectName("spinBox")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(220, 10, 561, 201))
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit_get = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_get.setGeometry(QtCore.QRect(220, 220, 451, 41))
        self.textEdit_get.setObjectName("textEdit_get")
        self.btn_send = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send.setGeometry(QtCore.QRect(680, 220, 101, 41))
        self.btn_send.setAutoFillBackground(False)
        self.btn_send.setObjectName("btn_send")
        self.btn_send_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send_2.setGeometry(QtCore.QRect(220, 380, 101, 61))
        self.btn_send_2.setAutoFillBackground(False)
        self.btn_send_2.setObjectName("btn_send_2")
        self.btn_send_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send_3.setGeometry(QtCore.QRect(340, 380, 101, 61))
        self.btn_send_3.setAutoFillBackground(False)
        self.btn_send_3.setObjectName("btn_send_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(220, 270, 561, 101))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.FREQ = QtWidgets.QTextEdit(self.centralwidget)
        self.FREQ.setGeometry(QtCore.QRect(140, 550, 141, 41))
        self.FREQ.setObjectName("FREQ")
        self.comboBox_plot = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_plot.setGeometry(QtCore.QRect(140, 709, 141, 41))
        self.comboBox_plot.setObjectName("comboBox_plot")
        self.comboBox_plot.addItem("")
        self.comboBox_plot.addItem("")
        self.comboBox_plot.addItem("")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 460, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 560, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.AMP = QtWidgets.QTextEdit(self.centralwidget)
        self.AMP.setGeometry(QtCore.QRect(140, 450, 141, 41))
        self.AMP.setObjectName("AMP")
        self.comboBox_channel = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_channel.setGeometry(QtCore.QRect(140, 660, 141, 41))
        self.comboBox_channel.setObjectName("comboBox_channel")
        self.comboBox_channel.addItem("")
        self.comboBox_channel.addItem("")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 719, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 669, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.slider1 = QtWidgets.QSlider(self.centralwidget)
        self.slider1.setGeometry(QtCore.QRect(70, 510, 160, 30))
        self.slider1.setMinimumSize(QtCore.QSize(0, 20))
        self.slider1.setOrientation(QtCore.Qt.Horizontal)
        self.slider1.setObjectName("slider1")
        self.slider2 = QtWidgets.QSlider(self.centralwidget)
        self.slider2.setGeometry(QtCore.QRect(70, 610, 160, 30))
        self.slider2.setMinimumSize(QtCore.QSize(0, 20))
        self.slider2.setOrientation(QtCore.Qt.Horizontal)
        self.slider2.setObjectName("slider2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(289, 449, 491, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_grafica = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_grafica.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_grafica.setObjectName("verticalLayout_grafica")
        self.btn_send_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send_4.setGeometry(QtCore.QRect(460, 380, 101, 61))
        self.btn_send_4.setAutoFillBackground(False)
        self.btn_send_4.setObjectName("btn_send_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionstart = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("start.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionstart.setIcon(icon)
        self.actionstart.setObjectName("actionstart")
        self.actionpause = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pause.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionpause.setIcon(icon1)
        self.actionpause.setObjectName("actionpause")
        self.actionstop = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("stop.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionstop.setIcon(icon2)
        self.actionstop.setObjectName("actionstop")
        self.actionclean = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("clean.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionclean.setIcon(icon3)
        self.actionclean.setObjectName("actionclean")
        self.actionCD = QtWidgets.QAction(MainWindow)
        self.actionCD.setObjectName("actionCD")
        self.actionCHECK = QtWidgets.QAction(MainWindow)
        self.actionCHECK.setObjectName("actionCHECK")
        self.actionPLOT = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../image.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPLOT.setIcon(icon4)
        self.actionPLOT.setObjectName("actionPLOT")
        self.actionPLOT_TRIANGULAR = QtWidgets.QAction(MainWindow)
        self.actionPLOT_TRIANGULAR.setIcon(icon4)
        self.actionPLOT_TRIANGULAR.setObjectName("actionPLOT_TRIANGULAR")
        self.actionPLOT_SINE = QtWidgets.QAction(MainWindow)
        self.actionPLOT_SINE.setIcon(icon4)
        self.actionPLOT_SINE.setObjectName("actionPLOT_SINE")
        self.actionadd = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("image.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionadd.setIcon(icon5)
        self.actionadd.setObjectName("actionadd")
        self.menu.addAction(self.actionstart)
        self.menu.addAction(self.actionpause)
        self.menu.addAction(self.actionstop)
        self.menu.addAction(self.actionclean)
        self.menu.addAction(self.actionadd)
        self.menubar.addAction(self.menu.menuAction())
        self.toolBar.addAction(self.actionstart)
        self.toolBar.addAction(self.actionpause)
        self.toolBar.addAction(self.actionstop)
        self.toolBar.addAction(self.actionclean)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "SERIAL"))
        self.comboBox_uart.setItemText(0, _translate("MainWindow", "COM1"))
        self.comboBox_uart.setItemText(1, _translate("MainWindow", "COM2"))
        self.comboBox_uart.setItemText(2, _translate("MainWindow", "COM3"))
        self.comboBox_uart.setItemText(3, _translate("MainWindow", "COM4"))
        self.comboBox_uart.setItemText(4, _translate("MainWindow", "COM5"))
        self.comboBox_uart.setItemText(5, _translate("MainWindow", "COM6"))
        self.comboBox_uart.setItemText(6, _translate("MainWindow", "COM7"))
        self.comboBox_uart.setItemText(7, _translate("MainWindow", "COM8"))
        self.comboBox_uart.setItemText(8, _translate("MainWindow", "COM9"))
        self.comboBox_baud.setItemText(0, _translate("MainWindow", "2400"))
        self.comboBox_baud.setItemText(1, _translate("MainWindow", "4800"))
        self.comboBox_baud.setItemText(2, _translate("MainWindow", "9600"))
        self.comboBox_baud.setItemText(3, _translate("MainWindow", "19200"))
        self.comboBox_baud.setItemText(4, _translate("MainWindow", "38400"))
        self.comboBox_baud.setItemText(5, _translate("MainWindow", "57600"))
        self.comboBox_baud.setItemText(6, _translate("MainWindow", "115200"))
        self.comboBox_baud.setItemText(7, _translate("MainWindow", "128000"))
        self.comboBox_baud.setItemText(8, _translate("MainWindow", "256000"))
        self.comboBox_databit.setItemText(0, _translate("MainWindow", "5"))
        self.comboBox_databit.setItemText(1, _translate("MainWindow", "6"))
        self.comboBox_databit.setItemText(2, _translate("MainWindow", "7"))
        self.comboBox_databit.setItemText(3, _translate("MainWindow", "8"))
        self.comboBox_polarity.setCurrentText(_translate("MainWindow", "0"))
        self.comboBox_polarity.setItemText(0, _translate("MainWindow", "0"))
        self.comboBox_polarity.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_stopbit.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_stopbit.setItemText(1, _translate("MainWindow", "1.5"))
        self.comboBox_stopbit.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_stopbit.setItemText(3, _translate("MainWindow", "2.5"))
        self.label.setText(_translate("MainWindow", "SERIAL PORT"))
        self.label_2.setText(_translate("MainWindow", "BAUD RATE"))
        self.label_3.setText(_translate("MainWindow", "DATA BITS"))
        self.label_4.setText(_translate("MainWindow", "PARITY"))
        self.label_5.setText(_translate("MainWindow", "STOP BITS"))
        self.groupBox_2.setTitle(_translate("MainWindow", "RECEIVING SETTING"))
        self.radioButton_recvascii.setText(_translate("MainWindow", "ASCII"))
        self.radioButton_recvhex.setText(_translate("MainWindow", "HEX"))
        self.checkBox_autoline.setText(_translate("MainWindow", "AUTOMATION"))
        self.checkBox_showsend.setText(_translate("MainWindow", "SHOW"))
        self.checkBox_showtime.setText(_translate("MainWindow", "TIME "))
        self.groupBox_3.setTitle(_translate("MainWindow", "SENDING SETTING"))
        self.radioButton_sendascii.setText(_translate("MainWindow", "ASCII"))
        self.radioButton_sendhex.setText(_translate("MainWindow", "HEX"))
        self.checkBox_repeatsend.setText(_translate("MainWindow", "RESEND"))
        self.label_7.setText(_translate("MainWindow", "TIME"))
        self.btn_send.setText(_translate("MainWindow", "SEND"))
        self.btn_send_2.setText(_translate("MainWindow", "RUN"))
        self.btn_send_3.setText(_translate("MainWindow", "STOP"))
        self.comboBox_plot.setItemText(0, _translate("MainWindow", "SQUARE_PULSE"))
        self.comboBox_plot.setItemText(1, _translate("MainWindow", "TRIANGULAR_PULSE"))
        self.comboBox_plot.setItemText(2, _translate("MainWindow", "SINE_PULSE"))
        self.label_6.setText(_translate("MainWindow", "  AMPLITUDE"))
        self.label_8.setText(_translate("MainWindow", "  FREQUENCY"))
        self.comboBox_channel.setItemText(1, _translate("MainWindow", "CHANNEL1"))
        self.comboBox_channel.setItemText(0, _translate("MainWindow", "CHANNEL2"))
        self.label_9.setText(_translate("MainWindow", "          PLOT"))
        self.label_10.setText(_translate("MainWindow", "     CHANNEL"))
        self.btn_send_4.setText(_translate("MainWindow", "PLOT"))
        self.menu.setTitle(_translate("MainWindow", "EDIT"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionstart.setText(_translate("MainWindow", "START"))
        self.actionpause.setText(_translate("MainWindow", "PAUSE"))
        self.actionpause.setToolTip(_translate("MainWindow", "pauser"))
        self.actionstop.setText(_translate("MainWindow", "STOP"))
        self.actionclean.setText(_translate("MainWindow", "CLEAN"))
        self.actionCD.setText(_translate("MainWindow", "CD"))
        self.actionCHECK.setText(_translate("MainWindow", "CHECK"))
        self.actionPLOT.setText(_translate("MainWindow", "PLOT SQUARE"))
        self.actionPLOT_TRIANGULAR.setText(_translate("MainWindow", "PLOT TRIANGULAR"))
        self.actionPLOT_SINE.setText(_translate("MainWindow", "PLOT SINE"))
        self.actionadd.setText(_translate("MainWindow", "ADD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SecondMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
