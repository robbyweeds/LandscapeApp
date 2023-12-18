from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from openpyxl import workbook
import excel_funcs as eF
from hard_coding import *

header_font = ("Helvetica", 14)
header2_font = ("Helvetica", 12)


def open_service_factor_setting_window(db, first, last):
    if first != '' and last != '' and db != '':
        

        servicefactor_setting_window = Toplevel()
        servicefactor_setting_window.iconbitmap('Shearon Logo.ico')
        servicefactor_setting_window.title('Settings')
        servicefactor_setting_window.geometry('700x700')

        setting_title = Label(servicefactor_setting_window, text='Labor Factors', font=header_font).grid(row=0,column=1)

        db_name = 'databases/' + str(db) + '.db'
        print(db_name)

        padding_x2 = 5
        padding_y2 = 5
    else:
        messagebox.showwarning("showwarning", "Missing Fields")

    def resetDefaultFactors():
        print('update default labor factors')
        db_name = 'databases/' + str(db) + '.db'
        print(db_name)

    def updateFactors():
        
        print('update factors')
        db_name = 'databases/' + str(db) + '.db'
        print(db_name)

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    # cur.execute('''CREATE TABLE IF NOT EXISTS labor_factors (con_qrt TEXT, con_gal TEXT, con_2gal TEXT, con_3gal TEXT, con_5gal TEXT, con_7gal TEXT, con_10gal TEXT, con_15gal TEXT, con_25gal TEXT,
    #                 dec_15 TEXT, dec_20 TEXT, dec_25 TEXT, dec_30 TEXT, dec_35 TEXT, dec_40 TEXT, dec_45 TEXT, dec_50 TEXT, dec_60 TEXT, dec_70 TEXT,
    #                 ever_4 TEXT, ever_5 TEXT, ever_6 TEXT, ever_7 TEXT, ever_8 TEXT, ever_10 TEXT, ever_12 TEXT, ever_14 TEXT,
    #                 sh_12 TEXT, sh_15 TEXT, sh_18 TEXT, sh_24 TEXT, sh_30 TEXT, sh_36 TEXT, sh_48 TEXT
    #                 )''')
    # ret_data = cur.execute('''SELECT * FROM labor_factors WHERE ROWID IN ( SELECT max( ROWID ) FROM labor_factors )''').fetchone()
    
    # print(ret_data)

    conn.close()

    # Material Service Factors
    Label(servicefactor_setting_window, text='Materials').grid(row=1, column=0, padx=padding_x2, pady=padding_y2)
    mulch_factor = StringVar()
    soil_factor = StringVar()
    stone_factor = StringVar()
    flagstone_factor =StringVar()
    sixbysixbyeight_footer_factor = StringVar()
    sixbysixbyeight_course_factor = StringVar()
    paver_factor = StringVar()
    ads_4pipe_factor = StringVar()

    Label(servicefactor_setting_window, text='Material Factors', font=header2_font).grid(row=1, column=0, padx=padding_x2, pady=padding_y2)
    Label(servicefactor_setting_window, text='1yard of Mulch').grid(row=2, column=0, padx=padding_x2, pady=padding_y2)
    Entry(servicefactor_setting_window, textvariable=mulch_factor).grid(row=2, column=1, padx=padding_x2, pady=padding_y2)
    Label(servicefactor_setting_window, text='1yard of Soil').grid(row=3, column=0, padx=padding_x2, pady=padding_y2)
    Entry(servicefactor_setting_window, textvariable=soil_factor).grid(row=3, column=1, padx=padding_x2, pady=padding_y2)
    Label(servicefactor_setting_window, text='1yard of Stone').grid(row=4, column=0, padx=padding_x2, pady=padding_y2)
    Entry(servicefactor_setting_window, textvariable=stone_factor).grid(row=4, column=1, padx=padding_x2, pady=padding_y2)
    Label(servicefactor_setting_window, text='100 sq/ft of Flagstone').grid(row=5, column=0, padx=padding_x2, pady=padding_y2)
    Entry(servicefactor_setting_window, textvariable=flagstone_factor).grid(row=5, column=1, padx=padding_x2, pady=padding_y2)
    Label(servicefactor_setting_window, text='6\"x6\"x8\' Tierod Footer or Deadman').grid(row=6, column=0, padx=padding_x2, pady=padding_y2)
    Entry(servicefactor_setting_window, textvariable=sixbysixbyeight_footer_factor).grid(row=6, column=1, padx=padding_x2, pady=padding_y2)
    Label(servicefactor_setting_window, text='6\"x6\"x8\' Tierod Course').grid(row=7, column=0, padx=padding_x2, pady=padding_y2)
    Entry(servicefactor_setting_window, textvariable=sixbysixbyeight_course_factor).grid(row=7, column=1, padx=padding_x2, pady=padding_y2)
    Label(servicefactor_setting_window, text='100 sq/ft of Pavers/Bricks').grid(row=8, column=0, padx=padding_x2, pady=padding_y2)
    Entry(servicefactor_setting_window, textvariable=paver_factor).grid(row=8, column=1, padx=padding_x2, pady=padding_y2)
    Label(servicefactor_setting_window, text='10\' of 4" pipe').grid(row=9, column=0, padx=padding_x2, pady=padding_y2)
    Entry(servicefactor_setting_window, textvariable=ads_4pipe_factor).grid(row=9, column=1, padx=padding_x2, pady=padding_y2)

    # Soil and Sod Factors
    groundtilling_factor = StringVar()
    sodprepared_factor = StringVar()
    sodunprepared_factor = StringVar()
    sodprepared_onewide_factor = StringVar()
    sodprepared_threewide_factor = StringVar()
    sodcutter = StringVar()

    Label(servicefactor_setting_window, text='Soil and Sod Factors', font=header2_font).grid(row=1, column=2, padx=padding_x2, pady=padding_y2)
    Label(servicefactor_setting_window, text='100sq/ft of Tilling').grid(row=2, column=2, padx=padding_x2, pady=padding_y2)
    Entry(servicefactor_setting_window, textvariable=groundtilling_factor).grid(row=2, column=3, padx=padding_x2, pady=padding_y2)
    Label(servicefactor_setting_window, text='500 sq/ft of sod prepped').grid(row=3, column=2, padx=padding_x2, pady=padding_y2)
    Entry(servicefactor_setting_window, textvariable=sodprepared_factor).grid(row=3, column=3, padx=padding_x2, pady=padding_y2)
    Label(servicefactor_setting_window, text='500 sq/ft of sod un-prepped').grid(row=4, column=2, padx=padding_x2, pady=padding_y2)
    Entry(servicefactor_setting_window, textvariable=sodunprepared_factor).grid(row=4, column=3, padx=padding_x2, pady=padding_y2)
    Label(servicefactor_setting_window, text='500 sq/ft of sod 1\' Wide').grid(row=5, column=2, padx=padding_x2, pady=padding_y2)
    Entry(servicefactor_setting_window, textvariable=sodprepared_onewide_factor).grid(row=5, column=3, padx=padding_x2, pady=padding_y2)
    Label(servicefactor_setting_window, text='500 sq/ft of sod 3\' Wide').grid(row=6, column=2, padx=padding_x2, pady=padding_y2)
    Entry(servicefactor_setting_window, textvariable=sodprepared_threewide_factor).grid(row=6, column=3, padx=padding_x2, pady=padding_y2)
    Label(servicefactor_setting_window, text='100 sq/ft Sodcutter').grid(row=6, column=2, padx=padding_x2, pady=padding_y2)
    Entry(servicefactor_setting_window, textvariable=sodcutter).grid(row=6, column=3, padx=padding_x2, pady=padding_y2)

    # Tree Staking
    sixfoot_upright_factor = StringVar()
    eightfoot_upright_factor = StringVar()
    twofoot_guywire_factor = StringVar()
    sixinch_turnbuckle_factor = StringVar()

    Label(servicefactor_setting_window, text='Tree Staking').grid(row=7, column=2, padx=padding_x2, pady=padding_y2)
    Label(servicefactor_setting_window, text='6\' Upright Staking').grid(row=8, column=2, padx=padding_x2, pady=padding_y2)
    Entry(servicefactor_setting_window, textvariable=sixfoot_upright_factor).grid(row=8, column=3, padx=padding_x2, pady=padding_y2)
    Label(servicefactor_setting_window, text='8\' Upright Staking').grid(row=9, column=2, padx=padding_x2, pady=padding_y2)
    Entry(servicefactor_setting_window, textvariable=eightfoot_upright_factor).grid(row=9, column=3, padx=padding_x2, pady=padding_y2)
    Label(servicefactor_setting_window, text='2\' Guywire').grid(row=10, column=2, padx=padding_x2, pady=padding_y2)
    Entry(servicefactor_setting_window, textvariable=twofoot_guywire_factor).grid(row=10, column=3, padx=padding_x2, pady=padding_y2)
    Label(servicefactor_setting_window, text='6" Turnbuckle').grid(row=11, column=2, padx=padding_x2, pady=padding_y2)
    Entry(servicefactor_setting_window, textvariable=sixinch_turnbuckle_factor).grid(row=11, column=3, padx=padding_x2, pady=padding_y2)
