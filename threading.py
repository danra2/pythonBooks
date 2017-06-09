import time, datetime

startTime = datetime.datetime(2029, 10, 31, 0,0,0)
while datetime.datetime.now() < startTime:
    time.sleep(1)

print('Program now starting on Halloween 2029')


import threading, time
print('Start of program.')

def takeANap():
    time.sleep(5)
    print('Wake up!')

threadObj = threading.Thread(target=takeANap)
#This how we create a new threading object.
#We are calling this function within a new thread instance.
#It's passing the function as a argument.
threadObj.start()
#This is when we start executing the second thread.
#threadObj = threading.Thread(target=print('Cats', 'Dogs', 'Frogs', sep=' & '))
print('End of program.')
