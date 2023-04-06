# python scripting
# easy to understand
# many libraries
# large community
# language interoperability - talk to other languages and software easily

# automate repetitive manual tasks using code

# some eg of thins we can write scripts for devops engineers:
# python to query a database
# write script to do a shell command
# script to create a backup
# script to fetch i.p addresses of an autoscalling
# check expiry date of an SSL certificate

# in-built modules:
# sys, os, subprocesses, math, random, datetime, json

# sys module

import sys
# print(sys.version)

# import os
# print(os.getcwd())
# os.chdir("C:/Users/user/pythonProject")
# print(os.getcwd())

# os.mkdir("test_dir")

# subprocess module

import subprocess
subprocess.run(["python", "hello_world.py"])

import math

pi = math.pi
pi_string = str(pi)
print("the value of pi is" + pi_string)

import random
randum = random.randrange(1, 10)
print(randum)

import datetime
today = datetime.datetime.now()
print(today)

# json module
import json

a = {
    "name": "John",
    "age": 30,
    "city": "London"
}

b = json.dumps(a)

print(a)
print(b)

