# -*- coding: utf-8 -*-

import sys
import PyQt5.QtWidgets as qw
import PyQt5.QtCore as qc
import GUI2
from tool2 import Tool
import serial
import serial.tools.list_ports
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np




class Canvas_grafica(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(facecolor='gray')
        super().__init__(self.fig)
        self.ax.grid()
        self.ax.margins(x=0)
        self.nivel1 = 15
        self.nivel2 = 1
        self.wave_type = 'SQUARE_PULSE'  # Thêm dòng này
        self.line, = self.ax.plot([], [], color='r', linewidth=2)
        self.grafica_datos()

    def set_wave_type(self, wave_type):
        self.wave_type = wave_type
        self.grafica_datos()
    def datos1(self, valor1):
        self.nivel1 = valor1 * 0.15
        self.grafica_datos()

    def datos2(self, valor2):
        self.nivel2 = valor2 * 0.05
        self.grafica_datos()

    def grafica_datos(self):
        x = np.arange(-np.pi, 15 * np.pi, 0.01)

        if self.wave_type == 'SINE_PULSE':
            y = self.nivel1 * np.sin(self.nivel2 * x)
        elif self.wave_type == 'SQUARE_PULSE':
            y = self.nivel1 * np.sign(np.sin(self.nivel2 * x))
        elif self.wave_type == 'TRIANGULAR_PULSE':
            y = self.nivel1 *2* (1 - np.abs(np.mod(x * self.nivel2 / (np.pi), 2) - 1))
            y -= self.nivel1
        else:
            raise ValueError("Invalid waveform type")

        self.line.set_data(x, y)
        self.ax.clear()
        plt.title("Waveform")
        self.ax.plot(x, y, color='r', linewidth=2)

        # Set cứng trục y trong khoảng (-max_value, max_value)
        max_value = np.max(np.abs(y))
        self.ax.set_ylim(-15, 15)
        step = len(y) // 150
        self.segmented_y_values = [y[i:i + step].mean() for i in range(0, len(y), step)]
        self.ax.grid(True)
        self.draw()





class SecondMainWindow(qw.QMainWindow, GUI2.SecondMainWindow):
    signal_recv_data = qc.pyqtSignal(str)
    signal_recv_data1 = qc.pyqtSignal(int)
    signal_recv_data2 = qc.pyqtSignal()

    def __init__(self):
        print("Initializing SecondMainWindow")

        super().__init__()
        # ui = ui_uart_tools.Ui_MainWindow()
        self.setupUi(self)
        self.grafica = Canvas_grafica()
        self.verticalLayout_grafica.addWidget(self.grafica)
        self.setWindowTitle("My New Window ")  # Change this line
        self.slider1.valueChanged.connect(self.slider_uno)
        self.slider2.valueChanged.connect(self.slider_dos)
        # Thêm kết nối cho sự kiện valueChanged của slider1 và slider2
        self.slider1.valueChanged.connect(self.slider1_value_changed)
        self.slider2.valueChanged.connect(self.slider2_value_changed)
        self.btn_send_2.clicked.connect(self.btn_send_2_cb)
        self.btn_send_3.clicked.connect(self.btn_send_3_cb)
        self.btn_send_4.clicked.connect(self.btn_send_4_cb)
        # Thêm kết nối cho sự kiện currentIndexChanged của comboBox_plot
        self.comboBox_plot.currentIndexChanged.connect(self.comboBox_plot_cb)
        # 获取串口列表
        self.comList = list(serial.tools.list_ports.comports())
        self.portlist = []
        for com in range(0, len(self.comList)):
            self.portlist.append(self.comList[com][0])
        # 加载配置文件
        self.settings = qc.QSettings("config2.ini", qc.QSettings.IniFormat)
        self.settings.setIniCodec("UTF-8")
        self.config_uartbaud = self.settings.value("setup/UART_BAUD", 0, type=int)
        self.uart_port = self.settings.value("setup/UART_PORT")
        # print(self.config_uartbaud)
        self.statusbar.showMessage("status: NORMAL")
        self.comboBox_uart.addItems(self.portlist)
        self.radioButton_recvascii.setChecked(True)
        self.radioButton_sendascii.setChecked(True)
        self.spinBox.setRange(100, 30 * 1000)
        self.spinBox.setSingleStep(100)
        self.spinBox.setWrapping(True)
        self.spinBox.setValue(1000)
        self.comboBox_baud.setCurrentText(str(self.config_uartbaud))
        self.comboBox_uart.setCurrentText(self.uart_port)
        self.comboBox_baud.currentIndexChanged.connect(self.comboBox_baud_cb)
        self.comboBox_uart.currentIndexChanged.connect(self.comboBox_uart_cb)
        self.btn_send.clicked.connect(self.btn_send_cb)
        self.actionstart.triggered.connect(self.actionstart_cb)
        self.actionpause.triggered.connect(self.actionpause_cb)
        self.actionstop.triggered.connect(self.actionstop_cb)
        self.actionclean.triggered.connect(self.actionqingsao_cb)
        self.radioButton_recvascii.toggled.connect(self.radioButton_recvascii_cb)
        self.radioButton_sendascii.toggled.connect(self.radioButton_sendascii_cb)
        self.radioButton_sendhex.toggled.connect(self.radioButton_sendhex_cb)
        self.radioButton_recvhex.toggled.connect(self.radioButton_recvhex_cb)
        self.checkBox_autoline.toggled.connect(self.checkBox_autoline_cb)
        self.checkBox_showsend.toggled.connect(self.checkBox_showsend_cb)
        self.checkBox_showtime.toggled.connect(self.checkBox_showtime_cb)
        self.checkBox_repeatsend.toggled.connect(self.checkBox_repeatsend_cb)
        self.spinBox.valueChanged.connect(self.spinBox_cb)
        self.slider_changed_by_user = True
        self.signal_recv_data.connect(self.textBrowser_show_data_cb)
        self.tool = Tool(self.config_uartbaud,self.uart_port )

    def btn_send_3_cb(self):
        # Clear the data in textBrowser_2
        self.textBrowser.clear()

    def btn_send_4_cb(self):
        # Access the segmented_y_values from Canvas_grafica instance
        segmented_y_values = self.grafica.segmented_y_values

        # Concatenate the segmented values into a single string
        result_string = " ".join([f" {val:.2f}" for i, val in enumerate(segmented_y_values)])

        # Append the concatenated string to textBrowser without new lines
        self.textBrowser.append(result_string)

    def comboBox_plot_cb(self, index):
        # Lấy giá trị được chọn từ comboBox_plot
        selected_wave = self.comboBox_plot.currentText().upper()

        # Gọi phương thức set_wave_type của đối tượng Canvas_grafica
        self.grafica.set_wave_type(selected_wave)

    def btn_send_2_cb(self):
        amp_text = self.AMP.toPlainText()
        freq_text = self.FREQ.toPlainText()

        print(f"AMP Text: {amp_text}, FREQ Text: {freq_text}")

        # Chuyển đổi văn bản thành số và cập nhật giá trị của slider1 và slider2
        try:
            amp_value = float(amp_text)
            freq_value = float(freq_text)

            # Tắt cờ (flag) để ngăn chặn sự kiện slider_changed_by_user
            self.slider_changed_by_user = False

            # Cập nhật giá trị của slider1 và slider2
            self.slider1.setValue(int(amp_value / 0.15))
            self.slider2.setValue(int(freq_value / 8))
        except ValueError:
            # Xử lý ngoại lệ nếu văn bản không thể chuyển đổi thành số
            print("Invalid input. Please enter numeric values for AMP and FREQ.")
        finally:
            # Bật lại cờ (flag) để sẵn sàng cho sự kiện slider_changed_by_user
            self.slider_changed_by_user = True

    def slider1_value_changed(self, value):
        if self.slider_changed_by_user:
            self.AMP.setPlainText(str(value*0.15))

            # Đảm bảo không kích hoạt sự kiện khi thay đổi giá trị từ mã
            self.slider1.blockSignals(True)
            self.slider1.setValue(value)
            self.slider1.blockSignals(False)

    def slider2_value_changed(self, value):
        if self.slider_changed_by_user:
            self.FREQ.setPlainText(str(value*8))

            # Đảm bảo không kích hoạt sự kiện khi thay đổi giá trị từ mã
            self.slider2.blockSignals(True)
            self.slider2.setValue(value)
            self.slider2.blockSignals(False)
    def textBrowser_show_data_cb(self, data):
        self.textBrowser.insertPlainText(data)
        cursor = self.textBrowser.textCursor().End
        self.textBrowser.moveCursor(cursor)
    def slider_uno(self, event):
        self.grafica.datos1(event)


    def slider_dos(self, event):
        self.grafica.datos2(event)
    def comboBox_baud_cb(self):
        content = self.comboBox_baud.currentText()
        text = f"You currently have selected {content}"
        qw.QMessageBox.information(self, "baudrate", text, qw.QMessageBox.Ok | qw.QMessageBox.Cancel)

    def comboBox_uart_cb(self):
        content = self.comboBox_uart.currentText()
        self.settings.setValue("setup/UART_PORT", content)

    def btn_send_cb(self):
        # print("you click btn_send")
        send_data = self.textEdit_get.toPlainText()
        self.tool.uart.send_uart_data(send_data)

    def actionstart_cb(self):
        pass

    def actionpause_cb(self):
        pass

    def actionstop_cb(self):
        pass

    def actionqingsao_cb(self):
        self.textBrowser.clear()
        self.textEdit_get.clear()
        self.textBrowser_2.clear()
        self.slider1.setValue(0)
        self.slider2.setValue(0)
        pass

    def radioButton_recvascii_cb(self):
        pass

    def radioButton_sendascii_cb(self):
        pass

    def radioButton_recvhex_cb(self):
        pass

    def radioButton_sendhex_cb(self):
        pass

    def checkBox_autoline_cb(self):
        res_auto_line = self.checkBox_autoline.isChecked()
        print("res_auto_line is ", res_auto_line)
        res_show_send = self.checkBox_showsend.isChecked()
        print("res_show_send is ", res_show_send)
        res_show_time = self.checkBox_showtime.isChecked()
        print("res_show_time is ", res_show_time)
        res_repeat_send = self.checkBox_repeatsend.isChecked()
        print("res_repeat_send is ", res_repeat_send)

    def checkBox_showsend_cb(self):
        pass

    def checkBox_showtime_cb(self):
        pass

    def checkBox_repeatsend_cb(self):
        pass

    def spinBox_cb(self, value):
        # res_spinbox=self.spinBox.value()
        print("spinbox value is:", value)


if __name__ == '__main__':
    app2 = qw.QApplication(sys.argv)
    print(sys.argv)
    w = SecondMainWindow()
    w.show()
    sys.exit(app2.exec_())
