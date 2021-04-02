#Joel Anguiano
#Modified Echo-Client.py provided by Dr. Freudenthal

import socket,sys,re,time,os
sys.path.append("../lib")
import params
from read import my_getLine
from read import parseTCPInput
from framedSocket import framedSocket


switchesVarDefaults = (
    (('-s','--server'),'server',"127.0.0.1:50001"),
    (('-d','--delay'),'delay',"0"),
    (('-?','--usage'),"usage",False),
    )

progname= "framedClient"
paramMap = params.parseParams(switchesVarDefaults)

server,usage = paramMap["server"],paramMap["usage"]

if usage:
    params.usage()

try:
    serverHost,serverPort= re.split(":",server)
    serverPort = int(serverPort)
except:
    print("Can't parse server:port from '%s'" % server)
    sys.exit(1)

s = None
for res in socket.getaddrinfo(serverHost, serverPort, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        print("creating sock: af=%d, type=%d, proto=%d" % (af,socktype,proto))
        s = socket.socket(af,socktype,proto)
    except socket.error as msg:
        print("error %s" % msg)
        s.close()
        s = None
        continue
    break

if s is None:
    print("could not open socket")
    sys.exit(1)

delay = float(paramMap['delay'])
if delay != 0:
    print(f"sleeping for {delays}s")
    time.sleep(delay)
    print("done sleeping")

#above code provided by Dr.Freudenthal#
    
fs = framedSocket() #create instance of framedSocket class

input = my_getLine() #input from the user
command,localfile,host,remotefile = parseTCPInput(input) #parse input and get filename

fs.sendMessage(remotefile.encode())

reply = fs.receiveMessage()

if reply =="NO":
    OS.WRITE(2,("Failed").encode())
    sys.exit(1)

else:
    fd = os.open(localfile, os.O_RDONLY)
    buff = ""
    message = ""

    while(True):
        buff = os.read(fd,100)
        string = buff.decode()
        if len(string) == 0:
            break
        message += string

    fs.sendMessage(message.encode())
    s.close()


    
