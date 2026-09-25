import socket
import platform
import getpass

print("Informasi Sistem")
print("HostName : ", socket.gethostname())
print("Ip lokal : ", socket.gethostbyname(socket.gethostbyname))
print("OS       : ", platform.system(), platform.release())
print("python ver : ", platform.python_version())
print("user     : ", getpass.getuser())