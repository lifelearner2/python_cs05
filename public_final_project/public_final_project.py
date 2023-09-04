"""
phue by Nathanaël Lécaudé - A Philips Hue Python library
Contributions by Marshall Perrin, Justin Lintz
https://github.com/studioimaginaire/phue
Original protocol hacking by rsmck : http://rsmck.co.uk/hue

Published under the MIT license - See LICENSE file for more details.

"Hue Personal Wireless Lighting" is a trademark owned by Koninklijke Philips Electronics N.V., see www.meethue.com for more information.
I am in no way affiliated with the Philips organization.
-------------------------------------------------------------------------------------------------------------------------------------------------------
The following concepts are required in your program, how you use them is up to you:

if statement - DONE
for loop or while loop - DONE
function - DONE
dictionary or list - DONE
analysis/sorting of data or inputs (CSV or user input) - DONE
python library/libraries (native and/or non-native) - DONE

This version of my code omits my actual ip address (variable 'b') for public posting. Using a placeholder so this code will not run until an ip address is put in.
"""
#!/usr/bin/python

from phue import Bridge #non-native library provides functionalities to interact with Phillips Hue Lights and Bridges
import random #native python library allows population of random colors
import csv #python library to allow for csv file storage
import json #python library for data
import datetime #python library that allows for accessing date and time

#bridge ip address for connection setup
# b = Bridge('ip address removed for github')

#placeholder for bridge ip address
ip_address = Bridge("your_ip_here")


# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
#If running for the first time, press button on bridge and run with b.connect() uncommented
#b.connect()

#Headers for the CSV file
headers = ['Light ID', 'Light State', 'Random Colors', 'Usage Duration']
print(headers)

#initialize dictionary to store usage info for each light (I only have one at this time)
light_usage_info = {}

#defining list to store info on random colors
random_colors = []

#created variable defined with the light name and state
# light_state = b.get_light('Floor Light', 'on') #removing this to use placeholder for ip
light_state = ip_address.get_light('Floor Light', 'on')

#Function to initialize light usage info
def create_light_data(lights):
    light_info = {}
    #for each light, turn the brightness up to 254(max) and make the color change to a random color each time the code runs
    for light in lights:
        light.brightness = 254 
        light.xy = [random.random(),random.random()] #this needs both parameters if you do .xy but if only .x & one parameter then the light color isn't changed or at random.
        light_state = light.on
        random_colors = light.xy
     
        #light_state is equal to light.on - so if this is true do the following
        if light_state: 
            light_id = light.light_id
            # Get the current time when the light is turned on
            start_time = datetime.datetime.now()
            light_info[light_id] = {
                'start_time': start_time, 
                'random_colors': random_colors
                } 
    return light_info

#Get list of light objects
# lights = b.get_light_objects() #removing this to use placeholder code
lights = ip_address.get_light_objects() 
# Call the function to initialize light usage info
light_usage_info = create_light_data(lights)

#Iterating through dictionary items and printing usage info for each light
for light_id, usage_info in light_usage_info.items():
    start_time = usage_info["start_time"]
    #assuming end_time is current time when loop is running
    end_time = datetime.datetime.now() 
    #calculate usage duration in seconds
    usage_duration = (end_time - start_time).total_seconds()
    random_colors = usage_info["random_colors"]
    print(f"Light ID: {light_id}")
    print(f"Start Time: {start_time}")
    print(f"End Time: {end_time}")
    print(f"Usage duration: {usage_duration: .2f} seconds")
    print(f"Random Colors: {random_colors}")
        
# Get the bridge state (This returns the full dictionary to explore)
# b.get_api() 
# api = b.get_api()
ip_address.get_api() 
api = ip_address.get_api()
print()
print(api)
print()

# Use the light_state variable to check if the light is on or off - it will say True if it's on or False if it's off (but the light will turn on dimly when code is ran if it's off)
print("The Bedroom Floor Light state is: ", light_state) 

# Get a dictionary with the light id as the key
# lights = b.get_light_objects('id') #removed to use placeholder
lights = ip_address.get_light_objects('id')

# The set_light method can also take a dictionary as the second argument to do more fancy stuff
# This will turn Floor Light on with a transition time of 30 seconds - this only works if the light is already off - once light is on and I run code it will change color but transition only runs when starts at off 
command =  {'transitiontime' : 300, 'on' : True, 'bri' : 254}
# b.set_light('Floor Light', command) #using placeholder for ip address below
ip_address.set_light('Floor Light', command) 

#iterating through light_usage_info and writing data to  csv file           
with open('light_usage.csv', "w", newline='') as csvfile:
    writer = csv.writer(csvfile)   
    writer.writerow(headers)
    for light_id, usage_info in light_usage_info.items():
        start_time = usage_info['start_time']
        end_time = datetime.datetime.now()
        usage_duration = (end_time - start_time).total_seconds()
        random_colors = ', '.join(map(str, usage_info['random_colors']))  # Use random_colors from usage_info
        writer.writerow([light_id, light_state, random_colors, usage_duration])     

# Read and print the contents of the CSV
with open('light_usage.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)








