from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from openpyxl import Workbook
import plantwindow_funcs as wF
import editlaborfactor_window as lF
import plantedit_window as pE
import servicewindow_funcs as sF
import excel_funcs as eF
from hard_coding import *

change_factors = False

root = Tk()
root.iconbitmap('Shearon Logo.ico')
root.title('Bid Sheet')

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

b1 = Button(root, text='Add Plants', command=lambda: wF.open_plant_window(e3_var.get(), e2_var.get(),e1_var.get() )).grid(row=3, column=0, padx=padding_x, pady=padding_y)
b11 = Button(root, text='Edit Plants', command=lambda: pE.editPlants(e3_var.get(), e2_var.get(),e1_var.get() )).grid(row=3, column=1, padx=padding_x, pady=padding_y)
b2 = Button(root, text='Add Services', command=lambda: sF.open_service_window(e3_var.get(), e2_var.get(),e1_var.get() )).grid(row=4, column=0, padx=padding_x, pady=padding_y)
b3 = Button(root, text='Create Excel', command=lambda: eF.createExcel()).grid(row=5, column=0, padx=padding_x, pady=padding_y)

root.geometry('350x300')

root_menu = Menu(root)

root.config(menu=root_menu)
laborfactor_setting_menu = Menu(root_menu, tearoff=False)
laborfactor_setting_menu.add_command(
    label='Labor Factors',
    command=lambda: lF.open_labor_factor_setting_window(e3_var.get(), e2_var.get(),e1_var.get() )
    )
root_menu.add_cascade(
    label='Settings',
    menu=laborfactor_setting_menu,
    underline=0
    )

root.mainloop()

