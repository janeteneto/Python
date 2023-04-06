# python libraries and modules

# extensive libraries in python - external collections of useful functions and methods

from random import *
import math

print(random())

num_float = 23.66

print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi)

# modules - smaller than library - set of code or functions with the .py extension.
# library are basically a collection of modules

import os
import datetime, sys

working_dir = os.getcwd()
print(working_dir)
print(datetime.datetime.today())

print(sys.path)

def operating_system_info():
    print(os.cpu_count())

operating_system_info()

# pip - pythons package manager

import requests

request_bbc = requests.get("https://www.bbc.co.uk")

print(request_bbc.status_code)
print(request_bbc.content)



