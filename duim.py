#!/usr/bin/env python3

import subprocess, sys
import os
import argparse



'''
OPS435 Assignment 2 - Summer 2021
Program: duim.py 
Author: "gbrana"
The python code in this file (duim.py) is original work written by
"gbrana". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: This script will use du tool to provide the sub directory list of the provided directory and the graph will show the directory space.

Date: July 26, 2021
'''

'''
This function will take the input integer in percent if the number is between 0 to 100 and convert it into the graph to show the occupied space of the directory as "=" and available space as " " in the graph. If the provided input integer is not between 0 to 100 then this function will prompt a Usage message.
'''
def percent_to_graph(percent, total_chars):
    "returns a string: eg. '##  ' for 50 if total_chars == 4"
    if percent >= 0 and percent <= 100:
            percentgraph = int((percent/100) * total_chars)
            percentspaces = int(total_chars - percentgraph)
            return (("'" + "=" * percentgraph) + (" " * percentspaces) + "'")
    else:
            print("Usage: Percentage value must be between 0 and 100.")

'''
This function will take the location of the directory and give a list of its subdirectories.
'''
def call_du_sub(location):
    "use subprocess to call `du -d 1 + location`, rtrn raw list"
    process = subprocess.Popen(['du -d 1 ' + location], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = process.communicate()
    return list(output[0].decode('utf-8').strip())

if __name__ == '__main__':
    location = sys.argv[1]
