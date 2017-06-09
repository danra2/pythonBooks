#Popen() stands for process open and it's apart of the subprocess module.
#Unlike threads, a process cannot directly read and write another processes' vairables.
# If you think of a multithreaded program as having multiple fingers following source code,
# then having multiple processes of the same program open is like having
# a friend with a separate copy of the program’s source code. You are both
# independently executing the same program.

calcProc = subprocess.Popen('c:\\Windows\\System32\\calc.exe')
calcProc.poll() == None
True
calcProc.wait()
0
calcProc.poll()
0
#Poll tells if you if the other instance of the program has yet finished running.
#Wait tells us until this program is done running don't run etc kind of like a promise.
subprocess.Popen(['C:\\Windows\\notepad.exe', 'C:\\hello.txt'])
#The first argument is the location and name of the program itself
#The second argument is the script you want it to run or read from following opening.


>>> subprocess.Popen(['C:\\python34\\python.exe', 'hello.py'])
<subprocess.Popen object at 0x000000000331CF28>

fileObj = open('hello.txt', 'w')
fileObj.write('Hello world!')
12
356 Chapter 15
fileObj.close()
import subprocess
subprocess.Popen(['start', 'hello.txt'], shell=True)

subprocess.Popen(['open', '/Applications/Calculator.app/'])
subprocess.Popen object at 0x10202ff98>
