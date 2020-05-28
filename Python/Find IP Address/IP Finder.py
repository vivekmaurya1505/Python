## importing Socket module
import socket
##getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting IP Address using socket.gethostbyname() mehod
ip_address = socket.gethostbyname(hostname)

print(f"Hostname: {hostname}")
print(f"Ip Address: {ip_address}")
