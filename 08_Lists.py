mixed=[2,4,8,"abhi",9090,44,71,'a',"asdf"]
print(mixed)
print(mixed[1:4])

newSlice = mixed[2:6]
print(newSlice)
print(type(newSlice))


backSlice = mixed[-4:-1]
print(backSlice)
backSlice1 = mixed[-4:]
print(backSlice1)
backSlice2 = mixed[-4::-1]
print(backSlice2)

print()
#Interating through List
for item in mixed:
    print(item)

providers = ["Ola","Uber","Zomato","FoodPanda"]
firstProviders = [provider[0] for provider in providers]
print(firstProviders)
lengthOfEachProviders = [len(provider) for provider in providers]
print(lengthOfEachProviders)
#IN Operator
print("Uber" in providers)

#add items in two lists
getx = [x for x in "abhishek"]
print(getx)


#Creating 2D List
print("adi "*4)
clone = [4]*3
print(clone)

clone2 = [[4]*3]*3
print(clone2)

friends=["OMA","OKA","CHIA"]
friends2=["B","CD","EFG"]

friends3= friends+friends2
print(friends3)


#OR
friends.extend(friends2)
print(friends)


print(mixed[0:7:2])
mixed.insert(0,55)
print(mixed)
mixed.pop(0)
print(mixed)

del mixed[0]
print(mixed) 



twodimension = [[4]*3 for a in range(0,3)]
print(twodimension)

#[[0, 0, 0], [1, 1, 1], [2, 2, 2]]
twodimension = [[a+1]*3 for a in range(-1,2)]
print(twodimension)

#[[0, 0, 0], [1, 1, 1], [4, 4, 4]]
twodimension = [[a**2]*3 for a in range(0,3)]
print(twodimension)

#[[0, 0, 0], [1, 1, 1], [8, 8, 8]]
twodimension = [[a**3]*3 for a in range(0,3)]
print(twodimension)