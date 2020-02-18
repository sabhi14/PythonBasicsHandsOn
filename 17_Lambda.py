'''
    nonname or anonymous functions
'''
def  addNum(n1,n2):
    return n1+n2

sum=addNum(4,8)
print(sum)

#Lambda Way
sum=lambda n1,n2,n3: n1+n2+n3
print(sum(4,8,12))

#Lambda Way
sum=lambda m: print(m)
sum("HEllo||")

squared= lambda n: n*n
print(squared(6))

#list of Lambda functions(functions in collections)
lambdalist = [lambda a: a**2, lambda a,b:a*b,lambda a,b: a+b]
print(lambdalist[0](8))
print(lambdalist[1](8,5))
print(lambdalist[2](8,4))


#Lambda with no Parameters
noParaCheck=lambda : True
print(noParaCheck())