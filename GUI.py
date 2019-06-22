from tkinter import * 
from tkinter import scrolledtext
from tkinter import filedialog

class GUI:
    def __init__(self, master):
        resize_img()
        self.master = master
        master.title("Easy Git")

        
root = Tk()
root.geometry("925x510") #GUI start size
my_gui = GUI(root)
root.mainloop()
