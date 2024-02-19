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
        servicefactor_setting_window.geometry('700x450')

        setting_title = Label(servicefactor_setting_window, text='Labor Factors', font=header_font).grid(row=0,column=1)

        db_name = 'databases/' + str(db) + '.db'
        print(db_name)

        

        padding_x2 = 5
        padding_y2 = 5

        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS service_labor_factors (mulch TEXT, soil TEXT, stone TEXT, flagstone TEXT, sixbysixbyeight_footer TEXT, sixbysixbyeight_course TEXT, paver TEXT, ads_4inchpipe TEXT,
                        tilling TEXT, sod_prepped TEXT, sod_unprepped TEXT, sod_prepped_1wide TEXT, sod_prepped_3wide TEXT, sodcutter TEXT,
                        six_upright TEXT, eight_upright TEXT, guywire_2ft TEXT, turnbuckle TEXT
                        )''')
        ret_data = cur.execute('''SELECT * FROM service_labor_factors WHERE ROWID IN ( SELECT max( ROWID ) FROM service_labor_factors )''').fetchone()
        
        print(ret_data)

        

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

        def updateFactors():
            
            print('update factors')
            db_name = 'databases/' + str(db) + '.db'
            print(db_name)
            conn = sqlite3.connect(db_name)
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS service_labor_factors (mulch TEXT, soil TEXT, stone TEXT, flagstone TEXT, sixbysixbyeight_footer TEXT, sixbysixbyeight_course TEXT, paver TEXT, ads_4inchpipe TEXT,
                        tilling TEXT, sod_prepped TEXT, sod_unprepped TEXT, sod_prepped_1wide TEXT, sod_prepped_3wide TEXT, sodcutter TEXT,
                        six_upright TEXT, eight_upright TEXT, guywire_2ft TEXT, turnbuckle TEXT
                        )''')
            cur.execute('''DELETE FROM service_labor_factors''')
            cur.execute('''INSERT INTO service_labor_factors VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                        ''', (mulch_factor.get(), soil_factor.get(), stone_factor.get(), flagstone_factor.get(), sixbysixbyeight_footer_factor.get(), sixbysixbyeight_course_factor.get(), paver_factor.get(), ads_4pipe_factor.get(),
                            groundtilling_factor.get(), sodprepared_factor.get(), sodunprepared_factor.get(), sodprepared_onewide_factor.get(), sodprepared_threewide_factor.get(), sodcutter.get(),
                            sixfoot_upright_factor.get(), eightfoot_upright_factor.get(), twofoot_guywire_factor.get(), sixinch_turnbuckle_factor.get()
                        ))
            conn.commit()
            ret_cur = cur.execute('''SELECT * FROM service_labor_factors''').fetchall()
            print(ret_cur)
            conn.close()
            servicefactor_setting_window.destroy()

        def resetDefaultFactors():
            print('update default service  labor factors')
            db_name = 'databases/' + str(db) + '.db'
            print(db_name)
            mulch_factor.set(base_service_factors["mulch_1yard"])
            soil_factor.set(base_service_factors["soil_1yard"])
            stone_factor.set(base_service_factors["stone_1yard"])
            flagstone_factor.set(base_service_factors["flagstone_100sqft_4inchbase"])
            sixbysixbyeight_footer_factor.set(base_service_factors["sixbysixbyeight_footer"])
            sixbysixbyeight_course_factor.set(base_service_factors["sixbysixbyeight_course"])
            paver_factor.set(base_service_factors["paver_100sqft_4inchbase"])
            ads_4pipe_factor.set(base_service_factors["pipe_4inchx10ft"])
            groundtilling_factor.set(base_service_factors["tilling_100sqft"])
            sodprepared_factor.set(base_service_factors["sod_500sqft_preppped"])
            sodunprepared_factor.set(base_service_factors["sod_500sqft_unprepped"])
            sodprepared_onewide_factor.set(base_service_factors["sod_prepped_1wide"])
            sodprepared_threewide_factor.set(base_service_factors["sod_prepped_3wide"])
            sodcutter.set(base_service_factors["sodcutter_100sqft"]),
            sixfoot_upright_factor.set(base_service_factors["six_upright"])
            eightfoot_upright_factor.set(base_service_factors["eight_upright"])
            twofoot_guywire_factor.set(base_service_factors["guywire_2ft"])
            sixinch_turnbuckle_factor.set(base_service_factors["turnbuckle"])

            conn = sqlite3.connect(db_name)
            cur = conn.cursor()
            cur.execute('''DELETE FROM service_labor_factors''')
            cur.execute('''INSERT INTO service_labor_factors VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                        ''',(mulch_factor.get(), soil_factor.get(), stone_factor.get(), flagstone_factor.get(), sixbysixbyeight_footer_factor.get(), sixbysixbyeight_course_factor.get(), paver_factor.get(), ads_4pipe_factor.get(),
                            groundtilling_factor.get(), sodprepared_factor.get(), sodunprepared_factor.get(), sodprepared_onewide_factor.get(), sodprepared_threewide_factor.get(), sodcutter.get(),
                            sixfoot_upright_factor.get(), eightfoot_upright_factor.get(), twofoot_guywire_factor.get(), sixinch_turnbuckle_factor.get()
                        ))
            conn.commit()

            conn.close()



        Button(servicefactor_setting_window, text='Save Factors', command=updateFactors).grid(row=12, column=3, padx=padding_x2, pady=padding_y2)
        Button(servicefactor_setting_window, text='Reset Deffault Factors', command=resetDefaultFactors).grid(row=12, column=2, padx=padding_x2, pady=padding_y2)


        laborfactor_data = cur.execute('''SELECT * FROM service_labor_factors ORDER BY ROWID DESC LIMIT 1''').fetchone()
        if laborfactor_data == None:
            mulch_factor.set(base_service_factors["mulch_1yard"])
            soil_factor.set(base_service_factors["soil_1yard"])
            stone_factor.set(base_service_factors["stone_1yard"])
            flagstone_factor.set(base_service_factors["flagstone_100sqft_4inchbase"])
            sixbysixbyeight_footer_factor.set(base_service_factors["sixbysixbyeight_footer"])
            sixbysixbyeight_course_factor.set(base_service_factors["sixbysixbyeight_course"])
            paver_factor.set(base_service_factors["paver_100sqft_4inchbase"])
            ads_4pipe_factor.set(base_service_factors["pipe_4inchx10ft"])
            groundtilling_factor.set(base_service_factors["tilling_100sqft"])
            sodprepared_factor.set(base_service_factors["sod_500sqft_preppped"])
            sodunprepared_factor.set(base_service_factors["sod_500sqft_unprepped"])
            sodprepared_onewide_factor.set(base_service_factors["sod_prepped_1wide"])
            sodprepared_threewide_factor.set(base_service_factors["sod_prepped_3wide"])
            sodcutter.set(base_service_factors["sodcutter_100sqft"]),
            sixfoot_upright_factor.set(base_service_factors["six_upright"])
            eightfoot_upright_factor.set(base_service_factors["eight_upright"])
            twofoot_guywire_factor.set(base_service_factors["guywire_2ft"])
            sixinch_turnbuckle_factor.set(base_service_factors["turnbuckle"])
        else:
            mulch_factor.set(laborfactor_data[0])
            soil_factor.set(laborfactor_data[1])
            stone_factor.set(laborfactor_data[2])
            flagstone_factor.set(laborfactor_data[3])
            sixbysixbyeight_footer_factor.set(laborfactor_data[4])
            sixbysixbyeight_course_factor.set(laborfactor_data[5])
            paver_factor.set(laborfactor_data[6])
            ads_4pipe_factor.set(laborfactor_data[7])
            groundtilling_factor.set(laborfactor_data[8])
            sodprepared_factor.set(laborfactor_data[9])
            sodunprepared_factor.set(laborfactor_data[10])
            sodprepared_onewide_factor.set(laborfactor_data[11])
            sodprepared_threewide_factor.set(laborfactor_data[12])
            sodcutter.set(laborfactor_data[13]),
            sixfoot_upright_factor.set(laborfactor_data[14])
            eightfoot_upright_factor.set(laborfactor_data[15])
            twofoot_guywire_factor.set(laborfactor_data[16])
            sixinch_turnbuckle_factor.set(laborfactor_data[17])

        conn.close()

        

        
    else:
        messagebox.showwarning("showwarning", "Missing Fields")

    


    