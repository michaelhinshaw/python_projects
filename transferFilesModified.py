import glob
import os
import datetime
import shutil
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__ (self,master)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(600, 400))
        self.master.title('Check for Modified Files')
        self.master.config(bg='lightgray')
        

        self.lbl = Label(self, text = "Open File", font=("Helvetica", 16), fg="black", bg="lightblue")
        self.lbl.grid(column = 0, row = 1, padx = (20, 0), pady = (0, 20))

        self.btnBrowse = Button(self.master, text="Browse Files", width=30, height= 2, command = self.fileDialog)
        self.btnBrowse.grid(row=2, column=1)
        
        self.btnGetFile = Button(self.master, text = "Copy Files", width=30, height = 2, command = self.GetFileList)
        self.btnGetFile.grid(row=3, column=1)

        self.btnCopied = Button(self.master, text="Copied Files",width=30, height = 2, command = self.copiedDialog)
        self.btnCopied.grid(row=4, column=1)

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir = "/Users/Student/Desktop/Folder A", title = "Select a file", filetype= (("txt files", "*.txt"),("all files","*.*")))
        self.label = Label(self.label, text = "")
        self.label.grid(column = 1, row = 2)
        self.label.configure(text = self.filename)

    def copiedDialog(self):
        self.filename = filedialog.askopenfilename(initialdir = "/Users/Student/Desktop/Folder B", title = "Select a file", filetype = (("txt files", "*.txt"),("all files","*.*")))
        self.label2 = Label(self.label, text = "")
        self.label2.grid(column = 2, row = 2)
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


        
