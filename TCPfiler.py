import socket
import os
import sys

myIP = socket.gethostbyname(socket.gethostname())
print(myIP)
serverPort = 12000

def accept(conn):
    conn.send("accept".encode())
    while True:
        with open('received_file', 'wb') as f:
            print('file opened')
            while True:
                print('receiving data...')
                data = conn.recv(1024)
                if data.decode() != "done":
                    print(data)
                else:
                    break
                # write data to a file
                f.write(data)
        f.close()
        print("successfully got the file")

def deny(conn):
    conn.send("deny".encode())
    conn.close()

def sListen():
    serverName = myIP
    serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serverSocket.bind((serverName,12000))
    serverSocket.listen(5)
    print("serve is listening...")
    print ('The server is ready to receive')
    conn, addr = serverSocket.accept()
    print ('connected ' + serverName + ":" + str(12000))
    incommingFile = conn.recv(1024).decode()
    return conn, incommingFile
    

def connect(IP):
    serverName = IP
    clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    clientSocket.connect((serverName,12000))
    print ('connected to ' + serverName + ":" + str(12000))
    return clientSocket
         
def sendFile(filePath,FileName,clientSocket):
    bFileFound = 0
    
    while True:
        fileP = filePath
        sFileName = FileName
        
        for file in os.listdir(fileP):
            if file == sFileName:
                bFileFound = 1
                break 
                
        if bFileFound == 0:
            print(sFileName + " Not Found in Directory")
        else:
            clientSocket.send(FileName.encode())
            modifiedSentence = clientSocket.recv(1024).decode()
            if modifiedSentence == 'accept':
                
                print(fileP + "/" + sFileName + " File Found")
                fUploadFile = open(sFileName, "rb")
                sRead = fUploadFile.read(1024)
                count = 1
                while sRead:
                    print(count)
                    clientSocket.send(sRead)
                    sRead = fUploadFile.read(1024)
                    count += 1
                print("Sending Completed")
                clientSocket.send("done".encode())
                clientSocket.close()
            else:
                clientSocket.close()
    

I = input("Send File or Receive File: ")
if (I.lower() == "send file"):
    sendFile(filePath, fileName, self.connect(IP))
    
elif (I.lower() == "receive file"):    
    sListen()

