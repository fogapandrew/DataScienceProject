import Utilities
import os

print("Current Working Directory:", os.getcwd())

DATA_DIR = Utilities.getfilepath()

filepath = os.path.join(DATA_DIR, 'rawdata', 'heart.csv')

print(filepath)

Rawdata = Utilities.importdata(filepath)

