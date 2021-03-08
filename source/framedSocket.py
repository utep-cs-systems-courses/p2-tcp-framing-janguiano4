class framedSocket:
    def _init_(self,connectedSocket):
        self.cs = connectedSocket

    def sendMessage(self,message):
        lengthStr = str(len(message)) + ':'
        lengthBA = bytearray(lengthStr,'utf-8')
        message = lengthBA + message
        self.cs.send(message)

    def receiveMessage(self):
        msgList = []
        data = self.cs.recv(100).decode()
        left,right = partition(data)
        msgList.append(data[left:right])
        data = data[right:]

        while(data):
            left,right = partition(data)
            if len(data) < right:
                data += self.cs.recv(100).decode()
            else:
                msgList.append(data[left:right])
                data = data[right:]
        return msgList

def partition(string):
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
        

        

        
