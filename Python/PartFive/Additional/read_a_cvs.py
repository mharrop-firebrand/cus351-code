# Text files aren’t the only thing that Python can read, but they’re the only thing that we don’t need any additional parsing library to understand

# CSV files are an example of a text file that impose a structure to their data

# CSV stands for Comma-Separated Values and CSV files are usually the way that data from spreadsheet software (like Microsoft Excel or Google Sheets) is exported into a portable format
import os

file_path = r"C:\Users\mharrop\OneDrive - Firebrand Training Limited\Documents\Teaching\Python\FBA-Python - SE-C52-P\Python_day_four_m5_p2\Additional\read_file.csv"

if os.path.exists("file_path"):
    with open(file_path, "r") as file:
        print(file.read())
    file.close()
