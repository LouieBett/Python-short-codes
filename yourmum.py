import sys, time, random

while True:
    number = int(input("input a number?"))
    
    if number <= 0:
        break
    number = number *2
    print(number)