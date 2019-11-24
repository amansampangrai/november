#python library

'''import datetime
print("Today date is ",datetime.date.today())

import time
print(time.asctime())

import webbrowser
a=input("Search video")
print("Opening browser")
webbrowser.open_new_tab('youtube.com/search?q=%s'%a)


import os
print(os.get_exec_path())
print(os.getcwd())


import math
num=int(input("Enter a number"))
print(math.factorial(num))
print(math.sqrt(num))'''


'''from termcolor import colored
print(colored('hello world','red','on_grey'))

text=colored('wou color look nice','red',attrs=['reverse','blink'])
print(text)
'''

import os
import math
import datetime
import termcolor
print(termcolor.colored("Hello world",'red'))
print(math.factorial(5))
print(os.getcwd())
print(datetime.date.today())



