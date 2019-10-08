### Python 1 - Verifikasi telnet dan menambahkan ip address pada interface loopback
#inport librari python
import getpass
import sys
import telnetlib

#Definisi ip host, buat variabel user dan password
HOST = "192.168.122.191"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

#perintah telnet dari librari telnetlib
tn = telnetlib.Telnet(HOST)

#proses saat telnet
tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

#Masukkan config yang akan di eksekusi
tn.write("enable\n")
tn.write("cisco\n")
tn.write("conf t\n")
tn.write("int loop 0\n")
tn.write("ip address 1.1.1.1 255.255.255.255\n")
tn.write("int loop 1\n")
tn.write("ip address 2.2.2.2 255.255.255.255\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()

