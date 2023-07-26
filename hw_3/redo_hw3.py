'''
Goal of this project to use libraries to read and analyze fitness data from each category of csv_input.csv across mean, median and range
Use statistics library: https://docs.python.org/3/library/statistics.html 
Write a function that takes in list as a parameter and returns the range (min value subtracted from max value) to find the range.
range = max value - min value  | diff between highest and lowest numbers

Extra Challenge:
Write values into a new csv with the mean, median and range for each category of data in this format:

mean steps      median steps        range steps     mean active Hr  median active hr    range active hr mean resting hr median resting hr and range resting hr

calculations listed below each category

mean() # average of data
median() # middle value of data
range() # from beginning or set number to the number before the declared end number

Think of a problem in your life that you could use python to address and spend 10 min+ looking for a library in that field
'''

import csv
import statistics

#define lists that will store data we read from the csv into the specific categories
dates = []
steps = []
rest_hr = []
act_hr = []
mean_rhr = []
median_rhr = []
range_rhr = []
mean_ahr = []
median_ahr = []
range_ahr = []

#created variable for header names and am using this variable to print all the headers names below
header_names = ['Date', 'Steps', 'RstHr', 'ActHr']

#Function to calculate the range   
def calculate_range(data):
    max_data = max(data)
    min_data = min(data)
    return max_data - min_data 
   
def calc_mean_steps():
    # Calculate the mean/avg steps in a week using Statistics library
    mean = statistics.mean(steps)
    print("Mean/Avg steps in a week:", mean)
    
def calc_median_steps():
    # Calculate the median using Statistics library
    median = statistics.median(steps)
    print("Median:", median)

    
#created a function for adding data
def add_data():
    print(header_names)  
    for row in reader:
        if row[0] != 'Date':
            dates.append(row[0]) # this is the first column in each row
            steps.append(int(row[1])) # add steps data to the list
            rest_hr.append(int(row[2])) # add resting heart rate data to the list
            act_hr.append(int(row[3])) # add active heart rate data to the list
            print(row)  #printing data for each row
     
#open the csv file and each 'row' is a list of the data in the same order as the columns in the csv.
with open('csv_input.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0] != 'Date':
            dates.append(row[0])
            steps.append(int(row[1]))
            rest_hr.append(int(row[2]))
            act_hr.append(int(row[3]))
            add_data()
calc_mean_steps()
calc_median_steps()
print('Range of steps: ', calculate_range(steps))     

def calc_mean_ahr():
    # Calculate the mean using Statistics library
    mean = statistics.mean(act_hr)
    print("Mean Active hr:", mean)

def calc_median_ahr():
    median = statistics.median(act_hr)
    print("Median Active hr:", median)

    
def calc_mean_rhr():
    mean = statistics.mean(rest_hr)  
    print("Mean Resting HR: ", mean)
    
def calc_median_rhr():
    median = statistics.median(rest_hr)
    print("Median Resting Hr: ", median)
    
new_headers = (['Mean Steps', 'Median Steps', 'Range Steps',  
                'Mean RstHr', 'Median RstHr', 'Range RstHr', 
                'Mean ActHr', 'Median ActHr', 'Range ActHr'])

row_data = [
            statistics.mean(steps), statistics.median(steps), calculate_range(steps), 
            statistics.mean(rest_hr), statistics.median(rest_hr), calculate_range(rest_hr),
            statistics.mean(act_hr), statistics.median(act_hr), calculate_range(act_hr)
        ]         

# def write_to_csv():
with open('redo_hw3_input.csv', "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(new_headers)
    writer.writerow(row_data)
            
print('Range for Resting Hr: ', calculate_range(rest_hr))
print('Range for Active Hr: ', calculate_range(act_hr))


     