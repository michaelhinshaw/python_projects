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
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(600, 400))
        self.master.title('Check for Modified Files')
        self.master.config(bg='lightgray')

 
        self.btnBrowseSrc = Button(self.master, text="Browse Source Files", width=30, height= 2, command = self.fileDialog1)
        self.btnBrowseSrc.grid(row=2, column=1)

        self.btnBrowseDest = Button(self.master, text="Browse Destination Files", width=30, height= 2, command = self.fileDialog2)
        self.btnBrowseDest.grid(row=4, column=1)
        
        self.btnGetFile = Button(self.master, text = "Copy Files", width=30, height = 2, command = self.GetFileList)
        self.btnGetFile.grid(row=6, column=1)

        self.btnCopied = Button(self.master, text="Copied Files",width=30, height = 2, command = self.copiedDialog)
        self.btnCopied.grid(row=8, column=1)

        self.src_path = tk.Entry(self.master,text=self.var_src, width=50, font=("Helvetica",14), fg="#333", bg="#fff")
        self.src_path.grid(row=2, column = 2)

        self.dest_path = tk.Entry(self.master,text=self.var_dest, width=50, font=("Helvetica",14), fg="#333", bg="#fff")
        self.dest_path.grid(row=4, column=2)

        


        

    def fileDialog1(self):
        path1 = filedialog.askdirectory()
        path1 = path1 +"/"
        self.src_path.delete(0, END)
        self.src_path.insert(END, path1)

    def fileDialog2(self):
        path2 = filedialog.askdirectory()
        path2 = path2 + "/"
        self.dest_path.delete(0, END)
        self.dest_path.insert(END, path2)
                

    def copiedDialog(self):
        self.filename = filedialog.askdirectory(initialdir = "/Users/Student/Desktop/Folder B", title = "Select a file", filetype = (("txt files", "*.txt"),("all files","*.*")))
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


        
