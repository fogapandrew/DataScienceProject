import utilities
import os

# Get the absolute path for data using the getfilepath from the utilities class.
DATA_DIR = utilities.getfilepath()

# getting the path for the raw data file()
filepath = os.path.join(DATA_DIR, 'rawdata', 'heart.csv')

try:
    # Using importdata method from the utilities to import read in the file as a dataframe.
    Rawdata = utilities.importdata(filepath)
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")
