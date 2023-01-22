import warnings
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import argparse
import sys

parser = argparse.ArgumentParser(
                    # prog = 'ProgramName',
                    # description = 'What the program does',
                    # epilog = 'Text at the bottom of help'
                    )
parser.add_argument('-e', '--export', action='store_true')  # on/off flag
parser.add_argument('--filename', default="fischarten.csv")


args = parser.parse_args()

make_csv = lambda fn: f"{fn}.csv" if fn.split(".")[-1] != "csv" else fn


EXPORT = args.export
FILENAME = make_csv(args.filename)

url = "https://de.wikipedia.org/wiki/Liste_europ%C3%A4ischer_S%C3%BC%C3%9Fwasserfische_und_Neunaugen"

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="bodyContent")

is_latin_name = lambda s: True if "(" not in s else False

def remove_numbers(s):
    out = ""
    for c in s:
        if not c.isdigit():
            out += c
    return out

species_with_german_name = []
species = results.find_all("li")
for s in species[:-9]: # ignore lis on bottom
    if not is_latin_name(s.text):
        species_with_german_name.append(remove_numbers(s.text.split(" (")[0]).lstrip())


df = pd.DataFrame (species_with_german_name, columns = ['name'])





def check_answer():
    yes = {'yes','y', 'ye', ''}
    no = {'no','n'}

    choice = input().lower()
    if choice in yes:
       return True
    elif choice in no:
       return False
    else:
       sys.stdout.write("Please run again and respond with  either 'yes' or 'no'")


if EXPORT:
    if os.path.exists(FILENAME):
        sys.stdout.write(f"File {FILENAME} already exists...\nPlease type yes if you want to overwrite the existing file {FILENAME}. Type 'no' if you want to keep the existing file.\n")
        overwrite = check_answer()
        if overwrite:
            sys.stdout.write(f"\nOverwriting existing file {FILENAME}...\n")
            df.to_csv(FILENAME)
        else:
            sys.stdout.write(f"\nKeeping {FILENAME}...\n")
    else:
        sys.stdout.write(f"\nSaving parsed data to {FILENAME}...\n")
        df.to_csv(FILENAME)
