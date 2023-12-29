from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from openpyxl import workbook
import excel_funcs as eF
from hard_coding import *

header_font = ("Helvetica", 14)
header2_font = ("Helvetica", 12)

def editPlants(db, first, last):
    def changePlantInfo(data):
        print(data)
        name_var1 = StringVar()
        qty_var1 = StringVar()
        size_var1 = StringVar()
        cost_var1 = StringVar()
        plant_type_var1 = StringVar()
        def updateBox(*args):
            print(plant_type_var1.get)
            size_var1.set('')
            size_var1['values'] = plant_categories[plant_type.get()]
            size_var1.current(0)



        edit_window = Toplevel()
        edit_window.iconbitmap('Shearon Logo.ico')
        edit_window.title('Edit Window')
        padding_x1 = 5
        padding_y1 =5
        def changeInfo(name):
            db_name = 'databases/' + str(db) + '.db'
            print(db_name)
            conn = sqlite3.connect(db_name)
            cur = conn.cursor()
            cur.execute('''UPDATE plants SET qty = ?, size = ?, cost = ?, plant_type =? WHERE name = ?
                        ''',(qty_var1.get(), size_var1.get(), cost_var1.get(), plant_type_var1.get(), name))
            conn.commit()
            conn.close()
            edit_window.destroy()
            plant_edit_window.destroy()


            

        Label(edit_window, text= "Plant Name").grid(row=1, column=0, padx=padding_x1, pady=padding_y1)
        Label(edit_window, text= "Qty").grid(row=1, column=1, padx=padding_x1, pady=padding_y1)
        Label(edit_window, text= "Cost").grid(row=1, column=2, padx=padding_x1, pady=padding_y1)
        Label(edit_window, text= "Size").grid(row=1, column=3, padx=padding_x1, pady=padding_y1)
        Label(edit_window, text= "Cost").grid(row=1, column=5, padx=padding_x1, pady=padding_y1)
        Label(edit_window, text="Plant Type").grid(row=1, column=2, padx=padding_x1, pady=padding_y1)


        new_name = Label(edit_window, text=data[0]).grid(row=2, column=0, padx=padding_x1, pady=padding_y1)
        new_qty = Entry(edit_window, textvariable=qty_var1).grid(row=2, column=1, padx=padding_x1, pady=padding_y1)
        new_cost = Entry(edit_window, textvariable=cost_var1).grid(row=2, column=5, padx=padding_x1, pady=padding_y1)
        plant_type = ttk.Combobox(edit_window, textvariable=plant_type_var1)
        plant_type['values'] = [key for key in plant_categories.keys()]
        plant_type.grid(row=2, column=2)
        plant_type.current(0)
        
        plant_type.bind("<<ComboboxSelected>>", lambda event: updateBox())
        plant_size = ttk.Combobox(edit_window, textvariable=size_var1)
        plant_size['values'] = plant_categories['container']
        plant_size.grid(row=2,column=3, padx=padding_x1, pady=padding_y1)
        plant_size.current(0)

        Button(edit_window, text='Update Information', command=lambda: changeInfo(data[0])).grid(row=3, column=2, padx=padding_x1, pady=padding_y1)


    if first != '' and last != '' and db != '':
        plant_edit_window = Toplevel()
        plant_edit_window.title("Plant Edit Window")
        plant_edit_window.geometry('550x500')
        ret_entries = []
        db_name = 'databases/' + str(db) + '.db'
        print(db_name)
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
        cur = cur.execute('''SELECT * FROM plants''')
        data = cur.fetchall()
        for i in data:
            p_group = [i[0], i[1], i[2], i[3], i[4]]
            # print(p_group)
            ret_entries.append(p_group)
        conn.close()
        p_rows = 3
        for i in ret_entries:
            print(i)          
            p_rows = p_rows + 1          
            Label(plant_edit_window, text= i[0]).grid(row=p_rows, column=0)
            Label(plant_edit_window, text= i[1]).grid(row=p_rows, column=1)
            Label(plant_edit_window, text= i[2]).grid(row=p_rows, column=2)
            Label(plant_edit_window, text= "${:,.2f}".format(int(i[3]))).grid(row=p_rows, column=3)
            Label(plant_edit_window, text=ret_entries.index(i)).grid(row=p_rows, column=4)
            Label(plant_edit_window, text= i[4]).grid(row=p_rows, column=5)
            Button(plant_edit_window, text="Edit", command=lambda: changePlantInfo(i)).grid(row=p_rows, column=6)


        l1 = Label(plant_edit_window, text="Plant Edit Window").grid(row=0, column = 2)
        header_common_name = Label(plant_edit_window, text='Plant Common Name').grid(row=2, column=0)
        header_qty = Label(plant_edit_window, text='Plant Quantity').grid(row=2, column=1)
        header_size = Label(plant_edit_window, text='Plant Size').grid(row=2, column=2)
        header_cost = Label(plant_edit_window, text='Plant Cost').grid(row=2, column=3)
        row_num = Label(plant_edit_window, text='Row #').grid(row=2, column=4)
        header_plant_type = Label(plant_edit_window, text='Plant Type').grid(row=2, column=5)

    else:
        messagebox.showwarning("showwarning", "Missing Fields")