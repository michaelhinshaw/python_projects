import webbrowser
import os
import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Python Create HTML')
        self.master.config(bg='lightgray')

        self.varBodyText = StringVar()

        self.lblBodyText = Label(self.master,text ='Your Text', font=("Helvetica", 16), fg="black", bg="lightgray")
        self.lblBodyText.grid(row=0,column=0,padx=(30,0),pady=(30,0))


        self.lblDisplay = Label(self.master,text = '', font=("Helvetica", 16), fg="black", bg="lightblue")
        self.lblDisplay.grid(row=3, column=1,padx=(30,0),pady=(30,0))
        self.txtBodyText = Entry(self.master,text=self.varBodyText, font=("Helvetica", 16), fg="black", bg="lightblue")
        self.txtBodyText.grid(row=0, column=1,padx=(30,0),pady=(30,0))


        self.btnSubmit = Button(self.master, text="Submit", width=10, height = 2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady =(30,0), sticky=N+E)

    def writeBody(self):
         bT = self.varBodyText.get()
         self.lblDisplay.config(text = 'Your New Content is {}'.format(bT))


print()
f = open('helloworld.html', 'w')

message = """<html>
<body>
Stay tuned for our amazing summer sale!
</body>
</html>"""

f.write(message)
f.close()

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop

filename = 'file:///'+os.getcwd()+'/' + 'helloworld.html'
webbrowser.open_new_tab(filename)
