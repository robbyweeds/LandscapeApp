from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from openpyxl import workbook
import excel_funcs as eF
from hard_coding import *

header_font = ("Helvetica", 14)
header2_font = ("Helvetica", 12)

def open_labor_factor_setting_window(db, first, last):
    if first != '' and last != '' and db != '':
        

        laborfactor_setting_window = Toplevel()
        laborfactor_setting_window.iconbitmap('Shearon Logo.ico')
        laborfactor_setting_window.title('Settings')
        setting_title = Label(laborfactor_setting_window, text='Labor Factors', font=header_font).grid(row=0,column=2)
        db_name = 'databases/' + str(db) + '.db'
        print(db_name)

        padding_x2 = 5
        padding_y2 = 5


        def resetDefaultFactors():
            print('update default labor factors')
            db_name = 'databases/' + str(db) + '.db'
            print(db_name)
            quart_factor.set(base_factors_dict["quart"])
            gal_factor.set(base_factors_dict["1gal"])
            twogal_factor.set(base_factors_dict["2gal"])
            threegal_factor.set(base_factors_dict["3gal"])
            fivegal_factor.set(base_factors_dict["5gal"])
            sevengal_factor.set(base_factors_dict["7gal"])
            tengal_factor.set(base_factors_dict["10gal"])
            fifteengal_factor.set(base_factors_dict["15gal"])
            twentyfivegal_factor.set(base_factors_dict["25gal"])

            one5_two_factor.set(base_factors_dict["one5inch"])
            two_two5_factor.set(base_factors_dict["twoinch"])
            two5_three_factor.set(base_factors_dict["two5inch"])
            three_three5_factor.set(base_factors_dict["threeinch"])
            three5_four_factor.set(base_factors_dict["three5inch"])
            four_four5_factor.set(base_factors_dict["fourinch"])
            four5_five_factor.set(base_factors_dict["four5inch"])
            five_six_factor.set(base_factors_dict["fiveinch"])
            six_seven_factor.set(base_factors_dict["sixinch"])
            seven_eight_factor.set(base_factors_dict["seveninch"])

            evfour_five_factor.set(base_factors_dict["four5"])
            evfive_six_factor.set(base_factors_dict["five6"])
            evsix_seven_factor.set(base_factors_dict["six7"])
            evseven_eight_factor.set(base_factors_dict["seven8"])
            eveight_ten_factor.set(base_factors_dict["eight10"])
            evten_twelve_factor.set(base_factors_dict["ten12"])
            evtwelve_fourteen_factor.set(base_factors_dict["twelve14"])
            evfourteen_sixteen_factor.set(base_factors_dict["fourteen16"])

            twelve_factor.set(base_factors_dict["twelve"])
            fifteen_factor.set(base_factors_dict["fifteen"])
            eighteen_factor.set(base_factors_dict["eighteen"])
            twentyfour_factor.set(base_factors_dict["twentyfour"])
            thirty_factor.set(base_factors_dict["thirty"])
            thirtysix_factor.set(base_factors_dict["thirtysix"])
            fortyeight_factor.set(base_factors_dict["fortyeight"])


            conn = sqlite3.connect(db_name)
            cur = conn.cursor()
            cur.execute('''DELETE FROM labor_factors''')
            cur.execute('''INSERT INTO labor_factors VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                        ''',(quart_factor.get(), gal_factor.get(), twogal_factor.get(), threegal_factor.get(), fivegal_factor.get(), sevengal_factor.get(), tengal_factor.get(), fifteen_factor.get(), twentyfivegal_factor.get(),
                            one5_two_factor.get(), two_two5_factor.get(), two5_three_factor.get(), three_three5_factor.get(), three5_four_factor.get(), four_four5_factor.get(), four5_five_factor.get(), five_six_factor.get(), six_seven_factor.get(), seven_eight_factor.get(),
                            evfour_five_factor.get(), evfive_six_factor.get(), evsix_seven_factor.get(), evseven_eight_factor.get(), eveight_ten_factor.get(), evten_twelve_factor.get(), evtwelve_fourteen_factor.get(), evfourteen_sixteen_factor.get(),
                            twelve_factor.get(), fifteen_factor.get(), eighteen_factor.get(), twentyfour_factor.get(), thirty_factor.get(), thirtysix_factor.get(), fortyeight_factor.get()))
            conn.commit()

            conn.close()


        def updateFactors():
            
            print('update factors')
            db_name = 'databases/' + str(db) + '.db'
            print(db_name)
            conn = sqlite3.connect(db_name)
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS labor_factors (con_qrt TEXT, con_gal TEXT, con_2gal TEXT, con_3gal TEXT, con_5gal TEXT, con_7gal TEXT, con_10gal TEXT, con_15gal TEXT, con_25gal TEXT,
                        dec_15 TEXT, dec_20 TEXT, dec_25 TEXT, dec_30 TEXT, dec_35 TEXT, dec_40 TEXT, dec_45 TEXT, dec_50 TEXT, dec_60 TEXT, dec_70 TEXT,
                        ever_4 TEXT, ever_5 TEXT, ever_6 TEXT, ever_7 TEXT, ever_8 TEXT, ever_10 TEXT, ever_12 TEXT, ever_14 TEXT,
                        sh_12 TEXT, sh_15 TEXT, sh_18 TEXT, sh_24 TEXT, sh_30 TEXT, sh_36 TEXT, sh_48 TEXT
                        )''')
            cur.execute('''DELETE FROM labor_factors''')
            cur.execute('''INSERT INTO labor_factors VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                        ''',(quart_factor.get(), gal_factor.get(), twogal_factor.get(), threegal_factor.get(), fivegal_factor.get(), sevengal_factor.get(), tengal_factor.get(), fifteen_factor.get(), twentyfivegal_factor.get(),
                            one5_two_factor.get(), two_two5_factor.get(), two5_three_factor.get(), three_three5_factor.get(), three5_four_factor.get(), four_four5_factor.get(), four5_five_factor.get(), five_six_factor.get(), six_seven_factor.get(), seven_eight_factor.get(),
                            evfour_five_factor.get(), evfive_six_factor.get(), evsix_seven_factor.get(), evseven_eight_factor.get(), eveight_ten_factor.get(), evten_twelve_factor.get(), evtwelve_fourteen_factor.get(), evfourteen_sixteen_factor.get(),
                            twelve_factor.get(), fifteen_factor.get(), eighteen_factor.get(), twentyfour_factor.get(), thirty_factor.get(), thirtysix_factor.get(), fortyeight_factor.get()))
            conn.commit()
            ret_cur = cur.execute('''SELECT * FROM labor_factors''').fetchall()
            print(ret_cur)
            conn.close()
            laborfactor_setting_window.destroy()

        db_name = 'databases/' + str(db) + '.db'
        print(db_name)
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS labor_factors (con_qrt TEXT, con_gal TEXT, con_2gal TEXT, con_3gal TEXT, con_5gal TEXT, con_7gal TEXT, con_10gal TEXT, con_15gal TEXT, con_25gal TEXT,
                        dec_15 TEXT, dec_20 TEXT, dec_25 TEXT, dec_30 TEXT, dec_35 TEXT, dec_40 TEXT, dec_45 TEXT, dec_50 TEXT, dec_60 TEXT, dec_70 TEXT,
                        ever_4 TEXT, ever_5 TEXT, ever_6 TEXT, ever_7 TEXT, ever_8 TEXT, ever_10 TEXT, ever_12 TEXT, ever_14 TEXT,
                        sh_12 TEXT, sh_15 TEXT, sh_18 TEXT, sh_24 TEXT, sh_30 TEXT, sh_36 TEXT, sh_48 TEXT
                        )''')
        ret_data = cur.execute('''SELECT * FROM labor_factors WHERE ROWID IN ( SELECT max( ROWID ) FROM labor_factors )''').fetchone()
        
        print(ret_data)
    #Container Labor Factors
        quart_factor= StringVar()
        gal_factor = StringVar()
        twogal_factor = StringVar()
        threegal_factor = StringVar()
        fivegal_factor = StringVar()
        sevengal_factor = StringVar()
        tengal_factor = StringVar()
        fifteengal_factor = StringVar()
        twentyfivegal_factor = StringVar()
        Label(laborfactor_setting_window, text='Container', font=header2_font).grid(row=1, column=0, padx=padding_x2, pady=padding_y2)
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
        two_two5_factor = StringVar()
        two5_three_factor = StringVar()
        three_three5_factor = StringVar()
        three5_four_factor = StringVar()
        four_four5_factor = StringVar()
        four5_five_factor = StringVar()
        five_six_factor = StringVar()
        six_seven_factor = StringVar()
        seven_eight_factor = StringVar()

        Label(laborfactor_setting_window, text='Deciduous Trees', font=header2_font).grid(row=1, column=2, padx=padding_x2, pady=padding_y2)
        Label(laborfactor_setting_window, text='1.5"-2"').grid(row=2, column=2, padx=padding_x2, pady=padding_y2)
        Entry(laborfactor_setting_window, textvariable=one5_two_factor).grid(row=2, column=3, padx=padding_x2, pady=padding_y2)
        Label(laborfactor_setting_window, text='2"-2.5"').grid(row=3, column=2, padx=padding_x2, pady=padding_y2)
        Entry(laborfactor_setting_window, textvariable=two_two5_factor).grid(row=3, column=3, padx=padding_x2, pady=padding_y2)
        Label(laborfactor_setting_window, text='2.5"-3"').grid(row=4, column=2, padx=padding_x2, pady=padding_y2)
        Entry(laborfactor_setting_window, textvariable=two5_three_factor).grid(row=4, column=3, padx=padding_x2, pady=padding_y2)
        Label(laborfactor_setting_window, text='3"-3.5"').grid(row=5, column=2, padx=padding_x2, pady=padding_y2)
        Entry(laborfactor_setting_window, textvariable=three_three5_factor).grid(row=5, column=3, padx=padding_x2, pady=padding_y2)
        Label(laborfactor_setting_window, text='3.5"-4"').grid(row=6, column=2, padx=padding_x2, pady=padding_y2)
        Entry(laborfactor_setting_window, textvariable=three5_four_factor).grid(row=6, column=3, padx=padding_x2, pady=padding_y2)
        Label(laborfactor_setting_window, text='4"-4.5"').grid(row=6, column=2, padx=padding_x2, pady=padding_y2)
        Entry(laborfactor_setting_window, textvariable=four_four5_factor).grid(row=6, column=3, padx=padding_x2, pady=padding_y2)
        Label(laborfactor_setting_window, text='4.5"-5"').grid(row=7, column=2, padx=padding_x2, pady=padding_y2)
        Entry(laborfactor_setting_window, textvariable=four5_five_factor).grid(row=7, column=3, padx=padding_x2, pady=padding_y2)
        Label(laborfactor_setting_window, text='5"-6"').grid(row=8, column=2, padx=padding_x2, pady=padding_y2)
        Entry(laborfactor_setting_window, textvariable=five_six_factor).grid(row=8, column=3, padx=padding_x2, pady=padding_y2)
        Label(laborfactor_setting_window, text='6"-7"').grid(row=9, column=2, padx=padding_x2, pady=padding_y2)
        Entry(laborfactor_setting_window, textvariable=six_seven_factor).grid(row=9, column=3, padx=padding_x2, pady=padding_y2)
        Label(laborfactor_setting_window, text='7"-8""').grid(row=10, column=2, padx=padding_x2, pady=padding_y2)
        Entry(laborfactor_setting_window, textvariable=seven_eight_factor).grid(row=10, column=3, padx=padding_x2, pady=padding_y2)


    #Evergreen Trees Labor Factors
        evfour_five_factor= StringVar()
        evfive_six_factor = StringVar()
        evsix_seven_factor = StringVar()
        evseven_eight_factor = StringVar()
        eveight_ten_factor = StringVar()
        evten_twelve_factor = StringVar()
        evtwelve_fourteen_factor = StringVar()
        evfourteen_sixteen_factor = StringVar()
        Label(laborfactor_setting_window, text='Evergreen Trees', font=header2_font).grid(row=11, column=2, padx=padding_x2, pady=padding_y2)
        Label(laborfactor_setting_window, text="4'-5'").grid(row=12, column=2, padx=padding_x2, pady=padding_y2)
        Entry(laborfactor_setting_window, textvariable=evfour_five_factor).grid(row=12, column=3, padx=padding_x2, pady=padding_y2)
        Label(laborfactor_setting_window, text="5'-6'").grid(row=13, column=2, padx=padding_x2, pady=padding_y2)
        Entry(laborfactor_setting_window, textvariable=evfive_six_factor).grid(row=13, column=3, padx=padding_x2, pady=padding_y2)
        Label(laborfactor_setting_window, text="6'-7'").grid(row=14, column=2, padx=padding_x2, pady=padding_y2)
        Entry(laborfactor_setting_window, textvariable=evsix_seven_factor).grid(row=14, column=3, padx=padding_x2, pady=padding_y2)
        Label(laborfactor_setting_window, text="7'-8'").grid(row=15, column=2, padx=padding_x2, pady=padding_y2)
        Entry(laborfactor_setting_window, textvariable=evseven_eight_factor).grid(row=15, column=3, padx=padding_x2, pady=padding_y2)
        Label(laborfactor_setting_window, text="8'-10'").grid(row=16, column=2, padx=padding_x2, pady=padding_y2)
        Entry(laborfactor_setting_window, textvariable=eveight_ten_factor).grid(row=16, column=3, padx=padding_x2, pady=padding_y2)
        Label(laborfactor_setting_window, text="10'-12'").grid(row=17, column=2, padx=padding_x2, pady=padding_y2)
        Entry(laborfactor_setting_window, textvariable=evten_twelve_factor).grid(row=17, column=3, padx=padding_x2, pady=padding_y2)
        Label(laborfactor_setting_window, text="12'-14'").grid(row=18, column=2, padx=padding_x2, pady=padding_y2)
        Entry(laborfactor_setting_window, textvariable=evtwelve_fourteen_factor).grid(row=18, column=3, padx=padding_x2, pady=padding_y2)
        Label(laborfactor_setting_window, text="14'-16'").grid(row=19, column=2, padx=padding_x2, pady=padding_y2)
        Entry(laborfactor_setting_window, textvariable=evfourteen_sixteen_factor).grid(row=19, column=3, padx=padding_x2, pady=padding_y2)

    #shrubs Trees Labor Factors
        twelve_factor= StringVar()
        fifteen_factor = StringVar()
        eighteen_factor = StringVar()
        twentyfour_factor = StringVar()
        thirty_factor = StringVar()
        thirtysix_factor = StringVar()
        fortyeight_factor = StringVar()

        Label(laborfactor_setting_window, text='Shrubs', font=header2_font).grid(row=1, column=4, padx=padding_x2, pady=padding_y2)
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
        Label(laborfactor_setting_window, text='36"-48"').grid(row=8, column=4, padx=padding_x2, pady=padding_y2)
        Entry(laborfactor_setting_window, textvariable=thirtysix_factor).grid(row=8, column=5, padx=padding_x2, pady=padding_y2)
        Label(laborfactor_setting_window, text='48"-46"').grid(row=9, column=4, padx=padding_x2, pady=padding_y2)
        Entry(laborfactor_setting_window, textvariable=fortyeight_factor).grid(row=9, column=5, padx=padding_x2, pady=padding_y2)

        Button(laborfactor_setting_window, text='Save Factors', command=updateFactors).grid(row=20, column=5, padx=padding_x2, pady=padding_y2)
        Button(laborfactor_setting_window, text='Reset Deffault Factors', command=resetDefaultFactors).grid(row=20, column=4, padx=padding_x2, pady=padding_y2)

        laborfactor_data = cur.execute('''SELECT * FROM labor_factors ORDER BY ROWID DESC LIMIT 1''').fetchone()
        if laborfactor_data == None:

            quart_factor.set(base_factors_dict["quart"])
            gal_factor.set(base_factors_dict["1gal"])
            twogal_factor.set(base_factors_dict["2gal"])
            threegal_factor.set(base_factors_dict["3gal"])
            fivegal_factor.set(base_factors_dict["5gal"])
            sevengal_factor.set(base_factors_dict["7gal"])
            tengal_factor.set(base_factors_dict["10gal"])
            fifteengal_factor.set(base_factors_dict["15gal"])
            twentyfivegal_factor.set(base_factors_dict["25gal"])

            one5_two_factor.set(base_factors_dict["one5inch"])
            two_two5_factor.set(base_factors_dict["twoinch"])
            two5_three_factor.set(base_factors_dict["two5inch"])
            three_three5_factor.set(base_factors_dict["threeinch"])
            three5_four_factor.set(base_factors_dict["three5inch"])
            four_four5_factor.set(base_factors_dict["fourinch"])
            four5_five_factor.set(base_factors_dict["four5inch"])
            five_six_factor.set(base_factors_dict["fiveinch"])
            six_seven_factor.set(base_factors_dict["sixinch"])
            seven_eight_factor.set(base_factors_dict["seveninch"])

            evfour_five_factor.set(base_factors_dict["four5"])
            evfive_six_factor.set(base_factors_dict["five6"])
            evsix_seven_factor.set(base_factors_dict["six7"])
            evseven_eight_factor.set(base_factors_dict["seven8"])
            eveight_ten_factor.set(base_factors_dict["eight10"])
            evten_twelve_factor.set(base_factors_dict["ten12"])
            evtwelve_fourteen_factor.set(base_factors_dict["twelve14"])
            evfourteen_sixteen_factor.set(base_factors_dict["fourteen16"])

            twelve_factor.set(base_factors_dict["twelve"])
            fifteen_factor.set(base_factors_dict["fifteen"])
            eighteen_factor.set(base_factors_dict["eighteen"])
            twentyfour_factor.set(base_factors_dict["twentyfour"])
            thirty_factor.set(base_factors_dict["thirty"])
            thirtysix_factor.set(base_factors_dict["thirtysix"])
            fortyeight_factor.set(base_factors_dict["fortyeight"])

        else:
            quart_factor.set(laborfactor_data[0])
            gal_factor.set(laborfactor_data[1])
            twogal_factor.set(laborfactor_data[2])
            threegal_factor.set(laborfactor_data[3])
            fivegal_factor.set(laborfactor_data[4])
            sevengal_factor.set(laborfactor_data[5])
            tengal_factor.set(laborfactor_data[6])
            fifteengal_factor.set(laborfactor_data[7])
            twentyfivegal_factor.set(laborfactor_data[8])

            one5_two_factor.set(laborfactor_data[9])
            two_two5_factor.set(laborfactor_data[10])
            two5_three_factor.set(laborfactor_data[11])
            three_three5_factor.set(laborfactor_data[12])
            three5_four_factor.set(laborfactor_data[13])
            four_four5_factor.set(laborfactor_data[14])
            four5_five_factor.set(laborfactor_data[15])
            five_six_factor.set(laborfactor_data[16])
            six_seven_factor.set(laborfactor_data[17])
            seven_eight_factor.set(laborfactor_data[18])

            evfour_five_factor.set(laborfactor_data[19])
            evfive_six_factor.set(laborfactor_data[20])
            evsix_seven_factor.set(laborfactor_data[21])
            evseven_eight_factor.set(laborfactor_data[22])
            eveight_ten_factor.set(laborfactor_data[23])
            evten_twelve_factor.set(laborfactor_data[24])
            evtwelve_fourteen_factor.set(laborfactor_data[25])
            evfourteen_sixteen_factor.set(laborfactor_data[26])

            twelve_factor.set(laborfactor_data[27])
            fifteen_factor.set(laborfactor_data[28])
            eighteen_factor.set(laborfactor_data[29])
            twentyfour_factor.set(laborfactor_data[30])
            thirty_factor.set(laborfactor_data[31])
            thirtysix_factor.set(laborfactor_data[32])
            fortyeight_factor.set(laborfactor_data[33])
        

        


        conn.close()


    else:
        messagebox.showwarning("showwarning", "Missing Fields")

    