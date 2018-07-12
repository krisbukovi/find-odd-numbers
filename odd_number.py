# filename: framework.py
# author: kris bukovi
# last modified: July 12, 2018

import math

def main():

    x = 2
    y = 5
    arr = []


    for i in range(x, y+1):
        
        if i%2 != 0:
            arr.append(i)

    print(arr)

main()