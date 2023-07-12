# Part 1 -  Write a program that declares 3 variables (length, width, and height), then calculates and prints the volume.
length = 10
width = 3
height = 5

volume = length * width * height
print(volume)

 

# Part 2 - Write your own “Guess my name” without inputs, but with the name to guess as Sean. Include if/else statement checks for multiple spellings of the name (e.g. Shawn and Shaun are also correct answers). Hint: You can use an if statement inside an else statement.

# if guess=='Sean':
#     print('correct')
# else:
#     if guess=='Shaun':
#         print('correct')


# the problem with this code below is that once guess_1 is correct the others won't be run. But if you change the guess's value then you can see the others run.
# I think the problem is that the subsequent if/else statements are nested in the first one, I did it this way initially because your instructions said I could put...
# ...if statements inside of the else statements.
name_1 = "Sean"
name_2 = "Shawn"
name_3 = "Shaun"

guess_1 = "Sean"
guess_2 = "Shawn"
guess_3 = "Shaun"

if guess_1 == name_1:
    print("You guessed my name!")
else: 
    if guess_2 == name_2: 
        print("That's correct! Though the spelling I prefer is Sean")
    else:
        if guess_3 == name_3:
            print("That's correct, though I prefer the spelling to be Sean")

        else: 
            print("Sorry, that's not my name")
    

# trying again - this code below does allow for all guesses to be checked/run and printed - but I had to do it in separate if/else statements.
# I initially wrote this with the exact name and guess variable names and it worked, but then I thought that could be confusing and possibly cause trouble, 
# ...so I changed the variable names for good measure.
name_one = "Sean"
name_two = "Shawn"
name_three = "Shaun"

guess_one = "Sean"
guess_two = "Shawn"
guess_three = "Shaun"

if guess_one == name_one:
    print("You guessed it!")
else: 
    print("Try again.")

if guess_two == name_two:
    print("You got it right!")
else: 
    print("Maybe next time")
    
if guess_three == name_three: 
    print("Great Job!")
else: 
    print("Aww...man!")
 
# Question: is there a way to do it the way I attempted the first time and have it check, run and print all or did I need to do it the way I did it the second time?   

# Part 3 - Extra Challenge: add input to your “Guess my name” code in the section above, then experiment with “elif” which is the same as the combined else and if.
new_name = "Sean"
new_guess = input("Guess my name...: ")

if new_guess == new_name:
    print("Wow! Are you psychic?!")
elif new_guess == "Shawn":
    print("I don't spell it that way, but yes that's my name!")
elif new_guess == "Shaun":
    print("Yes - that's my name, just not my spelling")
else: 
    print("Sorry, that's not it")
    

