import time

def calcProd():
    #Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1,100000):
        product = product *1
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))


import time

for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)

    time.sleep(5)

#Control + C won't stop a process in IDLE.

for i in range(30):
    time.sleep(1)


import time

now = time.time()
now
1425064108.017826
round(now, 2)
1425064108.02
round(now, 4)
1425064108.0178
round(now)
1425064108
