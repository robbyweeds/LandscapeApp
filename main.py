from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from openpyxl import Workbook
import excel_funcs as eF

change_factors = False
all_entries = []

plant_categories = {
            'container': ['quart', '1gal', '2gal', '3gal', '5gal', '7gal', '10gal', '15gal', '25gal'], 
            'deciduous trees':['1.5"-2"', '2"-2.5"', '2.5"-3"', '3"-3.5"', '3.5"-4"'], 
            'evergreen trees':["4'-5'", "5'-6'", "6'-7'", "7'-8'", "8'-9'", "9'-10'"],
            'shrubs': ['12"-15"', '15"-18"', '18"-24"', '24"-30"', '30"-36"', '36"-40"']}
base_labor_factors = ['0.10', '0.15', '0.20', '0.35', '0.45', '0.50', '0.60', '0.45', '0.75' ,'2.0', '2.5', '3.0', '3.5', '4.0', '2.0', '2.5','3.0', '3.5','4.0','5.0','0.35','0.45','0.55','0.65','0.70','0.80', '0.90']

grid_rows = 3

def open_plant_window():
    plant_window = Toplevel()
    db_name = 'databases/' + str(e3_var.get()) + '.db'
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
            all_entries.append( [name_var.get(), qty_var.get(), size_var.get(), cost_var.get(), plant_type_var.get()] )
            db_name = 'databases/' + str(e3_var.get()) + '.db'
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
    if e1_var.get() != '' and e2_var.get() != '' and e3_var.get() != '':
            
        
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


def open_service_window():
    def addService(window):
        if s1_name_var.get() != '' and s1_matname_var.get() != '' and s1_matcost_var.get() != '' and s1_manhours_var.get() != '':
            db_name = 'databases/' + str(e3_var.get()) + '.db'
            print(db_name)
            conn = sqlite3.connect(db_name)
            cur = conn.cursor()
            cur.execute('''INSERT INTO services VALUES (?,?,?,?)
                        ''', (s1_name_var.get(), s1_matname_var.get(), s1_matcost_var.get(), s1_manhours_var.get()))
            
            ret_data = cur.execute('''SELECT * FROM services''').fetchall()
            print(s1_manhours_var.get())
            p_rows = 3
            for i in ret_data:          
                p_rows = p_rows + 1          
                Label(service_window, text= i[0]).grid(row=p_rows, column=0)
                Label(service_window, text= i[1]).grid(row=p_rows, column=1)
                Label(service_window, text= i[2]).grid(row=p_rows, column=2)  
                Label(service_window, text= i[3]).grid(row=p_rows, column=3)               
                
                Label(service_window, text=ret_data.index(i)).grid(row=p_rows, column=4)
                
            conn.commit()
            conn.close()

            s1_name_var.set('')
            s1_matname_var.set('')
            s1_matcost_var.set('')
            s1_manhours_var.set('')
        else:
            messagebox.showwarning("showwarning", "All Fields Not Completed")
    s1_name_var = StringVar()
    s1_matname_var = StringVar()
    s1_matcost_var = StringVar()
    s1_manhours_var = StringVar()


    service_window = Toplevel()
    service_window.title('Services')
    service_window.geometry('700x700')

    service_window_title = Label(service_window, text='Service Chart').grid(row=0, column=2)

    header_service_name = Label(service_window, text='Name of Service').grid(row=1, column=0)
    header_material_name = Label(service_window, text='Materials').grid(row=1, column=1)
    header_material_cost = Label(service_window, text='Material Cost').grid(row=1, column=2)
    header_manhours = Label(service_window, text='Total Man Hours').grid(row=1, column=3)
    row_num = Label(service_window, text='Row #').grid(row=1, column = 4)
    add_plant = Button(service_window, text='Add Service Info', command=lambda: addService(service_window)).grid(row=0, column=5)

    s1_name = Entry(service_window, textvariable=s1_name_var).grid(row=2, column=0)
    s1_matname = Entry(service_window, textvariable=s1_matname_var).grid(row=2, column=1)
    s1_matcost = Entry(service_window, textvariable=s1_matcost_var).grid(row=2, column=2)
    s1_manhours = Entry(service_window, textvariable=s1_manhours_var).grid(row=2, column=3)

    db_name = 'databases/' + str(e3_var.get()) + '.db'
    print(db_name)
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS services (name TEXT, material TEXT, mat_cost TEXT, manhours TEXT)''')
    conn.commit()
    ret_data1 = cur.execute('''SELECT * FROM services''').fetchall()
    p_rows = 3
    for i in ret_data1:          
        p_rows = p_rows + 1          
        Label(service_window, text= i[0]).grid(row=p_rows, column=0)
        Label(service_window, text= i[1]).grid(row=p_rows, column=1)
        Label(service_window, text= i[2]).grid(row=p_rows, column=2)
        Label(service_window, text= i[3]).grid(row=p_rows, column=3)                
        Label(service_window, text=ret_data1.index(i)).grid(row=p_rows, column=4)
        
    conn.close()



def createExcel():
    db_name = 'databases/' + str(e3_var.get()) + '.db'
    print(db_name)
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur = cur.execute('''SELECT * FROM plants''')
    data = cur.fetchall()
    for i in data:
        print(i)


    eF.createWorkbook(db_name)  
    conn.close()



def editPlants():
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
        padding_x1 = 5
        padding_y1 =5
        def changeInfo(name):
            db_name = 'databases/' + str(e3_var.get()) + '.db'
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


    if e1_var.get() != '' and e2_var.get() != '' and e3_var.get() != '':
        plant_edit_window = Toplevel()
        plant_edit_window.title("Plant Edit Window")
        plant_edit_window.geometry('550x500')
        ret_entries = []
        db_name = 'databases/' + str(e3_var.get()) + '.db'
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
            Label(plant_edit_window, text= i[3]).grid(row=p_rows, column=3)
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

def open_labor_factor_setting_window():
    if e1_var.get() != '' and e2_var.get() != '' and e3_var.get() != '':
        

        laborfactor_setting_window = Toplevel()
        laborfactor_setting_window.title('Settings')
        setting_title = Label(laborfactor_setting_window, text='Labor Factors').grid(row=0,column=2)
        db_name = 'databases/' + str(e3_var.get()) + '.db'
        print(db_name)

        padding_x2 = 5
        padding_y2 = 5
    else:
        messagebox.showwarning("showwarning", "Missing Fields")

    def updateFactors():
        change_factors = True
        print('update factors')
        db_name = 'databases/' + str(e3_var.get()) + '.db'
        print(db_name)
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS labor_factors (con_qrt TEXT, con_gal TEXT, con_2gal TEXT, con_3gal TEXT, con_5gal TEXT, con_7gal TEXT, con_10gal TEXT, con_15gal TEXT, con_25gal TEXT,
                    dec_15 TEXT, dec_20 TEXT, dec_25 TEXT, dec_30 TEXT, dec_35 TEXT,
                    ever_4 TEXT, ever_5 TEXT, ever_6 TEXT, ever_7 TEXT, ever_8 TEXT, ever_9 TEXT,
                    sh_12 TEXT, sh_15 TEXT, sh_18 TEXT, sh_24 TEXT, sh_30 TEXT, sh_36 TEXT, sh_40 TEXT
                    )''')
        cur.execute('''INSERT INTO labor_factors VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                    ''',(quart_factor.get(), gal_factor.get(), twogal_factor.get(), threegal_factor.get(), fivegal_factor.get(), sevengal_factor.get(), tengal_factor.get(), fifteen_factor.get(), twentyfivegal_factor.get(),
                         one5_two_factor.get(), two_two5_factor.get(), two5_three_factor.get(), three_three5_factor.get(), three5_four_factor.get(),
                         four_five_factor.get(), five_six_factor.get(), six_seven_factor.get(), seven_eight_factor.get(), eight_nine_factor.get(), nine_ten_factor.get(),
                         twelve_factor.get(), fifteen_factor.get(), eighteen_factor.get(), twentyfour_factor.get(), thirty_factor.get(), thirtysix_factor.get(), forty_factor.get()))
        conn.commit()
        ret_cur = cur.execute('''SELECT * FROM labor_factors''').fetchall()
        print(ret_cur)
        conn.close()

    db_name = 'databases/' + str(e3_var.get()) + '.db'
    print(db_name)
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    ret_data = cur.execute('''SELECT * FROM labor_factors WHERE ROWID IN ( SELECT max( ROWID ) FROM labor_factors )''').fetchone()
    ('last entry')
    print(ret_data)
#Container Labor Factors
    quart_factor= StringVar()
    quart_factor.set(ret_data[0])
    gal_factor = StringVar()
    gal_factor.set(base_labor_factors[1])
    twogal_factor = StringVar()
    twogal_factor.set(base_labor_factors[2])
    threegal_factor = StringVar()
    threegal_factor.set(base_labor_factors[3])
    fivegal_factor = StringVar()
    fivegal_factor.set(base_labor_factors[4])
    sevengal_factor = StringVar()
    sevengal_factor.set(base_labor_factors[5])
    tengal_factor = StringVar()
    tengal_factor.set(base_labor_factors[6])
    fifteengal_factor = StringVar()
    fifteengal_factor.set(base_labor_factors[7])
    twentyfivegal_factor = StringVar()
    twentyfivegal_factor.set(base_labor_factors[8])
    Label(laborfactor_setting_window, text='Container').grid(row=1, column=0, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text='Quart').grid(row=2, column=0, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=quart_factor).grid(row=2, column=1, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text='Gallon').grid(row=3, column=0, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=gal_factor).grid(row=3, column=1, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text='2 Gal').grid(row=4, column=0, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=twogal_factor).grid(row=4, column=1, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text='3 Gal').grid(row=5, column=0, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=threegal_factor).grid(row=5, column=1, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text='5 Gal').grid(row=6, column=0, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=fivegal_factor).grid(row=6, column=1, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text='7 Gal').grid(row=7, column=0, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=sevengal_factor).grid(row=7, column=1, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text='10 Gal').grid(row=8, column=0, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=tengal_factor).grid(row=8, column=1, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text='15 Gal').grid(row=9, column=0, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=fifteengal_factor).grid(row=9, column=1, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text='25 Gal').grid(row=10, column=0, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=twentyfivegal_factor).grid(row=10, column=1, padx=padding_x2, pady=padding_y2)

#Deciduous Trees Labor Factors
    one5_two_factor= StringVar()
    one5_two_factor.set(base_labor_factors[9])
    two_two5_factor = StringVar()
    two_two5_factor.set(base_labor_factors[10])
    two5_three_factor = StringVar()
    two5_three_factor.set(base_labor_factors[11])
    three_three5_factor = StringVar()
    three_three5_factor.set(base_labor_factors[12])
    three5_four_factor = StringVar()
    three5_four_factor.set(base_labor_factors[13])
    Label(laborfactor_setting_window, text='Deciduous Trees').grid(row=1, column=2, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text='1.5"-2"').grid(row=2, column=2, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=one5_two_factor).grid(row=2, column=3, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text='2"-2.5"').grid(row=3, column=2, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=two_two5_factor).grid(row=3, column=3, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text='2.5"-3"').grid(row=4, column=2, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=two5_three_factor).grid(row=4, column=3, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text='3"-3.5""').grid(row=5, column=2, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=three_three5_factor).grid(row=5, column=3, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text='3.5"-4"').grid(row=6, column=2, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=three5_four_factor).grid(row=6, column=3, padx=padding_x2, pady=padding_y2)

#Evergreen Trees Labor Factors
    four_five_factor= StringVar()
    four_five_factor.set(base_labor_factors[14])
    five_six_factor = StringVar()
    five_six_factor.set(base_labor_factors[15])
    six_seven_factor = StringVar()
    six_seven_factor.set(base_labor_factors[16])
    seven_eight_factor = StringVar()
    seven_eight_factor.set(base_labor_factors[17])
    eight_nine_factor = StringVar()
    eight_nine_factor.set(base_labor_factors[18])
    nine_ten_factor = StringVar()
    nine_ten_factor.set(base_labor_factors[19])
    Label(laborfactor_setting_window, text='Evergreen Trees').grid(row=7, column=2, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text="4'-5'").grid(row=8, column=2, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=four_five_factor).grid(row=8, column=3, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text="5'-6'").grid(row=9, column=2, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=five_six_factor).grid(row=9, column=3, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text="6'-7'").grid(row=10, column=2, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=six_seven_factor).grid(row=10, column=3, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text="7'-8'").grid(row=11, column=2, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=seven_eight_factor).grid(row=11, column=3, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text="8'-9'").grid(row=12, column=2, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=eight_nine_factor).grid(row=12, column=3, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text="9'-10'").grid(row=13, column=2, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=nine_ten_factor).grid(row=13, column=3, padx=padding_x2, pady=padding_y2)

#shrubs Trees Labor Factors
    twelve_factor= StringVar()
    twelve_factor.set(base_labor_factors[20])
    fifteen_factor = StringVar()
    fifteen_factor.set(base_labor_factors[21])
    eighteen_factor = StringVar()
    eighteen_factor.set(base_labor_factors[22])
    twentyfour_factor = StringVar()
    twentyfour_factor.set(base_labor_factors[23])
    thirty_factor = StringVar()
    thirty_factor.set(base_labor_factors[24])
    thirtysix_factor = StringVar()
    thirtysix_factor.set(base_labor_factors[25])
    forty_factor = StringVar()
    forty_factor.set(base_labor_factors[26])

    Label(laborfactor_setting_window, text='Shrubs').grid(row=1, column=5, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text='12"-15"').grid(row=2, column=4, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=twelve_factor).grid(row=2, column=5, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text='15"-18"').grid(row=3, column=4, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=fifteen_factor).grid(row=3, column=5, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text='18"-24"').grid(row=4, column=4, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=eighteen_factor).grid(row=4, column=5, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text='24"-30""').grid(row=5, column=4, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=twentyfour_factor).grid(row=5, column=5, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text='30"-36"').grid(row=6, column=4, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=thirty_factor).grid(row=6, column=5, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text='30"-36""').grid(row=7, column=4, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=thirtysix_factor).grid(row=7, column=5, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text='36"-40"').grid(row=8, column=4, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=thirtysix_factor).grid(row=8, column=5, padx=padding_x2, pady=padding_y2)
    Label(laborfactor_setting_window, text='40"-46"').grid(row=9, column=4, padx=padding_x2, pady=padding_y2)
    Entry(laborfactor_setting_window, textvariable=forty_factor).grid(row=9, column=5, padx=padding_x2, pady=padding_y2)

    Button(laborfactor_setting_window, text='Update Factors', command=updateFactors).grid(row=14, column=2, padx=padding_x2, pady=padding_y2)

    conn.close()

root = Tk()

root.title('Welcome')

e1_var = StringVar()
e2_var = StringVar()
e3_var = StringVar()

padding_y = 10
padding_x = 20


l1 = Label(root, text='First Name').grid(row=0, column=0, padx=padding_x, pady=padding_y)
l2 = Label(root, text='Last Name').grid(row=1, column=0, padx=padding_x, pady=padding_y)
l3 = Label(root, text='Project Name').grid(row=2, column=0, padx=padding_x, pady=padding_y)

e1 = Entry(root, textvariable=e1_var).grid(row=0, column=1, padx=padding_x, pady=padding_y)
e2 = Entry(root, textvariable=e2_var).grid(row=1, column=1, padx=padding_x, pady=padding_y)
e3 = Entry(root, textvariable=e3_var).grid(row=2, column=1, padx=padding_x, pady=padding_y)

b1 = Button(root, text='Add Plants', command=open_plant_window).grid(row=3, column=0, padx=padding_x, pady=padding_y)
b11 = Button(root, text='Edit Plants', command=editPlants).grid(row=3, column=1, padx=padding_x, pady=padding_y)
b2 = Button(root, text='Add Services', command=open_service_window).grid(row=4, column=0, padx=padding_x, pady=padding_y)
b3 = Button(root, text='Create Excel', command=createExcel).grid(row=5, column=0, padx=padding_x, pady=padding_y)

root.geometry('350x300')

root_menu = Menu(root)


root.config(menu=root_menu)
laborfactor_setting_menu = Menu(root_menu, tearoff=False)
laborfactor_setting_menu.add_command(
    label='Labor Factors',
    command=open_labor_factor_setting_window
)
root_menu.add_cascade(
    label='Settings',
    menu=laborfactor_setting_menu,
    underline=0
)


root.mainloop()

