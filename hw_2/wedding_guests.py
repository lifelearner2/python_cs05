
'''
Assignment: group the given guests by bride and groom. Your final output should be
two variables that each represent a list of guests,
one for "bride" and one for "groom"
'''
#All guests listed in key/value pairs in dictionaries within a list. I added a role description to the key and value so that it makes more sense and is easier to access
guest_list = [
    {'Name': 'Albert Einstein', 'supporting': 'bride'}, 
    {'Name': 'Alfred Pennyworth', 'supporting': 'bride'}, 
    {'Name': 'Anthony Cleopatra', 'supporting': 'groom'}, 
    {'Name': 'Ben Frank', 'supporting': 'bride'}, 
    {'Name': 'Ben Button', 'supporting': 'groom'}, 
    {'Name': 'Charlie Bucket', 'supporting': 'groom'}, 
    {'Name': 'David Attenborough', 'supporting': 'bride'}
]
 
#Two variables with an empty list for bride guests and a list for groom guests
bride = []
groom = []

#iterating over the guest list and then accessing the name and supporting values within each dictionary/guest
#guest represents the "key" and guest_list represents the "dictionary"
for guest in guest_list: 
    name = guest['Name']  #accessing the value('Name') and assigning it to this variable
    supporting = guest['supporting']   #storing value of supporting party to this variable
    #checking to see who they are supporting and appending the guests to the appropriate list based on who they are supporting
    if supporting == 'bride':   
        bride.append(guest)  #current guest dictionary is appended/added to the brides list
    elif supporting == 'groom':
        groom.append(guest)    
       
print() # For readability - I like to print and empty space line before/between and after the lists
print('Brides List: ' , bride)
print()
print('Grooms List: ' , groom)
print()            
  
#Extra Challenge (optional): add code for users to input guests by name and either
bride or groom,


#variable created for goodbye message - will be displayed if they type q to not enter any more guests
goodbye_message = "Thank you, see you at the wedding!"

#variable to determine if the while loop will continue to run (I got help for this part)
add_more = True

#starts while loop until add_more variable is set to false 
#could have also used while True instead of add_more variable
while add_more:
    #asks user to enter guest and either bride or groom and stores that info in variable called user_guest and gives them the option to enter again or quit
    user_guest = input("Enter guest name and who they are supporting (use this format - 'Jane: bride') or type 'q' to quit: ")    
    #check to see if user wants to quit
    if user_guest == 'q':
        add_more = False #if user says to quit then this will be set to false to stop the while loop
        print(goodbye_message)
        break  #exit the code immediately after printing the goodbye message - so it won't still print a list with 'q' added to the list.
    
    #extracting values from the user guest list like we did from guest list (I sought help for this part)
    else:
        guest_info = user_guest.split(':')  #splits the user_guest input at the colon and stores the parts into guest_info 
        name = guest_info[0].strip()    #extracts name from guest_info by accessing index 0 and removes whitespace using the method
        supporting = guest_info[1].strip()
        
    if supporting == 'bride':
        bride.append(user_guest) # guest name is appended/added to the list
        #This prints the brides list
        print() # For readability - I like to print and empty space line before/between and after the lists
        print('Brides List: ' , bride)
        print()
        
    elif supporting == 'groom':
        groom.append(user_guest)
        #This prints the grooms list
        print('Grooms List: ' , groom)
        print()

    


'''
when using a for loop on dictionaries, the loop iterates through the keys
so in this case the variable g (I chose g, it could be any letter or word) is each
key each time the loop executes. For example g is "Albert Einstein", then g is "Ben
Frank".
You can run the code right now to see this in action.
Afterwards, feel free to remove the print lines inside the for loop, they are just
to demonstrate
this point.
'''












