

all_entries = []

plant_categories = {
            'container': ['quart', '1gal', '2gal', '3gal', '5gal', '7gal', '10gal', '15gal', '25gal'], 
            'deciduous trees':['1.5"-2"', '2"-2.5"', '2.5"-3"', '3"-3.5"', '3.5"-4"'], 
            'evergreen trees':["4'-5'", "5'-6'", "6'-7'", "7'-8'", "8'-9'", "9'-10'"],
            'shrubs': ['12"-15"', '15"-18"', '18"-24"', '24"-30"', '30"-36"', '36"-40"']}
base_labor_factors = ['0.10', '0.15', '0.20', '0.35', '0.45', '0.50', '0.60', '0.45', '0.75' ,'2.0', '2.5', '3.0', '3.5', '4.0', '2.0', '2.5','3.0', '3.5','4.0','5.0','0.35','0.45','0.55','0.65','0.70','0.80', '0.90']
base_factors_dict = {
        "quart": "0.01",
        "1gal" : "0.033",
        "2gal" : "0.05",
        "3gal" : "0.09",
        "5gal" : "0.15",
        "7gal" : "0.40",
        "10gal" : "0.60",
        "15gal" : "0.80",
        "25gal" : "1.50",
        "one5inch" : "1.3",
        "twoinch" : "1.6",
        "two5inch" : "2.1",
        "threeinch" : "2.4",
        "three5inch" : "2.8",
        "fourinch" : "3.5",
        "four5inch" : "3.7",
        "fiveinch" : "4.5",
        "sixinch" : "5.75",
        "seveninch" : "6.75",
        "four5" : "0.65",
        "five6" : "1.0",
        "six7" : "1.2",
        "seven8" : "1.5",
        "eight10" : "1.7",
        "ten12" : "2.5",
        "twelve14" : "3.15",
        "fourteen16" : "3.65",
        "twelve" : "0.12",
        "fifteen" : "0.14",
        "eighteen" : "0.19",
        "twentyfour" : "0.24",
        "thirty" : "0.29",
        "thirtysix" : "0.39",
        "fortyeight" : "0.45"
                        }

grid_rows = 3