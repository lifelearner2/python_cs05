print('fitness tracking')


steps = {}


date1 = input('date: ')

footsteps1 = int(input('steps: '))

steps[date1] = footsteps1
print(steps)


date2 = input('date: ')
footsteps2 = int(input('steps: '))
steps[date2] = footsteps2
print(steps)

date3 = input('date: ')
footsteps3 = int(input('steps: '))
steps[date3] = footsteps3
print(steps)


summed = steps[date1] + steps[date2] + steps[date3]

avg = summed/3
print('On average you walked ' + str(avg) + ' steps')