#
#Primes V1.1
#Copyright James Robinson 2018
#All rights reserved
#

'''
Notes:
█
System Arguements: maxNum, i
file.py maxNum, i
# =...60
'''

import math, sys, os

maxNum = 10000000

#Only if graphOutput == False
graphOutput = True
graphWidth = 10
graphPrime = "1 "
graphNorm = ". "

i = 1
filename = "primes.txt"

# Functions ==================================================

def isPrime(num):       
        if num < 2:
            return False

        for i in range(2, int(math.sqrt(num)) + 1):    
            if num % i == 0:
                return False
            
        return True

def printOutput(graphOutput, result, i):
    if graphOutput == True:
        if result == True:
            file_object.write(graphPrime)

        else:
            file_object.write(graphNorm)

        if i % graphWidth == 0:
            file_object.write("\n")

    else:
        if result == True:
            output = str(i) + "\n"        
            file_object.write(output)

# Start of Main ============================================

if len(sys.argv) == 2:
    maxNum = sys.argv[1]

elif len(sys.argv) >= 3:
    maxNum = sys.argv[1]
    i = sys.argv[2]


with open(filename, 'w') as file_object:

    

    while i <= int(maxNum):
        
        printOutput(graphOutput, isPrime(i), i)              
        i = i + 1


print(f"DONE: {filename} is {int(os.path.getsize(filename)) / 1000} bytes")