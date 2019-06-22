from tkinter import * 
from tkinter import scrolledtext
from tkinter import filedialog

def resize_img():
    size = 500, 500 #Thumbnail size
    #makes thumbnail of input.png, which makes it resize correctly for this. input.thumbnail only used for GUI
    for infile in glob.glob("*.png"):
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        im.thumbnail(size)
        im.save(file + ".thumbnail", "PNG")

class GUI:
    def __init__(self, master):
        resize_img()
        self.master = master
        master.title("Easy Git")

        
root = Tk()
root.geometry("925x510") #GUI start size
my_gui = GUI(root)
root.mainloop()
