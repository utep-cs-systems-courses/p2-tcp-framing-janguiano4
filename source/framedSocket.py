#Joel Anguiano
#file contains framedSocket class

class framedSocket:
    def _init_(self,connectedSocket): #This is how make an instance of the class, pass connSocket
        self.cs = connectedSocket         #this is how send messages between the client and server 

    def sendMessage(self,message):
        lengthStr = str(len(message)) + ':' #takes mess. converts to lenght# then to string
        lengthBA = bytearray(lengthStr,'utf-8') #converts lenghtStr in bytearray
        message = lengthBA + message #Concatanates bytearray with origal message
        self.cs.send(message) #sends mess. to connected socket

    def receiveMessage(self):
        msgList = [] #mess. is empty
        data = self.cs.recv(100).decode() #this is what were going to read from the sockete
        left,right = partition(data)
        msgList.append(data[left:right]) #fill data from left to right
        data = data[right:] #removes what we already read

        while(data): #keep iterating while there is still data
            left,right = partition(data)
            if len(data) < right:
                data += self.cs.recv(100).decode()
            else:
                msgList.append(data[left:right])
                data = data[right:]
        return msgList

def partition(string): #method indicates first and last character in a message
    num = ""
    while(string[0].isdigit()):
        num += string[0]
        string = string[1:]

    if num.isnumeric():
        left = len(num)+1
        right = int(num) + (len(num)+1)
        return left, right
    else:
        return None

def parse(string):
    left,right = partition(string)

    if len(string) < right:
        return None,string
    else:
        message = string[left:right]
        remainingString = string[right:]

        if remainingString == "":
            return message, remainingString
        else:
            return message, remainingString
        

        

        
