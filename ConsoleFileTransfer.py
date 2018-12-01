import socket
import os
import sys

#get IP for connecting
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
            sendFile.close()
        if client == "sendFile":
    
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
            sendFile().close()
        #Send file activation
        elif sentence == "sendFile":
            fileP = input("enter file path")
            sFileName = input("enter file name")
            sentence = sFileName
            clientSocket.send(sentence.encode())
            
            for file in os.listdir(fileP):
                if file == sFileName:
                    bFileFound = 1
                    break
            #if file not found
            if bFileFound == 0:
                print(sFileName + " Not Found in Directory")
            #if file found
            else:
                print(sFileName + " File Found")
                fUploadFile = open(fileP + "/" +sFileName, "rb")
                sRead = fUploadFile.read(1024)
                count = 1
                while sRead:
                    print(count)
                    clientSocket.send(sRead)
                    sRead = fUploadFile.read(1024)
                    count += 1
                print("Sending Completed")
                clientSocket.send("done".encode())

        modifiedSentence = clientSocket.recv(1024).decode()
        print('From Server:' + modifiedSentence)
    
#Main Body
I = input("Send File or Receive File:")
if (I.lower() == "send file"):
    sendFile()
    
elif (I.lower() == "receive file"):    
    sListen()

