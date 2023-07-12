#concatenating and converting a number to a string 
x = 12
print('The number is ' + str(x))

my_list = [1, 2, 3, 4]

#adding a list within a list. The output will be [1,2,3,4, [5,6]] - the length of the elements are 5 since the subset list is considered as one
my_list.append([5,6])
print(my_list)

