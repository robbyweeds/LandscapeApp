from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from openpyxl import workbook
import excel_funcs as eF
from hard_coding import *

def open_labor_factor_setting_window(db, first, last):
    if first != '' and last != '' and db != '':
        

        laborfactor_setting_window = Toplevel()
        laborfactor_setting_window.iconbitmap('Shearon Logo.ico')
        laborfactor_setting_window.title('Settings')
        setting_title = Label(laborfactor_setting_window, text='Labor Factors').grid(row=0,column=2)
        db_name = 'databases/' + str(db) + '.db'
        print(db_name)

        padding_x2 = 5
        padding_y2 = 5
    else:
        messagebox.showwarning("showwarning", "Missing Fields")

    def updateFactors():
        change_factors = True
        print('update factors')
        db_name = 'databases/' + str(db) + '.db'
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

    db_name = 'databases/' + str(db) + '.db'
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