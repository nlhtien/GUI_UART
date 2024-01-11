# -*- coding: utf-8 -*-
import binascii
import sys
import PyQt5.QtWidgets as qw
import PyQt5.QtCore as qc
from PyQt5.QtCore import QThread,QTimer
import GUI3
from tool2 import Tool
import serial
import serial.tools.list_ports
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from PyQt5.QtSerialPort import QSerialPort
from PyQt5.QtWidgets import QMessageBox

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
class myMainwindow(qw.QMainWindow, GUI3.SecondMainWindow):
    def __init__(self):
        super().__init__()
        # ui = ui_uart_tools.Ui_MainWindow()
        self.setupUi(self)
        self.grafica = Canvas_grafica()
        self.verticalLayout_grafica.addWidget(self.grafica)
        self.slider1.valueChanged.connect(self.slider_uno)
        self.slider2.valueChanged.connect(self.slider_dos)
        self.setWindowTitle("My New Window ")  # Change this line
        self.uart_connected = False
        # Thêm kết nối cho sự kiện valueChanged của slider1 và slider2
        self.slider1.valueChanged.connect(self.slider1_value_changed)
        self.slider2.valueChanged.connect(self.slider2_value_changed)
        self.btn_send_2.clicked.connect(self.btn_send_2_cb)
        self.btn_send_3.clicked.connect(self.btn_send_3_cb)
        self.btn_send_4.clicked.connect(self.btn_send_4_cb)
        self.btn_send_4.clicked.connect(self.btn_send_5_cb)
        self.btn_send_4.clicked.connect(self.btn_send_6_cb)
        # Thêm kết nối cho sự kiện currentIndexChanged của comboBox_plot
        self.comboBox_plot.currentIndexChanged.connect(self.comboBox_plot_cb)
        #CHECK SERIAL CONNECT
        self.serial_port = QSerialPort(self)
        self.serial_port.errorOccurred.connect(self.handle_serial_error)
        #UART
        self.comList = list(serial.tools.list_ports.comports())
        self.portlist = []
        for com in range(0, len(self.comList)):
            self.portlist.append(self.comList[com][0])
        # CONFIG SETTING
        self.settings = qc.QSettings("config.ini", qc.QSettings.IniFormat)
        self.settings.setIniCodec("UTF-8")
        self.config_uartbaud = self.settings.value("setup/UART_BAUD", 0, type=int)
        self.uart_port = self.settings.value("setup/UART_PORT")
        # print(self.config_uartbaud)
        self.statusbar.showMessage("status: INIT 2")
        self.comboBox_uart.addItems(self.portlist)
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
        self.actionclean.triggered.connect(self.actionclean_cb)
        self.radioButton_sendascii.toggled.connect(self.radioButton_sendascii_cb)
        self.radioButton_sendhex.toggled.connect(self.radioButton_sendhex_cb)


        self.spinBox.valueChanged.connect(self.spinBox_cb)
        self.slider_changed_by_user = True
        self.tool = Tool(self, self.uart_port, self.config_uartbaud)
        # Connect the actionadd to the function that opens the second GUI
        self.actionadd.triggered.connect(self.open_second_window)
        # Khởi tạo QTimer
        self.auto_send_timer = QTimer(self)
        self.auto_send_timer.timeout.connect(self.auto_send_data)
        self.checkBox_repeatsend.toggled.connect(self.checkBox_repeatsend_cb)

    def open_second_window(self):
        # Start the thread for the second GUI
        self.second_window_thread.start()
        # Tạo một đối tượng thời gian với thời điểm hiện tại
        current_time = datetime.now()
        # Chuyển đổi thời gian thành chuỗi với định dạng mong muốn
        time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
        # Tạo chuỗi thông báo mới có thêm thông tin thời gian
        message = f"{time_str}: ADD A NEW WINDOW!"
        # Hiển thị thông báo trong textBrowser_2
        self.textBrowser_2.append(message)
    def handle_serial_error(self, error):
        print("Serial Error:", error)
        if error == QSerialPort.ResourceError:
            # Handle the resource error (e.g., disconnected)
            self.handle_uart_disconnected()

    def handle_uart_disconnected(self):
        print("UART Disconnected")

        # Handle when UART is not connected
        self.uart_connected = False
        self.statusbar.showMessage("UART disconnected")
        QMessageBox.critical(self, "UART Disconnected", "The UART connection has been lost.", QMessageBox.Ok)

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

    def btn_send_5_cb(self):
        pass
    def btn_send_6_cb(self):
        pass
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
        self.settings.setValue("setup/UART_BAUD", content)
        try:
            baud_value = int(content)
            self.config_uartbaud = baud_value
            self.tool.update_uart_settings(self.uart_port, self.config_uartbaud)
        except ValueError:
            print("Invalid baud rate.")
        text = f"You currently have selected {content}"
        qw.QMessageBox.information(self, "baudrate", text, qw.QMessageBox.Ok | qw.QMessageBox.Cancel)

    def comboBox_uart_cb(self):
        content = self.comboBox_uart.currentText()
        self.settings.setValue("setup/UART_PORT", content)

        self.uart_port = content
        self.tool.update_uart_settings(self.uart_port, self.config_uartbaud)

    def btn_send_cb(self):

        if self.uart_connected:
            send_data = self.textEdit_get.toPlainText()
            # Tạo một đối tượng thời gian với thời điểm hiện tại
            current_time = datetime.now()
            # Chuyển đổi thời gian thành chuỗi với định dạng mong muốn
            time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
            # Tạo chuỗi thông báo mới có thêm thông tin thời gian
            message = f"{time_str}: turn on send"
            # Hiển thị thông báo trong textBrowser_2
            self.textBrowser_2.append(message)

            if self.radioButton_sendascii.isChecked():
                # Chuyển đổi văn bản sang mã ASCII
                ascii_data = binascii.hexlify(send_data.encode('utf-8')).decode('utf-8')
                # Tạo một đối tượng thời gian với thời điểm hiện tại
                current_time = datetime.now()
                # Chuyển đổi thời gian thành chuỗi với định dạng mong muốn
                time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
                # Tạo chuỗi thông báo mới có thêm thông tin thời gian
                message = f"{time_str}: ascii - {ascii_data}"
                # Hiển thị thông báo trong textBrowser_2
                self.textBrowser_2.append(message)
                self.tool.uart.send_uart_data(ascii_data)
            elif self.radioButton_sendhex.isChecked():
                # Chuyển đổi văn bản sang mã HEX
                try:
                    hex_data = binascii.unhexlify(send_data.encode('utf-8')).decode('utf-8')
                    # Tạo một đối tượng thời gian với thời điểm hiện tại
                    current_time = datetime.now()
                    # Chuyển đổi thời gian thành chuỗi với định dạng mong muốn
                    time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
                    # Tạo chuỗi thông báo mới có thêm thông tin thời gian
                    message = f"{time_str}: hex - {hex_data}"
                    # Hiển thị thông báo trong textBrowser_2
                    self.textBrowser_2.append(message)
                    self.tool.uart.send_uart_data(hex_data)
                except binascii.Error:
                    # Tạo một đối tượng thời gian với thời điểm hiện tại
                    current_time = datetime.now()
                    # Chuyển đổi thời gian thành chuỗi với định dạng mong muốn
                    time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
                    # Tạo chuỗi thông báo mới có thêm thông tin thời gian
                    message = f"{time_str}: Invalid hex input."
                    # Hiển thị thông báo trong textBrowser_2
                    self.textBrowser_2.append(message)
            else:
                # Trường hợp khác, gửi dữ liệu như bình thường
                # Tạo một đối tượng thời gian với thời điểm hiện tại
                current_time = datetime.now()
                # Chuyển đổi thời gian thành chuỗi với định dạng mong muốn
                time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
                # Tạo chuỗi thông báo mới có thêm thông tin thời gian
                message = f"{time_str}: string - {send_data}"
                # Hiển thị thông báo trong textBrowser_2
                self.textBrowser_2.append(message)
                self.tool.uart.send_uart_data(send_data)
        else:
            # Tạo một đối tượng thời gian với thời điểm hiện tại
            current_time = datetime.now()
            # Chuyển đổi thời gian thành chuỗi với định dạng mong muốn
            time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
            # Tạo chuỗi thông báo mới có thêm thông tin thời gian
            message = f"{time_str}: turn off send"
            # Hiển thị thông báo trong textBrowser_2
            self.textBrowser_2.append(message)

    def actionstart_cb(self):
        # Bắt đầu kết nối UART ở đây
        self.uart_connected = True
        # Hiển thị trạng thái kết nối
        self.statusbar.showMessage("UART connected")


    def actionpause_cb(self):
        # Tạm dừng kết nối UART ở đây
        self.uart_connected = False
        # Hiển thị trạng thái tạm dừng
        self.statusbar.showMessage("UART paused")
        text = f"PRESENT PROGRAMMING IS PAUSE"
        qw.QMessageBox.information(self, "WARNING", text, qw.QMessageBox.Ok | qw.QMessageBox.Cancel)

    def actionstop_cb(self):
        # Dừng kết nối UART ở đây
        self.uart_connected = False
        # Hiển thị trạng thái dừng
        self.statusbar.showMessage("UART stopped")
        self.close()

    def actionclean_cb(self):
        self.textBrowser.clear()
        self.textEdit_get.clear()
        self.textBrowser_2.clear()
        self.slider1.setValue(0)
        self.slider2.setValue(0)



    def radioButton_sendascii_cb(self):
        pass

    def radioButton_sendhex_cb(self):
        pass

    def auto_send_data(self):

        # Kiểm tra xem chương trình có đang trong trạng thái kết nối không
        if self.uart_connected:
            # Kiểm tra trạng thái kết nối UART trước khi gửi dữ liệu tự động
            send_data = self.textEdit_get.toPlainText()
            # Tạo một đối tượng thời gian với thời điểm hiện tại
            current_time = datetime.now()
            # Chuyển đổi thời gian thành chuỗi với định dạng mong muốn
            time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
            # Tạo chuỗi thông báo mới có thêm thông tin thời gian
            message = f"{time_str}: turn on auto repeat"
            # Hiển thị thông báo trong textBrowser_2
            self.textBrowser_2.append(message)

            if self.radioButton_sendascii.isChecked():
                # Chuyển đổi văn bản sang mã ASCII
                ascii_data = binascii.hexlify(send_data.encode('utf-8')).decode('utf-8')
                print(ascii_data)
                self.tool.uart.send_uart_data(ascii_data)
            elif self.radioButton_sendhex.isChecked():
                # Chuyển đổi văn bản sang mã HEX
                try:
                    hex_data = binascii.unhexlify(send_data.encode('utf-8')).decode('utf-8')
                    print(hex_data)
                    self.tool.uart.send_uart_data(hex_data)
                except binascii.Error:
                    print("Invalid hex input.")
            else:
                # Trường hợp khác, gửi dữ liệu như bình thường
                print(send_data)
                self.tool.uart.send_uart_data(send_data)
        else:
            # Tạo một đối tượng thời gian với thời điểm hiện tại
            current_time = datetime.now()
            # Chuyển đổi thời gian thành chuỗi với định dạng mong muốn
            time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
            # Tạo chuỗi thông báo mới có thêm thông tin thời gian
            message = f"{time_str}: turn off auto repeat"
            # Hiển thị thông báo trong textBrowser_2
            self.textBrowser_2.append(message)

    def checkBox_repeatsend_cb(self,state):
        if state:  # Nếu checkBox_repeatsend được chọn
            interval = self.spinBox.value()  # Lấy giá trị từ spinBox
            self.auto_send_timer.start(interval)  # Bắt đầu bộ hẹn giờ
        else:
            self.auto_send_timer.stop()  # Dừng bộ hẹn giờ khi checkBox_repeatsend không được chọn

    def show_uart_disconnected_message(self):
        # Tạo một đối tượng thời gian với thời điểm hiện tại
        current_time = datetime.now()
        # Chuyển đổi thời gian thành chuỗi với định dạng mong muốn
        time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
        # Tạo chuỗi thông báo mới có thêm thông tin thời gian
        message = f"{time_str}: UART is not connected."
        # Hiển thị thông báo trong textBrowser_2
        self.textBrowser_2.append(message)
    def spinBox_cb(self, value):
        # res_spinbox=self.spinBox.value()
        print("spinbox value is:", value)


if __name__ == '__main__':
    app1 = qw.QApplication(sys.argv)
    print(sys.argv)
    w = myMainwindow()
    w.show()
    sys.exit(app1.exec_())