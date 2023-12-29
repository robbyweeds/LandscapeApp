from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from openpyxl import workbook
import excel_funcs as eF
from hard_coding import *


# base_labor_factors = ['0.10', '0.15', '0.20', '0.35', '0.45', '0.50', '0.60', '0.45', '0.75' ,'2.0', '2.5', '3.0', '3.5', '4.0', '2.0', '2.5','3.0', '3.5','4.0','5.0','0.35','0.45','0.55','0.65','0.70','0.80', '0.90']
# plant_categories = {
#             'container': ['quart', '1gal', '2gal', '3gal', '5gal', '7gal', '10gal', '15gal', '25gal'], 
#             'deciduous trees':['1.5"-2"', '2"-2.5"', '2.5"-3"', '3"-3.5"', '3.5"-4"'], 
#             'evergreen trees':["4'-5'", "5'-6'", "6'-7'", "7'-8'", "8'-9'", "9'-10'"],
#             'shrubs': ['12"-15"', '15"-18"', '18"-24"', '24"-30"', '30"-36"', '36"-40"']}
# grid_rows = 3
header_font = ("Helvetica", 11)

# style = ttk.Style()
# style.configure("Custom.TButton",
#                          foreground="black",
#                          background="white",
#                          padding=[10, 10, 10, 10],
#                          font="Calibri")

def open_plant_window(db, last, first):
    if first != '' and last != '' and db != '':
        plant_window = Toplevel()
        plant_window.iconbitmap('Shearon Logo.ico')
        db_name = 'databases/' + str(db) + '.db'
        print(db_name)
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS plants (name TEXT, qty TEXT, size TEXT, cost TEXT, plant_type TEXT)''')
        

        conn.commit()
        ret_data1 = cur.execute('''SELECT * FROM plants''').fetchall()
        p_rows = 3
        for i in ret_data1:          
            p_rows = p_rows + 1          
            Label(plant_window, text= i[0]).grid(row=p_rows, column=0)
            Label(plant_window, text= i[1]).grid(row=p_rows, column=1)
            Label(plant_window, text= i[4]).grid(row=p_rows, column=2)                    
            Label(plant_window, text= i[2]).grid(row=p_rows, column=3)
            Label(plant_window, text=ret_data1.index(i)).grid(row=p_rows, column=4)
            Label(plant_window, text= "${:,.2f}".format(int(i[3]))).grid(row=p_rows, column=5)
            Label(plant_window, text= "Ext Cost").grid(row=p_rows, column=6)
            Label(plant_window, text= "Total Cost").grid(row=p_rows, column=7)
        conn.close()

        def saveExit():
            plant_window.destroy()
            
        def addPlant(window):
            if name_var.get() != '' and qty_var.get() != '' and cost_var.get() != '' and size_var.get() != '' and plant_type_var.get() != '':

                db_name = 'databases/' + str(db) + '.db'
                print(db_name)
                conn = sqlite3.connect(db_name)
                cur = conn.cursor()
                cur.execute('''INSERT INTO plants VALUES (?,?,?,?,?)
                            ''', (name_var.get(), qty_var.get(), size_var.get(), cost_var.get(), plant_type_var.get()))
                
                ret_data = cur.execute('''SELECT * FROM plants''').fetchall()
                
                print(ret_data)
                p_rows = 3
                for i in ret_data:          
                    p_rows = p_rows + 1          
                    Label(plant_window, text= i[0]).grid(row=p_rows, column=0)
                    Label(plant_window, text= i[1]).grid(row=p_rows, column=1)
                    Label(plant_window, text= i[4]).grid(row=p_rows, column=2)                    
                    Label(plant_window, text= i[2]).grid(row=p_rows, column=3)
                    Label(plant_window, text=ret_data.index(i)).grid(row=p_rows, column=4)
                    Label(plant_window, text= "${:,.2f}".format(int(i[3]))).grid(row=p_rows, column=5)
                    Label(plant_window, text= "Ext Cost").grid(row=p_rows, column=6)
                    Label(plant_window, text= "Total Cost").grid(row=p_rows, column=7)
                conn.commit()
                conn.close()

                name_var.set('')
                qty_var.set('')
                size_var.set('')
                cost_var.set('')
            else:
                messagebox.showwarning("showwarning", "All Fields Not Completed")
    
            
        
        plantList = Frame(plant_window)
        plant_rows = IntVar(plant_window, value=3, name='plantrows')
        plant_window.title('Plant Selection')
        plant_window.geometry('950x700')
        plant_window_title = Label(plant_window, text='Plant Chart', font=("Helvetica", 18)).grid(row=0, column=2)
        add_plant = Button(plant_window, text='Add Plant Info', command=lambda: addPlant(plant_window), font=("Calibri", 12)).grid(row=1, column=4)
        save_and_Exit = Button(plant_window, text='Save and Exit', command=lambda: saveExit(), font=("Calibri", 12)).grid(row=1, column=5)
    #names of plant selection columns
        
        header_common_name = Label(plant_window, text='Plant Common Name', font=header_font).grid(row=2, column=0)
        header_qty = Label(plant_window, text='Qty', font=header_font).grid(row=2, column=1)
        header_plant_type = Label(plant_window, text='Plant Type', font=header_font).grid(row=2, column=2)
        header_size = Label(plant_window, text='Plant Size', font=header_font).grid(row=2, column=3)
        row_num = Label(plant_window, text='Row #', font=header_font).grid(row=2, column=4)
        header_cost = Label(plant_window, text='Plant Cost', font=header_font).grid(row=2, column=5)
        head_ext_cost = Label(plant_window, text='Plant Ext. Cost', font=header_font).grid(row=2, column=6)
        total_plant_cost = Label(plant_window, text='Total Plant Cost', font=header_font).grid(row=2, column=7)
        

        name_var = StringVar()
        qty_var = StringVar()
        size_var = StringVar()
        cost_var = StringVar()
        plant_type_var = StringVar()
        
        
        def updateBox(*args):
            print(plant_type.get)
            plant_size.set('')
            plant_size['values'] = plant_categories[plant_type.get()]
            plant_size.current(0)


        
        new_name = Entry(plant_window, textvariable=name_var).grid(row=grid_rows, column=0)
        new_qty = Entry(plant_window, textvariable=qty_var, width="10").grid(row=grid_rows, column=1)
        plant_type = ttk.Combobox(plant_window, textvariable=plant_type_var)
        plant_type['values'] = [key for key in plant_categories.keys()]
        plant_type.grid(row=grid_rows, column=2)
        plant_type.current(0)
        
        plant_type.bind("<<ComboboxSelected>>", lambda event: updateBox())
        plant_size = ttk.Combobox(plant_window, textvariable=size_var)
        plant_size['values'] = plant_categories['container']
        plant_size.grid(row=grid_rows,column=3)
        plant_size.current(0)
       
        new_cost = Entry(plant_window, textvariable=cost_var).grid(row=grid_rows, column=5)
        
    else:
        messagebox.showwarning("showwarning", "All Fields Not Completed")