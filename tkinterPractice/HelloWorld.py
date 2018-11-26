import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.availableIP = tk.textbox(self)
        self.availableIP["text"] = "Click 'Check network' to populate the list"
        
        self.checkNetwork = tk.button(self)
        self.checkNetwork["command"] = self.check_network
        self.availableIP.pack(side="top")
        self.checkNetwork.pack(side="middle")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def check_network(self):
        self.availableIP["text"] = "You have checked the IP addresses"
        

root = tk.Tk()
app = Application(master=root)
app.mainloop()