print('data logger code. please only enter whole numbers.')

data = []

data0 = int(input('enter data point: '))
data.append(data0)
print(data)


data1 = int(input('enter data point: '))
data.append(data1)
print(data)

data2 = int(input('enter data point: '))
data.append(data2)
print(data)

summed = data[0] + data[1] + data[2]
print(summed)

averaged = summed/3
print('average of the data: ' + str(averaged))