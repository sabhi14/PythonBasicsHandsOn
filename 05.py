n1 = 5
print(str(n1) + " Type is " + str(type(n1)))

n2 = 5.56
print(str(n2) + " Type is " + str(type(n2)))

#Lists

mixed=[]
print(type(mixed))
mixed=[2,5.5,'a','B',"Uber"]
print(mixed)
print("Length of list is :-"+ str(len(mixed)))
mixed[0]=4
print(mixed)


#Tuple

noChange = (2,5.5,'a','B',"Uber")
print(noChange)
print(type(noChange))
print(noChange[0])

#Strings

location = "Chennai"
print(type(location))
print(len(location))
print(location[2])


multiline='''
"hello" + 
" how are "+
    "you?"
'''
print(multiline)


#Sets
noOrder = {25,35,45,80,75}
print(type(noOrder))


#Dictionary
keyValue={}
print(type(keyValue))
keyValue={1:"Abhi", "Tech":"Java",4:90}
print(keyValue["Tech"])


#Type Conversion
n2=5
print(type(n2))
n3=float(n2)
print(type(n3))
n4=str(n3)
print(type(n4))


#Input
age=input("Enter Your Age :-")
print("Age:-"+age)
print("###############")
age=int(input("Enter Your Age :-"))
print("Age:-",age+55)

