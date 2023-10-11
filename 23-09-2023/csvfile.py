import csv

file_path = "C:/Users/athar/oneDrive/Desktop/Python Machine Learning/23-09-2023/example1.csv"

data = [
    {"ID": "atharvagujarathi92@gmail.com"},
    {"ID": "gujjya92@gmail.com"},
    {"ID": "atharvagujarathi68@gmail.com"},
    {"ID": "akgujarathi92@gmail.com"}
]

with open(file_path, mode='w', newline='') as file:
    fieldnames = data[0].keys()  # Assuming all dictionaries have the same keys
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()  # Write the header row with field names
    for row in data:
        writer.writerow(row)

