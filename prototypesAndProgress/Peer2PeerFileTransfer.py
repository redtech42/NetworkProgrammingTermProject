import socket
import os
import tkinter as tk
import TextWithVar

myIP = socket.gethostbyname(socket.gethostname())
print(myIP)
serverPort = 12000
    
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
        

    def create_widgets(self):

        #Each item is separated by one line, and named so finding them is idiot-proof
        
        self.receivingSide = tk.Frame(self)
        self.receivingSide.grid(row=0, column=0, sticky=tk.N, padx=10)
        self.sendingSide = tk.Frame(self)
        self.sendingSide.grid(row=0, column=2, sticky=tk.N, padx=10)
        #Receiving side of the window
        self.receivedLabel = tk.Label(self.receivingSide)
        self.receivedLabel["text"] = "Received files"
        self.receivedLabel.grid(row=0, column=0, columnspan=3, sticky=tk.N, padx=3, pady=3)

        self.fromLabel = tk.Label(self.receivingSide)
        self.fromLabel["text"] = "From:"
        self.fromLabel.grid(row=1, column=0, sticky=tk.W, padx=3, pady=3)
        
        self.fileNameLabel = tk.Label(self.receivingSide)
        self.fileNameLabel["text"] = "File name:"
        self.fileNameLabel.grid(row=2, column=0, sticky=tk.W, padx=3, pady=3)
        
        self.sourceIPString = tk.StringVar()
        self.sourceIPString.set("Source IP")
        self.sourceIPBox = TextWithVar.TextWithVar(self.receivingSide, textvariable=self.sourceIPString, height=1, width=30)
        #self.sourceIPBox.config(state='readonly')
        self.sourceIPBox.grid(row=1, column=1, columnspan=2, padx=3, pady=3)
        
        self.fileNameString = tk.StringVar()
        self.fileNameString.set("Incoming file name")
        self.fileNameBox = TextWithVar.TextWithVar(self.receivingSide, textvariable=self.fileNameString, height=1, width=30)
        #self.fileNameBox.config(state='readonly')
        self.fileNameBox.grid(row=2, column=1, columnspan=2, padx=3, pady=3)
        
        self.fileDenyButton = tk.Button(self.receivingSide)
        self.fileDenyButton["text"] = "Deny file"
       # self.fileDenyButton["command"] = self.acceptFile(False)
        self.fileDenyButton.grid(row=3, column=0,sticky=tk.W, padx=3, pady=3)
        
        self.fileAcceptButton = tk.Button(self.receivingSide)
        self.fileAcceptButton["text"] = "Listen"
        self.fileAcceptButton["command"] = self.sListen()
        self.fileAcceptButton.grid(row=3, column=2,sticky=tk.E, padx=3, pady=3)
        
        #this is to pad some space between the sending and receiving side of the window
        self.centerSpacer = tk.Label(self)
        self.centerSpacer.grid(row=0, column=1, rowspan=5, sticky=tk.N, padx=3, pady=3)
        
        
        #Sending side of the window
        self.availableUsersLabel = tk.Label(self.sendingSide)
        self.availableUsersLabel["text"] = "Available users"
        self.availableUsersLabel.grid(row=0, column=0, columnspan=3, sticky=tk.N, padx=3, pady=3)
        
        self.openUsersBox = tk.Listbox(self.sendingSide, width=30)
        self.openUsersBox.insert(1, "Press Scan to read")
        self.openUsersBox.insert(2, "available users")
        self.openUsersBox.grid(row=1, column=0, columnspan=3, rowspan=2, padx=3, pady=3)
        
        self.scanUsersButton = tk.Button(self.sendingSide)
        self.scanUsersButton["text"] = "Scan"
        #self.scanUsersButton["command"] = self.scanUsers
        self.scanUsersButton["command"] = self.displayDisconnected
        self.scanUsersButton.grid(row=3, column=0, sticky=tk.W, padx=3, pady=3)
        
        self.destIPString = tk.StringVar()
        self.destIPString.set("Destination IP")
        self.destIPBox = TextWithVar.TextWithVar(self.sendingSide, textvariable=self.destIPString, height=1, width=30)
        self.destIPBox.grid(row=3, column=1, columnspan=2, sticky=tk.E, padx=3, pady=3)
        
        self.filePathLabel = tk.Label(self.sendingSide)
        self.filePathLabel["text"] = "Sending file at:"
        self.filePathLabel.grid(row=4, column=0, sticky=tk.W, padx=3, pady=3)
        
        self.filePath = tk.StringVar()
        self.filePath.set("Enter the path of your file")
        self.filePathBox = TextWithVar.TextWithVar(self.sendingSide, textvariable=self.filePath, height=1, width=30)
        self.filePathBox.grid(row=5, column=0, columnspan=3, sticky=tk.W+tk.E, padx=3, pady=3)
        
        self.sendFileName = tk.StringVar()
        self.sendFileName.set("Enter the name of your file")
        self.sendFileNameBox = TextWithVar.TextWithVar(self.sendingSide, textvariable=self.filePath, height=1, width=30)
        self.sendFileNameBox.grid(row=6, column=0, columnspan=3, sticky=tk.W+tk.E, padx=3, pady=3)
        
        self.connectButton = tk.Button(self.sendingSide)
        self.connectButton["text"] = "Connect"
        self.connectButton["command"] = self.connectToPeer(self.destIPString)
        self.connectButton["command"] = self.displayConnected
        self.connectButton.grid(row=7, column=0, sticky=tk.W, padx=3, pady=3)
        
        self.readyButton = tk.Button(self.sendingSide)
        self.readyButton["text"] = "   "
        self.readyButton["bg"] = "red"
        self.readyButton.grid(row=7, column=1, padx=3, pady=3)
        
        self.sendButton = tk.Button(self.sendingSide)
        self.sendButton["text"] = "Send"
        self.sendButton["command"] = self.sendFileB(self.filePath, self.sendFileName, self.destIPString)
        self.sendButton["command"] = self.displayDisconnected
        self.sendButton.grid(row=7, column=2, padx=3, pady=3)
        
    def connectToPeer(self, IP):
        ip = str(IP)
        if len(ip) > 10:
            self.connectedSocket = self.connect(ip)
    def sendFileB(self, filePath, sendFileName, IP):
        if (len(str(filePath)) > 9 and len(str(sendFileName)) > 9 and len(str(IP)) > 9):
            self.sendFile(str(self.filePath), str(self.sendFileName), str(self.IP))
#    def acceptFile(self, accepting):
#        self.sourceIPString = ""
#        self.fileNameString = ""
#        if accepting:
#            self.accept(self.connectedSocket)
#        else:
#            self.deny(self.connectedSocket)
#        
#        self.displayDisconnected
        
    def displayConnected(self):
        self.readyButton.configure(bg="green")
    
    def displayDisconnected(self):
        self.readyButton.configure(bg="red")
    


#    def accept(self, conn):
#        conn.send("accepted".encode())
#        self.fileNameString = ""
#        self.sourceIPString = ""
#        while True:
#            with open('received_file', 'wb') as f:
#                print('file opened')
#                while True:
#                    print('receiving data...')
#                    data = conn.recv(1024)
#                    if data.decode() != "done":
#                        print(data)
#                    else:
#                        break
#                    # write data to a file
#                    f.write(data)
#            f.close()
#            print("successfully got the file")
#
#    def deny(self, conn):
#        conn.send("denied".encode())
#        conn.close()
#        self.fileNameString = ""
#        self.sourceIPString = ""

    def sListen(self):
        serverName = myIP
        serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        serverSocket.bind((serverName,12000))
        serverSocket.listen(5)
        print("server is listening...")
        print ('The server is ready to receive')
        conn, addr = serverSocket.accept()
        print ('connected ' + serverName + ":" + str(12000))
        self.fileNameString = conn.recv(1024).decode()
        self.sourceIPString = conn.getpeername()
#        return conn
#        self.fileNameString = ""
#        self.sourceIPString = ""
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
        

#    def connect(self, IP):
#        serverName = IP
#        print(serverName)
#        clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#        clientSocket.connect((serverName,12000))
#        print ('connected to ' + serverName + ":" + str(12000))
#        return clientSocket
             
    def sendFile(self, filePath,FileName, IP):
        serverName = IP
        print(serverName)
        clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        clientSocket.connect((serverName,12000))
        print ('connected to ' + serverName + ":" + str(12000))
        bFileFound = 0
        print(str (filePath))
        print(str (FileName))
        print(str (clientSocket))
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
 #               modifiedSentence = clientSocket.recv(1024).decode()
 #               if modifiedSentence == 'accept':
                    
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
 #               else:
 #                   clientSocket.close()
        


root = tk.Tk()
app = Application(master=root)
app.mainloop()

