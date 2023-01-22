import pandas as pd
import os


# TODO append args to existing dataframe
filename = "made_up_fishes.csv"
if os.path.exists(filename):
    df = pd.read_csv(filename)
else:
    made_up_names = [
        "Gorpedon",
        "Thunbul",
        "Seemoewenfisch",
        "Satyr",
        "Barball",
        "Zote",
        "Grasfisch",
        "Schwimmkrebs",
        "Marmorperl",
        "Laichbarsch",
        "Koniksalmler",
        "Schläucherling",
        "Flußschläfer",
        "Lappenzander",
        "Gemeiner Luftschnapper",
    ]
    df = pd.DataFrame(made_up_names, columns=['name'])

df.to_csv(filename)