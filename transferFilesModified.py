import glob
import os
import datetime
import shutil
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(600, 400))
        self.master.title('Check for Modified Files')
        self.master.config(bg='lightgray')
        

        self.labelFrame = ttk.LabelFrame(self, text = "Open File")
        self.labelFrame.grid(column = 0, row = 1, padx = (20, 0), pady = (0, 20))

        self.button()
        

    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Browse files", command = self.fileDialog)
        self.button.grid(column = 1, row = 1)

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir = "/Users/Student/Desktop/Folder A", title = "Select a file", filetype= (("txt files", "*.txt"),("all files","*.*")))
        self.label = ttk.Label(self.labelFrame, text = "")
        self.label.grid(column = 1, row = 2)
        self.label.configure(text = self.filename)
                        
                                                   

def GetFileList(path, type):
    '''
    return a list of filename matching the given path and file type
    '''
    return glob.glob(path + "*" + type)

originPath = '/Users/Student/Desktop/Folder B/'
destinationPath ='/Users/Student/Desktop/Folder A/'
fileType= ".txt"

fileList = GetFileList(originPath, fileType)

for file in fileList:
    modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(file))
    todaysDate = datetime.datetime.today()

    filePathList = file.split("\\")
    filename = filePathList[-1]

    modifyDateLimit = modifyDate + datetime.timedelta(days=1)

    if modifyDateLimit > todaysDate:
        shutil.copy2(file, destinationPath + filename)

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop


        
