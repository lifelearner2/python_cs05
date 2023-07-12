'''
Assignment: group the given guests by bride and groom. Your final output should be
two variables that each represent a list of guests,
one for "bride" and one for "groom"
'''
#THIS CODE DIDN'T WORK PERFECTLY - THAT'S WHY IT'S IN THE PRACTICE FILE

#a list of a dictionaries of all guests in key/value pairs that need to be sorted by bride and groom. This also gives better readability.
guests = [ 
    {'Albert Einstein': 'bride'},    
    {'Alfred Pennyworth': 'bride'}, 
    {'Anthony Cleopatra': 'groom'}, 
    {'Ben Frank': 'bride'}, 
    {'Ben Button': 'groom'},
    {'Charlie Bucket': 'groom'}, 
    {'David Attenborough': 'bride'}
    ]
# print(guests)

guest = ()

#this was hard coded - trying to find a way to do interpolation
bride = ['Albert Einstein', 'Alfred Pennyworth', 'Ben Frank', 'David Attenborough']
groom = ['Anthony Cleopatra', 'Ben Button', 'Charlie Bucket']

# bride = {guest: 'bride'}
# groom = {guest: 'groom'}

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
#asks user to enter guest and either bride or groom and stores that info in variable called add_guest
user_guest = input("Enter guest name and if they are with the bride or groom (use this format - 'Jane: bride'): ")

#This loops through each guest in the dictionary called guests
for guest in guests:
    # user_guest = guests
    # print(guest) #guest is a key in the dictionary
    print()
    #prints the newly added guest from user  
    print(user_guest ,[])
   

#This prints the word 'bride' - but why??? and why doesn't it print the word 'groom'?    
# print(guests[g])#because g is a key, guests[g] is the value paired with that key

#insert your code here
#This prints the brides list
print()
print('Brides List: ' , bride)
print()
#This prints the grooms list
print('Grooms List: ' , groom)

#Extra Challenge (optional): add code for users to input guests by name and either
bride or groom,
#and as they come in sort them accordingly into your two lists
#don't forget to let users stop entering guests whenever they are finished
#insert your code here

#asks user to enter guest and either bride or groom and stores that info in variable called add_guest
# user_guest = input("Enter guest name and if they are with the bride or groom (use this format - 'Jane: bride'): ")

# '' in user_guest

# if user_guest >= " ":
#     bride.append(user_guest)
# else: 
#     groom.append(user_guest)
    
# bride = {user_guest: bride}
# groom = {user_guest: groom}

#prints the bride and groom lists

# print() #prints a space between 
# print('Brides List: ' , user_guest, bride)
# print()  #prints space for readability
# print('Grooms List: ' , user_guest, groom)


# more code that I played with


'''
Assignment: group the given guests by bride and groom. Your final output should be
two variables that each represent a list of guests,
one for "bride" and one for "groom"
'''
#All guests listed in key/value pairs in dictionaries within a list. I added a role description to the key and value so that it makes more sense and is easier to access
guests = [
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

#this loops through the guest list and determines if the guest is supporting the bride or groom and then adds that key/value pair to the appropriate bride or groom list.
# for guest in guests:
#     if guest['supporting'] == 'bride':
#         bride.append(guest)
#     elif guest['supporting'] == 'groom':
#         groom.append(guest)

  
#Extra Challenge (optional): add code for users to input guests by name and either
bride or groom,

#variable created for goodbye message
goodbye_message = "Thank you, see you at the wedding!"

#variable to determine if the while loop will continue to run
add_more = True

#asks user to enter guest and either bride or groom and stores that info in variable called user_guest
user_guest = input("Enter guest name and who they are supporting (use this format - 'Jane: bride') or type 'q' to quit: ")    
#while loop for adding more guests until the user quits
while add_more:
    if user_guest == 'q':
        add_more = False
        print(goodbye_message)
    else: 
        guest_info = user_guest.split(':')
        #Split the user input at the colon - I had to get help for this part cuz I was stuck
        guest_name = guest_info[0].strip()
        supporting = guest_info[1].strip()
        #Extract the guest name and who they're supporting - I had been trying to access the value using an index and things weren't working perfectly so I got help for this part.
        
        #and as they come in sort them accordingly into your two lists
        #appending to appropriate list
        if supporting == 'bride':
            bride.append({'Name': guest_name, 'supporting': supporting}) # I was initially appending the whole guest_info list rather than just the dictionary 
            #This prints the brides list
            print() # For readability - I like to print and empty space line before/between and after the lists
            print('Brides List: ' , bride)
            print()
        elif supporting == 'groom':
            groom.append({'Name': guest_name, 'supporting': supporting})
            #This prints the grooms list
            print('Grooms List: ' , groom)
            print()




# #don't forget to let users stop entering guests whenever they are finished

# more_guest = input("Enter another guest name and who they're supporting or type 'q' to quit: ")
        
# add_guest = more_guest.split(':')


# guest_info = user_guest.split(':')
# #Split the user input at the colon - I had to get help for this part cuz I was stuck
# guest_name = guest_info[0].strip()
# supporting = guest_info[1].strip()



     

        # #variable created for goodbye message
        # goodbye_message = "Thank you, see you at the wedding!"

        # if supporting == 'bride':
        #     bride.append(guest_info)
        # if supporting == 'groom':
        #     groom.append(guest_info)
            

        # if supporting == 'bride':
        #     bride.append(add_guest)
        
        # if supporting == 'groom':
        #     groom.append(add_guest)

        # if supporting == 'bride':
        #     bride.append({'Name': guest_name, 'supporting': supporting}) 
        #     #This prints the brides list
        #     print() # For readability - I like to print and empty space line before/between and after the lists
        #     print('Brides List: ' , bride)
        #     print()
        # elif supporting == 'groom':
        #     groom.append({'Name': guest_name, 'supporting': supporting})    
        #     #This prints the grooms list
        #     print('Grooms List: ' , groom)
        #     print()
            
        # if more_guest == 'q':
        #         print()
        #         print(goodbye_message)
        #         print()

        #issue: it will add the first user entry to the correct place but the not the second 

        

        


            
            
            # print(guest) #g is a key in the dictionary
            
            # print(guests[guest])#because g is a key, guests[g] is the value paired with that key   





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












