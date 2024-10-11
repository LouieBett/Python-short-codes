import time

pick = int(input("Pick a number you want to count down from: "))

count = pick
while count >= 0:
    print(count)
    time.sleep(1 )
    count -= 1
print("COUNTDOWN IS OVER!!!")