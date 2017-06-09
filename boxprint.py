def boxPrint(symbol, width, height):
 if len(symbol) != 1:
u raise Exception('Symbol must be a single character string.')
 if width <= 2:
v raise Exception('Width must be greater than 2.')
 if height <= 2:
w raise Exception('Height must be greater than 2.')
Debugging 217
 print(symbol * width)
 for i in range(height - 2):
 print(symbol + (' ' * (width - 2)) + symbol)
 print(symbol * width)
for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
 try:
 boxPrint(sym, w, h)
x except Exception as err:
y print('An exception happened: ' + str(err))

# The sequence of calls is called the call stack.
# The trackback is displayed by Python whenever a raised exceptions goes unhandled.
# But you can also obtain it as a string by calling traceback.format_exc().
#This function is useful if you want the information from a exception's trackback but also want an except statement to gradecully handle the exception.
# You will need to import Python's traceback module before claling this function.

>>> import traceback
>>> try:
 raise Exception('This is the error message.')
except:
 errorFile = open('errorInfo.txt', 'w')
 errorFile.write(traceback.format_exc())
 errorFile.close()
 print('The traceback info was written to errorInfo.txt.')

 #This statement would be used to log information from errors into a textfile for future debugging.
