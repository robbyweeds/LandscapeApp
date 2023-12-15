from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from openpyxl import workbook
import excel_funcs as eF
from hard_coding import *

def open_service_factor_setting_window(db, first, last):
    if first != '' and last != '' and db != '':
        

        servicefactor_setting_window = Toplevel()