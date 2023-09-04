'''
First: Crawl the web for a dataset that you are interested in. Could be a company’s stock, temperature in a town over the last few years, the price of Coca-Cola over the years, etc, download as csv.

Next: Create a trend line (degree 1) to fit to the data with numpy. Then estimate the future values, bonus if you allow users to ask for specific future values.

You can reference the python file from this past lecture found on the Files page

Finally: Play around with different degrees to get a good fit
'''  # noqa: E501

import csv
import numpy as np

#defining lists to store info
death_day = []
natural_causes = []

#open the csv file and each 'row' is a list of the data in the same order as the columns in the csv.  
with open('death_input_stats.csv') as csvfile:
    reader = csv.reader(csvfile)  #read file
    next(reader)  # Skip the header row
    for idx, row in enumerate (reader): #iterate through the indexed list of rows of the csv file  
        #append the info to the list
        death_day.append(int(row[2])) #getting info from that index position and adding to list 
        natural_causes.append(int(row[10]))
            
headers = ['Day of Death', 'Natural Causes']
print(headers)

death_data = list(zip(death_day, natural_causes))

#write to  csv file           
with open('death_output.csv', "w", newline='') as csvfile:
     writer = csv.writer(csvfile)   
     writer.writerow(headers)
     for entry in death_data:
         writer.writerow(entry)

#degree is the line that on the graph to represent the median area and trajectory of the numbers - 1 is a diagonal line up but 2 would be a curved line.
degree = 1        
      
#calculate the coefficients of the line of best fit, to view import mathplotlib 
coeffs = np.polyfit(death_day, natural_causes, degree)

#function to predict how many will die of natural causes on a given day
def predict(day, coeffs):
    #return the predicted number of natural deaths for the given day
    return coeffs[0]*day + coeffs[1]
        
print('This shows how many people died of natural causes on this day of the month in the United States between 2019 and 2021.', death_data)  

what_day = int(input('What day would you like to predict? (Enter a number between 0 and 251) '))  

print('The predicted deaths by natural causes for day ' + str(what_day) + ' is ' + str(predict(what_day, coeffs)))  
     