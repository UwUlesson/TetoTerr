import tkinter

class windows:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry("1280x800")
    pass

    def show(self):
        self.window.mainloop()
    pass

