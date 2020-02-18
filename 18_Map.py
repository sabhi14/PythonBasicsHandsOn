
# Map works only on iterables
# It will return the list created by lambda function
# Lambda function works on parameter of map


messages = ['Help','Run', 'Fight', 'Request']

for m in messages:
    print("Current message is:",m)

def printMessage(msg):
    print("-->"+msg)
    return(msg)

mapCheck=map(printMessage,messages)
print(list(mapCheck))

#Using Lambda Function


mapCheck=map(lambda m: "message from lambda map"+m,messages)
newL=list(mapCheck)
print(type(list(mapCheck)))
print(newL)
print(list(mapCheck))

#mapcheck is becoming empty list after type check as list constructor is being used

scores1=[25,35,45]
scores2=[75,95,63]
scores3=[5,10,20]

score3= map(lambda n1,n2,n3:(n1+n2)*n3,scores1,scores2,scores3)
print(list(score3))


scores1=[25,35,45,25,60]
scores2=[75,95,63]
scores3=[5,10,20,89]

score3= map(lambda n1,n2,n3:(n1+n2)*n3,scores1,scores2,scores3)
print(list(score3))


messages = ['Help','Run', 'Fight', 'Request']
#create a 2D list of characters in messages
#[['h','e','l','p'],['r','u','n']]

list2d= map(list,messages)
print(list(list2d))