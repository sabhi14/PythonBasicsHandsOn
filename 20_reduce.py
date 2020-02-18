'''
Reduce -> Aggregate functions!
1. It works with iterable
2. It will return single value.
'''

from functools import reduce
numbers = [1,2,3,4,5,6,7,8,9,10]
total = reduce(lambda n1,n2: n1+n2,numbers)
print(total)

numbers =[55,75,62,32,45,22,4,66,88]
largest = reduce(lambda n1,n2: n1 if n1>n2 else n2,numbers)
print(largest)

numbers =[5,15,10,8,2,3,6,18,7]

'''square= reduce(lambda i, j: i*i + j * j , numbers) 
print(square)
'''
def function1(a,b):
    return a+b

def function2(a):
    return a*a

def function3(a):
    if a<10:
        return True
    else:
        return False
    
square =  reduce(function1, map(function2, filter(function3,numbers)))
print(square)

#Using Lambda Finction
sqaure = reduce( lambda a,b:a+b,map(lambda a:a*a,filter(lambda n:n<10,numbers)))
print(sqaure)

#Using Lambda Function square of even numbers
square = reduce( lambda a,b:a+b,map(lambda a:a*a,filter(lambda n:n if n%2==0 else 0,numbers)))
print(square)



