import csv

with open("excel.csv") as data:
    csv_list = csv.reader(data)
    for row in csv_list:
        device = row[0]
        location = row[2]
        IP = row[1]
        print(f"{device} is in {location.rstrip()} and has IP {IP}.")
