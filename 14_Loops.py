#For Loops

vowels="aeiou"
for b in vowels:
    print(b)

number = [1,2,3,4,5,6,7,8,9,10]
total=0
for n in number:
    total+=n
print("Sum is ",total)


#Using for loop with range
for n in range(1,15,3):
    print(n, end=" ")


for n in number:
    print(n**n)
    if(n==7):
        break
else:
    print("Exponent done calculation ")