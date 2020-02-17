lengthOfList=int (input("Enter the length of list :- "))
list=[]
for i in range(lengthOfList) :
    list.insert(i,int (input("Enter element in list:-")))

print(list)
sliceStart=int(input("Slice Start :- "))
sliceEnd=int(input("Slice End :- "))

list=list[sliceStart:sliceEnd]
list.sort()
print(list)