'''
Filter
 It works on iterable
 Works with two parameters
 1.> Function name/Lambda
 2.> Iterable
 Function name/Lambda will evaluate for each item in iterable

 Map-> It will return the list created by lambda/named function
 Filter-> It will return the list for which lambda /named function evaluates to true.

'''

numbers =[55,75,62,32,45,22,4,66,88]
selected = filter( lambda a:a>45,numbers)
print(list(selected))

even = filter( lambda a:a%2==0,numbers)
print(list(even))

odd = filter( lambda a:a%2!=0,numbers)
print(list(odd))