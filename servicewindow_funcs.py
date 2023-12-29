from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from openpyxl import workbook
import excel_funcs as eF
from hard_coding import *

padding_y = 10
padding_x = 20


def open_service_window(db, first, last):
    if first != '' and last != '' and db != '':

        def saveExit():
            service_window.destroy()
    
        def addService(window):
            if s1_name_var.get() != '' and s1_matname_var.get() != '' and s1_matcost_var.get() != '' and s1_manhours_var.get() != '':
                db_name = 'databases/' + str(db) + '.db'
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
        service_window.iconbitmap('Shearon Logo.ico')
        service_window.title('Services')
        service_window.geometry('900x700')

        service_window_title = Label(service_window, text='Service Chart').grid(row=0, column=2)

        header_service_name = Label(service_window, text='Name of Service').grid(row=1, column=0)
        header_material_name = Label(service_window, text='Materials').grid(row=1, column=1)
        header_material_cost = Label(service_window, text='Material Cost').grid(row=1, column=2)
        header_manhours = Label(service_window, text='Total Man Hours').grid(row=1, column=3)
        row_num = Label(service_window, text='Row #').grid(row=1, column = 4)
        mat_ext_cost = Label(service_window, text='Mat. Ext. Cost').grid(row=1, column=5)
        total_cost = Label(service_window, text='Total Cost').grid(row=1, column=6)
        add_plant = Button(service_window, text='Add Service Info', command=lambda: addService(service_window), font=("Calibri", 12)).grid(row=0, column=4, padx=padding_x, pady=padding_y)
        save_and_Exit = Button(service_window, text='Save and Exit', command=lambda: saveExit(), font=("Calibri", 12)).grid(row=0, column=5, padx=padding_x, pady=padding_y)

        s1_name = Entry(service_window, textvariable=s1_name_var).grid(row=2, column=0)
        s1_matname = Entry(service_window, textvariable=s1_matname_var).grid(row=2, column=1)
        s1_matcost = Entry(service_window, textvariable=s1_matcost_var).grid(row=2, column=2)
        s1_manhours = Entry(service_window, textvariable=s1_manhours_var).grid(row=2, column=3)

        db_name = 'databases/' + str(db) + '.db'
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
            Label(service_window, text= "${:,.2f}".format(int(i[2]))).grid(row=p_rows, column=2)
            Label(service_window, text= i[3]).grid(row=p_rows, column=3)                
            Label(service_window, text=ret_data1.index(i)).grid(row=p_rows, column=4)
            amount = "${:,.2f}".format(int(i[2]) / 0.58)
            Label(service_window, text=amount).grid(row=p_rows, column=5)
            Label(service_window, text="${:,.2f}".format(int(i[3]) * 50)).grid(row=p_rows, column=6)

            
        conn.close()
    else:
        messagebox.showwarning("showwarning", "All Fields Not Completed")