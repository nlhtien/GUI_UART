import sys
from time import sleep
import serial
from PyQt5.QtWidgets import QMessageBox

class Uart(object):
    def __init__(self, port, baud):
        self.err = 0
        try:
            self.serial = serial.Serial(port, baud)
            print("Open serial success.")
        except Exception as e:
            print("Open serial error:", e)
            self.err = -1
            self.show_error_message("Failed to open serial port.")

    def show_error_message(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setText(message)
        msg_box.setWindowTitle("Error")
        msg_box.exec_()

    def send_uart_data(self, data):
        if self.err == 0:
            try:
                self.serial.write(data.encode())
            except Exception as e:
                print("Send data error:", e)
        else:
            self.show_error_message("Cannot send data. Serial port not opened.")

    def uart_close(self):
        if self.err == 0:
            self.serial.close()


if __name__ == '__main__':
    myuart = Uart("COM2", 9600)
    if myuart.err == 0:
        print("Init UART success")

        while True:
            input_data = input("Please input data (type 'quit' to exit): ")
            if input_data.lower() == "quit":
                myuart.uart_close()
                break
            else:
                myuart.send_uart_data(input_data)
                sleep(0.01)

        print('Exit!')
    else:
        print("Init UART fail!")
