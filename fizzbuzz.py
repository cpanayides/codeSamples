$!/bin/python
# fizzbuzz.py

import sys

n = 100

def divBy(i, n):
    return 0 == i % n
    
for i in range(0, n+1):
    div_3 = divBy(i, 3)
    div_5 = divBy(i, 5)
    if div_3 and div_5:
        print str(i) + " fizzbuzz"
    elif div_3:
        print str(i) + " fizz"
    elif div_5:
        print str(i) + " buzz"
    else:
        print str(i)
    
