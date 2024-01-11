import socket

# Thông số kết nối
server_ip = '192.168.230.138'  # Địa chỉ IP của Raspberry Pi
server_port = 12346  # Cổng kết nối trên Raspberry Pi

# Tạo socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Kết nối socket đến địa chỉ và cổng của Raspberry Pi
    server_socket.connect((server_ip, server_port))
    print(f"Connected to {server_ip}:{server_port}")

    # Gửi một ký tự qua socket
    message = 'HELLO TIEN'  # Thay đổi thành ký tự bạn muốn gửi
    server_socket.send(message.encode())

    print("Data sent successfully.")

except socket.error as e:
    print(f"Error: Unable to connect to {server_ip}:{server_port}")
    print(f"Exception: {e}")

finally:
    # Đóng kết nối khi không cần thiết
    server_socket.close()
    print("Socket connection closed.")
