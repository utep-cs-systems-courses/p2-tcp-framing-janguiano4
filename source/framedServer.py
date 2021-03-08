import socket, sys, re, time, os
sys.path.append("../lib")
import params
from framedSocket import framedSocket


switchesVarDefaults = (
    (('-l','--listenPort'), 'listenPort', 50001),
    (('-?' ,'--usage'),"usage",False),
    )

progname = "echoserver"
paramMap = paramMap = params.parseParams(switchesVarDefaults)

listenPort = paramMap['listenPort']
listenAddr = ''

if paramMap['usage']:
    params.usage()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((listenAddr, listenPort))
s.listen(1)

####################################################
while True:
    conn,addr = s.accept()
    fs = framdedSocket(conn)
    if os.fork()==0:
        print("Connected by", addr)
        contents = fs.receiveMessage()

        filename = contents

        if os.path.isfile(filename):
            fs.sendMessage(b"NO")
            conn.shutdown(socket.SHUT_WR)
        else:
            fs.sendMesaage(b"ok")

        fd = os.open(filename, os.O_CREAT | os.O_WRONLY)
        os.write(fd,fs.receiveMessage().encode())
        os.close(fd)
        


     
    
