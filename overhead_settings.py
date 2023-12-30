from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from openpyxl import workbook
import excel_funcs as eF
from hard_coding import *

header_font = ("Helvetica", 14)
header2_font = ("Helvetica", 12)

padding_x2 = 5
padding_y2 = 5


def open_overhead_settings(db, first, last):
    if first != '' and last != '' and db != '':
        def saveandExit():
            db_name = 'databases/' + str(db) + '.db'
            print(db_name)
            conn = sqlite3.connect(db_name)
            cur = conn.cursor()

            cur.execute('''CREATE TABLE IF NOT EXISTS overhead (gross TEXT, overhead TEXT, adj TEXT, wtf TEXT, sub TEXT)''')
            cur.execute('''DELETE FROM overhead''')
            cur.execute('''INSERT INTO overhead VALUES(?,?,?,?,?)''',(gross_var.get(), overhead_var.get(), adj_var.get(), wtf_var.get(), sub_var.get()))

            conn.commit()
            conn.close()
            overhead_setting_window.destroy()

        def resetDefault():
            db_name = 'databases/' + str(db) + '.db'
            print(db_name)
            conn = sqlite3.connect(db_name)
            cur = conn.cursor()

            cur.execute('''CREATE TABLE IF NOT EXISTS overhead (gross TEXT, overhead TEXT, adj TEXT, wtf TEXT, sub TEXT)''')
            cur.execute('''DELETE FROM overhead''')
            cur.execute('''INSERT INTO overhead VALUES(?,?,?,?,?)''',(base_overhead['gross'], base_overhead['overhead'], base_overhead['adj'], base_overhead['wtf'], base_overhead['sub']))

            conn.commit()
            conn.close()

            gross_var.set(base_overhead['gross'])
            overhead_var.set(base_overhead['overhead'])
            adj_var.set(base_overhead['adj'])
            wtf_var.set(base_overhead['wtf'])
            sub_var.set(base_overhead['sub'])


        overhead_setting_window = Toplevel()
        overhead_setting_window.iconbitmap('Shearon Logo.ico')
        overhead_setting_window.title('Settings')
        overhead_setting_window.geometry('700x450')

        setting_title = Label(overhead_setting_window, text='Overhead Formula\'s', font=header_font).grid(row=0,column=2)

        Button(overhead_setting_window, text='Save and Exit', command=lambda: saveandExit()).grid(row=1, column=3, padx=padding_x2, pady=padding_y2)
        Button(overhead_setting_window, text='Reset to Default', command=lambda: resetDefault()).grid(row=2, column=3, padx=padding_x2, pady=padding_y2)

        db_name = 'databases/' + str(db) + '.db'
        print(db_name)
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS overhead (gross TEXT, overhead TEXT, adj TEXT, wtf TEXT, sub TEXT)''')
        conn.commit()
        ret_data = cur.execute('''SELECT * FROM overhead WHERE ROWID IN ( SELECT max( ROWID ) FROM labor_factors )''').fetchone()


        gross_var = StringVar()
        overhead_var = StringVar()
        adj_var = StringVar()
        wtf_var = StringVar()
        sub_var = StringVar()

        




        Label(overhead_setting_window, text='Gross Profit').grid(row=2, column=0, padx=padding_x2, pady=padding_y2)
        Entry(overhead_setting_window, textvariable=gross_var).grid(row=2, column=1, padx=padding_x2, pady=padding_y2)
        Label(overhead_setting_window, text='Overhead').grid(row=3, column=0, padx=padding_x2, pady=padding_y2)
        Entry(overhead_setting_window, textvariable=overhead_var).grid(row=3, column=1, padx=padding_x2, pady=padding_y2)
        Label(overhead_setting_window, text='Adjusted Overhead').grid(row=4, column=0, padx=padding_x2, pady=padding_y2)
        Entry(overhead_setting_window, textvariable=adj_var).grid(row=4, column=1, padx=padding_x2, pady=padding_y2)
        Label(overhead_setting_window, text='War., Tax, Freight').grid(row=5, column=0, padx=padding_x2, pady=padding_y2)
        Entry(overhead_setting_window, textvariable=wtf_var).grid(row=5, column=1, padx=padding_x2, pady=padding_y2)
        Label(overhead_setting_window, text='Sub-Contractor').grid(row=6, column=0, padx=padding_x2, pady=padding_y2)
        Entry(overhead_setting_window, textvariable=sub_var).grid(row=6, column=1, padx=padding_x2, pady=padding_y2)

        overhead_data = cur.execute('''SELECT * FROM overhead ORDER BY ROWID DESC LIMIT 1''').fetchone()
        if overhead_data == None:
            gross_var.set(base_overhead['gross'])
            overhead_var.set(base_overhead['overhead'])
            adj_var.set(base_overhead['adj'])
            wtf_var.set(base_overhead['wtf'])
            sub_var.set(base_overhead['sub'])
        else:
            gross_var.set(overhead_data[0])
            overhead_var.set(overhead_data[1])
            adj_var.set(overhead_data[2])
            wtf_var.set(overhead_data[3])
            sub_var.set(overhead_data[4])






        conn.close()

   

    else:
        messagebox.showwarning("showwarning", "Missing Fields")    
