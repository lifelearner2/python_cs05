import requests
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt

def scrape_global_temperature(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the element with the class "year-to-date"
        year_to_date_element = soup.find('caption', {'class': 'year-to-date'})

        if year_to_date_element:
            # Assuming the temperature data is in the next sibling element
            temperature_data_element = year_to_date_element.find_next_sibling('div')

            if temperature_data_element:
                temperature_text = temperature_data_element.get_text(strip=True)
                temperature = float(temperature_text.split()[0])  # Extract temperature value

                return temperature

            else:
                print("Global temperature data not found. Please check the HTML structure of the 'year-to-date' section.")
                return None
        else:
            print("Class 'year-to-date' not found. Please check the HTML structure or the URL.")
            return None

    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
        return None

if __name__ == '__main__':
    url = 'https://www.ncei.noaa.gov/access/monitoring/monthly-report/global/202013#:~:text=The%20global%20annual%20temperature%20has,0.32°F)%20since%201981.'
    global_temperature = scrape_global_temperature(url)

    if global_temperature:
        print(f"Global Temperature: {global_temperature} °F")
    else:
        print("Failed to fetch global temperature data.")
