import tkinter
from auth import authenticate
from window_general import windows

class start(windows):
    def __init__(self):
        super().__init__()
        title = tkinter.Label(self.window,text="Welcome to this app\n please log in with your account",)
        title.grid(row=1,column=1)
        button = tkinter.Button(self.window,text="_Log In_",command=self.exeAuth)
        button.grid(row=2,column=1)
        self.window.grid_rowconfigure(0, weight=1)  
        self.window.grid_rowconfigure(2, weight=1)  
        self.window.grid_columnconfigure(0, weight=1) 
        self.window.grid_columnconfigure(2, weight=1)  
    def exeAuth(self):        
        auth = authenticate()
        auth.authenticate_user() 
window = start()
window.show()
