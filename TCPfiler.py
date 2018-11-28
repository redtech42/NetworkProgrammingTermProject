import socket
import os
import sys

myIP = socket.gethostbyname(socket.gethostname())
print(myIP)
serverPort = 12000

def sListen():
    serverName = myIP
    serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serverSocket.bind((serverName,serverPort))
    serverSocket.listen(5)
    print("serve is listening...")
    
    print ('The server is ready to receive')
    conn, addr = serverSocket.accept()
    print ('connected ' + serverName + ":" + str(serverPort))
    while True:
        client = conn.recv(1024).decode()
        if client == "end":
            exit()
        if client == "sendFile":
            with open('received_file', 'wb') as f:
                print('file opened')
                while True:
                    print('receiving data...')
                    data = conn.recv(1024)
                    print(data)
                    if not data:
                        break
                    # write data to a file
                    f.write(data)
            f.close()
            print("successfully get the file")
        else:
            print('Client:' + client)
            sentence = input('Server: ')
            conn.send(sentence.encode())
        
def sendFile():
    serverName = input("Enter the IP you're connecting to:")
    clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    print ('connected to ' + serverName + ":" + str(serverPort))
    bFileFound = 0
    
    while True:
        sentence = input('Input: ')
        clientSocket.send(sentence.encode())
        if sentence == "end":
            sendFile().close
        elif sentence == "sendFile":
            fileP = input("enter file path")
            sFileName = input("enter file name")
            
            for file in os.listdir(fileP):
                if file == sFileName:
                    bFileFound = 1
                    break
        
            if bFileFound == 0:
                print(sFileName + " Not Found in Directory")
        
            else:
                print(sFileName + " File Found")
                fUploadFile = open("/"+sFileName, "rb")
                sRead = fUploadFile.read(1024)
                while sRead:
                    clientSocket.send(sRead)
                    sRead = fUploadFile.read(1024)
                print("Sending Completed")

        modifiedSentence = clientSocket.recv(1024).decode()
        print('From Server:' + modifiedSentence)
    

I = input("Client or Server")
if (I == "Client"):
    sendFile()
    
elif (I == "Server"):    
    sListen()

