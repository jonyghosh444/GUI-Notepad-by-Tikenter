# Hare Krishna
from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x600')
    root.title('Notepad by Jony')
    root.wm_iconbitmap('logo.ico')

    # Function
    def newFile():
        global file
        root.title('Untitled - Notepad')
        file = None
        textArea.delete(1.0, END)

    def openFile():
        global file
        file = askopenfilename(defaultextension=".txt", filetypes=[("ALL Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            root.title(os.path.basename(file) + " - Notepad by Jony")
            textArea.delete(1.0, END)
            f = open(file, "r")
            textArea.insert(1.0, f.read())
            f.close()

    def saveFile():
        global file
        if file is None:
            file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
            if file == "":
                file = None
            else:
                f = open(file, "w")
                f.write(textArea.get(1.0, END))
                f.close()

                root.title(os.path.basename(file) + "- Notepad by Jony")
                print("File saved.")
        else:
            f = open(file, "w")
            f.write(textArea.get(1.0, END))
            f.close()

    def cut():
        textArea.event_generate("<<Cut>>")

    def copy():
        textArea.event_generate("<<Copy>>")

    def paste():
        textArea.event_generate("<<Paste>>")

    def about():
        tmsg.showinfo('About Notepade by Jony', "It's a Notepad developed by Jony Ghosh.")

    def forHelp():
        tmsg.showinfo('Help', "For any help contact with developer Jony Ghosh.")

    # Add text area
    textArea = Text(root, font='arial 15')
    textArea.pack(expand=True, fill=BOTH)
    file = None

    # scroll bar
    Scroll = Scrollbar(textArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=textArea.yview)
    textArea.config(yscrollcommand=Scroll.set)

    # Menu bar
    menuBar = Menu(root)
    fileMenu = Menu(menuBar, tearoff=0)
    fileMenu.add_command(label='New', command=newFile)
    fileMenu.add_command(label='Open', command=openFile)
    fileMenu.add_command(label='Save', command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label='Exit', command=quit)
    menuBar.add_cascade(label='File', menu=fileMenu)

    editMenu = Menu(menuBar, tearoff=0)
    editMenu.add_command(label='Cut', command=cut)
    editMenu.add_command(label='Copy', command=copy)
    editMenu.add_command(label='Paste', command=paste)
    menuBar.add_cascade(label='Edit', menu=editMenu)

    helpMenu = Menu(menuBar, tearoff=0)
    helpMenu.add_command(label='Help', command=forHelp)
    menuBar.add_cascade(label='Help', menu=helpMenu)

    aboutMenu = Menu(menuBar, tearoff=0)
    aboutMenu.add_command(label='About', command=about)
    menuBar.add_cascade(label='About', menu=aboutMenu)

    root.config(menu=menuBar)

    root.mainloop()