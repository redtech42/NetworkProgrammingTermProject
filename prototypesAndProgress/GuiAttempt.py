import tkinter as tk
from TextWithVar import *

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.grid(row=0, column=0)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=1, column=0)
        """
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
        self.sourceIPBox = TextWithVar(self.receivingSide, textvariable=self.sourceIPString, height=1, width=30)
        #self.sourceIPBox.config(state='readonly')
        self.sourceIPBox.grid(row=1, column=1, columnspan=2, padx=3, pady=3)
        
        self.fileNameString = tk.StringVar()
        self.fileNameString.set("Incoming file name")
        self.fileNameBox = TextWithVar(self.receivingSide, textvariable=self.fileNameString, height=1, width=30)
        #self.fileNameBox.config(state='readonly')
        self.fileNameBox.grid(row=2, column=1, columnspan=2, padx=3, pady=3)
        
        self.fileDenyButton = tk.Button(self.receivingSide)
        self.fileDenyButton["text"] = "Deny file"
        self.fileDenyButton["command"] = self.acceptFile(False)
        self.fileDenyButton.grid(row=3, column=0,sticky=tk.W, padx=3, pady=3)
        
        self.fileAcceptButton = tk.Button(self.receivingSide)
        self.fileAcceptButton["text"] = "Accept file"
        #self.fileAcceptButton["command"] = self.acceptFile(True)
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
        self.destIPBox = TextWithVar(self.sendingSide, textvariable=self.destIPString, height=1, width=30)
        self.destIPBox.grid(row=3, column=1, columnspan=2, sticky=tk.E, padx=3, pady=3)
        
        self.filePathLabel = tk.Label(self.sendingSide)
        self.filePathLabel["text"] = "Sending file at:"
        self.filePathLabel.grid(row=4, column=0, sticky=tk.W, padx=3, pady=3)
        
        self.filePath = tk.StringVar()
        self.filePath.set("Enter the path of your file")
        self.filePathBox = TextWithVar(self.sendingSide, textvariable=self.filePath, height=1, width=30)
        self.filePathBox.grid(row=5, column=0, columnspan=3, sticky=tk.W+tk.E, padx=3, pady=3)
        
        self.sendFileName = tk.StringVar()
        self.sendFileName.set("Enter the name of your file")
        self.sendFileNameBox = TextWithVar(self.sendingSide, textvariable=self.sendFileName, height=1, width=30)
        self.sendFileNameBox.grid(row=6, column=0, columnspan=3, sticky=tk.W+tk.E, padx=3, pady=3)
        
        self.connectButton = tk.Button(self.sendingSide)
        self.connectButton["text"] = "Connect"
        #self.connectButton["command"] = self.connectToPeer
        self.connectButton["command"] = self.displayConnected
        self.connectButton.grid(row=7, column=0, sticky=tk.W, padx=3, pady=3)
        
        self.readyButton = tk.Button(self.sendingSide)
        self.readyButton["text"] = "   "
        self.readyButton["bg"] = "red"
        self.readyButton.grid(row=7, column=1, padx=3, pady=3)
        
        self.sendButton = tk.Button(self.sendingSide)
        self.sendButton["text"] = "Send"
        #self.sendButton["command"] = self.sendFile
        self.sendButton["command"] = self.displayDisconnected
        self.sendButton.grid(row=7, column=2, padx=3, pady=3)
        
        
    def acceptFile(self, accepting):
        self.sourceIPString = ""
        self.fileNameString = ""
        
    def displayConnected(self):
        self.readyButton.configure(bg="green")
    
    def displayDisconnected(self):
        self.readyButton.configure(bg="red")
        
        
    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()