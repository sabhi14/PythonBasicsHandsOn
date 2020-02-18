'''

if expression:
    pass
if condition:
    pass
else :
    pass

'''

number=int(input("Input Number: "))
if number>30 :
    print("Number is more than 30")
else :
    print("Something else")

numbers = [1,2,3,4,5,6,7,8,9,10]
if number in numbers:
    print("Present")
else:
    print("Absent")

friends1 = ["ola","uber","didi","mave","ride"]
friends2 = ["ride","jia","didi","zoom"]

#Common Friends
for f1 in friends1:
    if f1 in friends2:
        print(f1,end=" ")
