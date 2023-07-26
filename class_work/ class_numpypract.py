import csv
import numpy as np


opens = []
dates = []

def predict(day, coeffs):
    return coeffs[0] * day * coeffs[1]

with open('AAPL.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for idx, row in enumerate(reader): #assign two variables with enumerate
        opens.append(float(row[1]))
        dates.append(int(idx))

coeffs = np.polyfit(dates, opens, 1)
print("I can predict the Apple stock for you on a specific day")
what_day = int(input("Tell me the day by how many days after7/16/2018: "))
print(predict(what_day, coeffs))