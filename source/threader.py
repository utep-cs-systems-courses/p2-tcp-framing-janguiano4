#Joel Anguiano

import sys,os,socket,threading
from time import time
from threading import Thread, enumerate

threadNum  = 0
inTransfer = set()
transferLock = threading.Lock()

class Worker(Thread):
    def _init_(self,conn,addr): #creates instance of the class
        global threadNum
        Thread._init_(self, name="Thread-%d" % threadNum)
        threadNum += 1 #add +1 for the number of threads we have
        self.conn = conn #set both conn. and addr. to self
        self.addr = addr

def checkTrasnfer(self,filename): #we check if we can transfer
    global InTransfer, transferLock
    transferLock.acquire() #we acquire the lock, we lock it 
    if filename in inTransfer: #if in transfer, meaning we already have a thread = false
        canTransfer = False
    else:
        canTransfer = True #if we can add it, we add it to the set
        inTransfer.add(filename)
    transferLock.release()

    return canTransfer

def endTransfer(self,filename):
    global inTransfer
    inTransfer.remove(filename)

def run(self):
    fs = framedSocket(self.conn)
    contents = (fs.receiveMessage())
    filename = contents
    canTransfer = self.checkTransfer(filename)

    if(canTransfer):
        if os.path.isfile(filename):
            fs.sendMessage(b"NO")
            conn.shutdown(socket.SHUT_WR)
        else:
            fs.sendMessage(b"OK")

    else:
        os.write(2,("File already in Transfer").encode())
        conn.shutdown(socket.SHUT_WR)

    fd= os.open(filename, os.O_CREAT | os.O_WRONLY)
    os.write(fd,fs.receiveMessage().encode())
    os.close(fd)
    self.endTransfer(filename)
    self.conn.shutdown(socket.SHUT_WR)
