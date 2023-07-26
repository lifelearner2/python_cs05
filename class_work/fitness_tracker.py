print('fitness tracking')

#dictionary to hold number of steps
steps = {}

#ask user to tell us the date they want to enter data for, the raw_input gives you a string
date1 = input('date: ')

#remember that raw_input gives you a string, we want an int
footsteps1 = int(input('steps: '))
#add to dictionary as a key: value of date: footsteps
steps[date1] = footsteps1
print(steps)

#repeat 2 more times so you'll get something like: {'8/18': 12332, '9/4': 1345, '7/7': 9876}
date2 = input('date: ')
footsteps2 = int(input('steps: '))
steps[date2] = footsteps2
print(steps)

date3 = input('date: ')
footsteps3 = int(input('steps: '))
steps[date3] = footsteps3
print(steps)

#gather data and sum then average. Use index to get values for each key steps[date1] - adding value to appropriate key
summed = steps[date1] + steps[date2] + steps[date3]

avg = summed/3
print('On average you walked ' + str(avg) + ' steps')