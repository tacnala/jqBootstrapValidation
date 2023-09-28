
from storage import Storage
from statement import Sheet, Record

import tkinter as tk



class StorageGUI:

    def __init__(self, storage: Storage = None, width = 600, height = 300):
        self.storage = storage

        self.width, self.height = width, height
        self.window, self.canvas = self.base()
        self.load_sheets()
        self.window.mainloop()

    def base(self):
        window = tk.Tk()

        canvas = tk.Canvas(window, width= self.width, height= self.height)
        canvas.pack()

        window.title('Sheet Storage & Information')
        window.resizable(False, False   )

        return window, canvas
    
    def load_sheets(self):
        w = self.window
        c = self.canvas

        btn_height = 18
        line_width = 2
        line_y = self.height - btn_height - line_width
        line_x = 60
        c.create_line(0, line_y, self.width, line_y, width = line_width)
        c.create_line(line_x, line_y + line_width + 1, line_x, self.height+100)

        lbl_sheet = tk.Label(w, text="Sheets", font=("Helvetica", 11))
        lbl_sheet.place(x= 2, y= (line_y+line_width-1))     

        btn_x = line_x + 5
        # ADD A button for each sheet
        for sheet_name, sheet in self.storage.sheets.items():
            print(sheet_name)
            btn = tk.Button(w, text = sheet_name, font= ("Helvetica", 11))
            btn.config(height= btn_height)
            btn.place(x=btn_x, y=line_y + line_width)



    def toTab(self, sheet_name):
        return
        
class SheetGUI:
    def __init__(self, sheet: Sheet, width, height):
        self.sheet, self.width, self.height = sheet, width, height
        return





if __name__ == '__main__':
    print('loading GUI ...')

    main_storage = Storage()
    main_storage.load_sheets()

    StorageGUI(main_storage)


        #self.height += 200
        #w.config(height=self.height, width= self.width)