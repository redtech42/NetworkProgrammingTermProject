import socket
import os 

myIP = socket.gethostbyname(socket.gethostname())
print(myIP)
serverPort = 12000

def sListen():
    serverName = myIP
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind((serverName,serverPort))
    serverSocket.listen(1)
    sData = "temp"
    print ('The server is ready to receive')
    connectionSocket, addr = serverSocket.accept()
    print ('connected ' + serverName + ":" + str(serverPort))
    while True:
        client = connectionSocket.recv(1024).decode()
        if client == "end":
            exit()
        if client == "sendFile":
            sFileName = connectionSocket.recv(1024)
            fDownloadFile = open(sFileName, "wb")
            while sData:
               fDownloadFile.write(sData)
               sData = connectionSocket.recv(1024)
               print("Download Completed")
            break
        else:
            print('Client:' + client)
            sentence = input('Server: ')
            connectionSocket.send(sentence.encode())
        
def sendFile():
    serverName = input("Enter the IP you're connecting to:")
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    print ('connected to ' + serverName + ":" + str(serverPort))
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
                print(sFileName + " Not Found On Server")
        
            else:
                print(sFileName + " File Found")
                fUploadFile = open("files/" + sFileName, "rb")
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

