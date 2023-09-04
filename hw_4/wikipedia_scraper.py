import requests
from bs4 import BeautifulSoup
import csv
import numpy as np

headers = ['Country', 'Capital', 'Language']


def scrape_wikipedia(url):
    # Send an HTTP GET request to fetch the webpage content
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find the table that contains the list of countries and currencies
        tables = soup.find('table', {'class': 'wikitable'})

        all_data = [] #A list to store data from all tables
        
      
        print(headers) 
        for table in tables:
            # Initialize a list to store the data
            country_info = []
            if table:
                # Loop through each row in the table (skip the header row)  
                for row in tables.find_all('tr')[1:]:
                    columns = row.find_all('td')
                    country = columns[0].text.strip()
                    capital = columns[1].text.strip()
                    language = columns[4].text.strip() 
                    country_info.append((country, capital, language))
            else:
                print("Table not found on the page. Please check the HTML structure or the URL.")
            all_data.append(country_info) #Append data of each table to the all_data list
        
        return country_info
             

    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
        return None

if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_and_their_capitals_in_native_languages'  
    data = scrape_wikipedia(url)

    if data:
        # Print the list of countries and currencies
        for country, capital, language in data:
            print(f"{country}: {capital} {language}")


country_stats = data

with open('country_stats_output.csv', "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    for entry in country_stats:
        writer.writerow(entry)
