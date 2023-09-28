
from storage import Storage

import tkinter as tk




class StorageGUI:
    def __init__(self, width = 600, height = 200):

        self.width, self.height = width, height

        self.base()

        #self.base()


        #self.window, self.canvas = self.base()
        #self.canvas.pack()


    def base(self):
        window = tk.Tk()

        window.title('Sheet Storage & Information')
        window.geometry(f'{self.width}x{self.height}')

        window.mainloop()
    
    def load_sheets(self):
        #canvas = tk.Canvas(self.window)

        return


    def winExample(self):
        window = tk.Tk()

        window.title('Hello Python')
        window.geometry("300x200")

        # Canvas (for shapes?)
        canvas = tk.Canvas(window)

        # create_line
        canvas.create_line(0,25,300,25, width = 2)

        # pack canvas
        canvas.pack()

        # add button
        btn = tk.Button(window, text = "This is tk.Button widget", fg= 'blue')
        btn.place(x=80, y=100)

        # add label
        lbl = tk.Label(window, text="This is tk.Label widget", fg='red', font=("Helvetica", 16))
        lbl.place(x=60, y=50)

        # add Entry
        txtfld = tk.Entry(window, text = "This is tk.Entry Wdiget", bd=5)
        txtfld.place(x=80, y=150)
        window.mainloop()


    

if __name__ == '__main__':

    mainGUI = StorageGUI()
    #mainGUI.winExample()



