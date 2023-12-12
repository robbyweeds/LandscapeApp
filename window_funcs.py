from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from openpyxl import workbook
import excel_funcs as eF


base_labor_factors = ['0.10', '0.15', '0.20', '0.35', '0.45', '0.50', '0.60', '0.45', '0.75' ,'2.0', '2.5', '3.0', '3.5', '4.0', '2.0', '2.5','3.0', '3.5','4.0','5.0','0.35','0.45','0.55','0.65','0.70','0.80', '0.90']
plant_categories = {
            'container': ['quart', '1gal', '2gal', '3gal', '5gal', '7gal', '10gal', '15gal', '25gal'], 
            'deciduous trees':['1.5"-2"', '2"-2.5"', '2.5"-3"', '3"-3.5"', '3.5"-4"'], 
            'evergreen trees':["4'-5'", "5'-6'", "6'-7'", "7'-8'", "8'-9'", "9'-10'"],
            'shrubs': ['12"-15"', '15"-18"', '18"-24"', '24"-30"', '30"-36"', '36"-40"']}
grid_rows = 3

def open_plant_window(db, last, first):
    
    plant_window = Toplevel()
    db_name = 'databases/' + str(db) + '.db'
    print(db_name)
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS plants (name TEXT, qty TEXT, size TEXT, cost TEXT, plant_type TEXT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS labor_factors (con_qrt TEXT, con_gal TEXT, con_2gal TEXT, con_3gal TEXT, con_5gal TEXT, con_7gal TEXT, con_10gal TEXT, con_15gal TEXT, con_25gal TEXT,
                    dec_15 TEXT, dec_20 TEXT, dec_25 TEXT, dec_30 TEXT, dec_35 TEXT,
                    ever_4 TEXT, ever_5 TEXT, ever_6 TEXT, ever_7 TEXT, ever_8 TEXT, ever_9 TEXT,
                    sh_12 TEXT, sh_15 TEXT, sh_18 TEXT, sh_24 TEXT, sh_30 TEXT, sh_36 TEXT, sh_40 TEXT
                    )''')
    cur.execute('''INSERT INTO labor_factors VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                    ''', (base_labor_factors[0],base_labor_factors[1],base_labor_factors[2],base_labor_factors[3],base_labor_factors[4],base_labor_factors[5],base_labor_factors[6],base_labor_factors[7],base_labor_factors[8],
                          base_labor_factors[9],base_labor_factors[10],base_labor_factors[11],base_labor_factors[12],base_labor_factors[13],
                          base_labor_factors[14],base_labor_factors[15],base_labor_factors[16],base_labor_factors[17],base_labor_factors[18],base_labor_factors[19],
                          base_labor_factors[20],base_labor_factors[21],base_labor_factors[22],base_labor_factors[23],base_labor_factors[24],base_labor_factors[25],base_labor_factors[26]))
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
        Label(plant_window, text= i[3]).grid(row=p_rows, column=5)
    conn.close()


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
                Label(plant_window, text= i[3]).grid(row=p_rows, column=5)
            conn.commit()
            conn.close()

            name_var.set('')
            qty_var.set('')
            size_var.set('')
            cost_var.set('')
        else:
            messagebox.showwarning("showwarning", "All Fields Not Completed")
    if first != '' and last != '' and db != '':
            
        
        plantList = Frame(plant_window)
        plant_rows = IntVar(plant_window, value=3, name='plantrows')
        plant_window.title('Plant Selection')
        plant_window.geometry('800x700')
        plant_window_title = Label(plant_window, text='Plant Chart').grid(row=0, column=2)
        add_plant = Button(plant_window, text='Add Plant Info', command=lambda: addPlant(plant_window)).grid(row=1, column=0)
        # save_and_Exit = Button(plant_window, text='Save and Exit', command=lambda: saveExit()).grid(row=1, column=5)
    #names of plant selection columns
        
        header_common_name = Label(plant_window, text='Plant Common Name').grid(row=2, column=0)
        header_qty = Label(plant_window, text='Plant Quantity').grid(row=2, column=1)
        header_plant_type = Label(plant_window, text='Plant Type').grid(row=2, column=2)
        header_size = Label(plant_window, text='Plant Size').grid(row=2, column=3)
        row_num = Label(plant_window, text='Row #').grid(row=2, column=4)
        header_cost = Label(plant_window, text='Plant Cost').grid(row=2, column=5)
        

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
        new_qty = Entry(plant_window, textvariable=qty_var).grid(row=grid_rows, column=1)
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