# Trong file tool.py
from uart_operate import Uart

class Tool(object):
    def __init__(self, parent, uart_port, uart_baud):
        self.err = 0
        self.parent = parent
        print("Tool start...")
        self.uart = Uart(uart_port, uart_baud)

    def update_uart_settings(self, port, baud_rate):
        self.uart = Uart(port, baud_rate)
