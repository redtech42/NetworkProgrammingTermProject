from socket import *
serverName = '127.0.0.1'
serverPort = 12000
I = input("Client or Server")
if (I == "Client"):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    while True:
        sentence = input('Input: ')
        clientSocket.send(sentence.encode())
        if sentence == "end":
            exit()
        modifiedSentence = clientSocket.recv(1024).decode()
        print('From Server:' + modifiedSentence)
    
elif (I == "Server"):    
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind((serverName,serverPort))
    serverSocket.listen(1)
    print ('The server is ready to receive')
    connectionSocket, addr = serverSocket.accept()
    while True:
        client = connectionSocket.recv(1024).decode()
        if client == "end":
            exit()
        print('Client:' + client)
        sentence = input('Server: ')
        connectionSocket.send(sentence.encode())

