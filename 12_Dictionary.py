newDict= {}
print(type(newDict))

score={1:"Monday",2:"Tuesday",'3':"Wednesday","friends":["ana","bob","bin"]}
print(score)


#Create dictionary from list of tuple
friends = dict([("chennai",8),("mumbai",10),("Pune",30)])
print(friends)
#{'chennai': 8, 'mumbai': 10, 'Pune': 30}


print(friends["chennai"])

print(friends.get("mumbai"))

friends.update({'mumbai':5})
print(friends)


#iterate thrugh Dictionary
for key, value in friends.items():
    print(key," :- ",value)


#Create a dictionary key is string 
# and value is 
# length of string from the list of string

strings={"amar","tiger","monty","tony"}
friend ={ value:len(value) for value in strings}
print(friend)