#!/usr/bin/env python3
''' Description: This program will take the date of birth in three different formats and convert it into
    standard format.

-----------------------------------------------------------------------
OPS435 Assignment 1 - Winter 2021
Program: a1_gbrana.py
Author: "gbrana"
The python code in this file (a1_gbrana.py) is original work written by
"Gyan Bahadur Rana". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''
import os
import sys

def leap_year(obj):
    '''
    This Function checks if the given year(obj) in date of birth is leap year or not. This function returns
    True if the given year is leap year, otherwise Fasle.
    '''
    if (obj % 4) == 0:
        status = True
    elif (obj % 100) == 0:
        status = True
    elif (obj % 400) == 0:
        status = True
    else:
        status = False
    return status

def sanitize(obj1,obj2):
    '''
    This Function has 2 objects. Obj1 conatins the date of birth given by the user and obj2 conatins allowed
    letters i.e. 0-9 digits. This function removes characters from obj1 that are not in obj2 and return new obj1.
    '''
    results = ''
    for a in obj1:
        if a in obj2:
            results += a
    return results

def size_check(obj, intobj):
    '''
    This Function checks the lengths of the obj returned by sanitize Function. Intobj conatins the allowed size
    in integer and if the size of obj matches the intobj then it returns True, othersies False.
    '''
    status = ''
    if len(obj) == intobj:
        status = True
    else:
        status = False
    return status

def range_check(obj1, obj2):
    '''
    This Function checks the range of obj1. obj2 contains the two range values in integer; first one is lower bound of
    the range and second one is upper bound of the range. If the range of obj1 matches
    range of obj2 then it returns True, otherwies False.
    '''
    if obj1 >= obj2[0]  and obj1 <= obj2[1]:
        status = True
    else:
        status = False
    return status
    
def usage():    
    '''
    This Function checks the if the argument provided by the user is no valid or there is no argument then it returns a
    usage message.
    '''
    status = "Usage: a1_gbrana.py YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD"
    return status

if __name__ == "__main__":
   # step 1
   if len(sys.argv) != 2:
      print(usage())
      sys.exit()
   # step 2
   month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']
   days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
   user_raw_data = sys.argv[1]
   # step 3
   allow_chars = '0123456789'
   dob = sanitize(user_raw_data, allow_chars)
   # setp 4
   result = size_check(dob,8)
   if result == False:
       print("Error 09: wrong date entered")
       sys.exit()
   # step 5
   year = int(dob[0:4])
   month = int(dob[4:6])
   day = int(dob[6:])
   # step 6
   result = range_check(year,(1900,9999))
   if result == False:
       print("Error 10: year out of range, must be 1900 or later")
       sys.exit()
   result = range_check(month,(1,12))
   if result == False:
       print("Error 02: wrong month entered")
       sys.exit()
   result = leap_year(year)
   if result == True:
       days_in_month[2] = 29
   result = range_check(day, (1, days_in_month[month]))
   if result == False:
       print("Error 03: wrong day entered")
       sys.exit()
   # step 7
   new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)
   # step 8
   print(new_dob)  
