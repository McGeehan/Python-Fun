import time 
print("Let's try to count!")
print("Would you count along with me? (Type 'Yes' or 'No')")
password = input()
spam = 0
if password == 'Yes':
    print("Let's count to one million!")
    time.sleep(1)
    print("3,")
    time.sleep(1)
    print("2,")
    time.sleep(1)
    print("1,")
    time.sleep(1)
    while spam < 1000000:
        print(spam)
        spam = spam + 1
else:
    print("You're no fun! I'll count anyway!")
    print("Let's count to one million!")
    time.sleep(1)
    print("3,")
    time.sleep(1)
    print("2,")
    time.sleep(1)
    print("1,")
    time.sleep(1)
    while spam < 1000000:
        print(spam)
        spam = spam + 1
