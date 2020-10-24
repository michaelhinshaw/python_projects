import glob
import os
import datetime
import shutil
import tkinter
from tkinter import *
from tkinter import ttk as tk
from tkinter import filedialog

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(600, 400))
        self.master.title('Check for Modified Files')
        self.master.config(bg='lightgray')

        self.var_src = StringVar()
        self.var_dest = StringVar()

 
        self.btnBrowseSrc = Button(self.master, text="Browse Source Files", width=30, height= 2, command = self.fileDialog1)
        self.btnBrowseSrc.grid(row=2, column=1)

        self.btnBrowseDest = Button(self.master, text="Browse Destination Files", width=30, height= 2, command = self.fileDialog2)
        self.btnBrowseDest.grid(row=4, column=1)
        
        self.btnGetFile = Button(self.master, text = "Copy Files", width=30, height = 2, command = lambda: self.checkFiles())
        self.btnGetFile.grid(row=6, column=1)

        self.src_path = tk.Entry(self.master,text=self.var_src, width=50, font=("Helvetica",14))
        self.src_path.grid(row=2, column = 2)

        self.dest_path = tk.Entry(self.master,text=self.var_dest, width=50, font=("Helvetica",14))
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
                

    
                                                   


    def checkFiles(self):
        src = self.var_src.get()
        dst = self.var_dest.get()
        today = datetime.datetime.now()
        print(src)
        print(dst)
        fileList = os.listdir(src)
        print(fileList)
        for file in fileList:
            if file.endswith(".txt"):
                AbsoPath = os.path.join(src, file)
                modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(AbsoPath))
            

                filePathList = file.split("\\")
                filename = filePathList[-1]

                if today - modifyDate < datetime.timedelta(days=1):
                    shutil.copy(AbsoPath, dst)

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop


        
