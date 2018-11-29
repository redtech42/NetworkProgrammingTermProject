import socket
import os 

myIP = socket.gethostbyname(socket.gethostname())
print(myIP)
serverPort = 12000

def sListen():
    serverName = myIP
    serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serverSocket.bind((serverName,serverPort))
    serverSocket.listen(1)
    print ('The server is ready to receive')
    connectionSocket, addr = serverSocket.accept()
    print ('connected ' + serverName + ":" + str(serverPort))
    while True:
        client = connectionSocket.recv(1024).decode()
        if client == "end":
            serverSocket.close()
        print('Client:' + client)
        sentence = input('Server: ')
        connectionSocket.send(sentence.encode())
        
def sendFile():
    serverName = input("Enter the IP you're connecting to:")
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    print ('connected to ' + serverName + ":" + str(serverPort))
    while True:
        sentence = input('Input: ')
        clientSocket.send(sentence.encode())
        if sentence == "end":
            clientSocket.close()
        modifiedSentence = clientSocket.recv(1024).decode()
        print('From Server:' + modifiedSentence)
       
        
I = input("Client or Server")
if (I == "Client"):
    sendFile()
    
elif (I == "Server"):    
    sListen()

