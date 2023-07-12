name = "Michael"
print(name)
print(type(name))

# using python to do math
x = 12
y = 14

area = x * y
print(area)


# can also put math right into print function
x = 12
y = 14

print(x*y)  #good for less lines of code - but area as noted above is better for clarity and to be able to use "area" again in other functions.


# what's my name with logic
name = "Michael"
# guess = "Steve"
guess = input("Please guess a name: ")

if guess == name: 
    print("Great job!")
else: 
    print("Wrong")
    
print("Got Here")  #this isn't part of the logic since it's not indented so this will always print



