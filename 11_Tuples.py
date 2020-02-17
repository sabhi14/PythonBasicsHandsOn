sample=()
print(type(sample))
sample= 25,35,45
print(sample)
sample = (25,65,45,[90,"check",5.5])
print(sample)
sample=((3,4,5),(4,5,6),(5,6,7))
print(sample)
print(sample[1][1])


#creating tuples from list and sets

scores = [25,35,45]
sample=tuple(scores)
print(sample)

scores = {25,35,45}
sample=tuple(scores)
print(sample)


onlyOne = "omg"
checkOne=(onlyOne,)
print(checkOne)
print(type(checkOne))

sample = (25,65,45,[90,"check",5.5],90,78,'d')
print(sample[1:])
#(25, 65, 45, [90, 'check', 5.5], 90)
print(sample[:5])
#(25, 45, 90)
print(sample[:5:2])


#Tuple is immutable -> You cannot modify elements in the tuple
#                   ->but you can assign new tuple to same variable


sample=(25,65,45)
print(sample[0])
#TypeError: 'tuple' object does not support item assignment
#sample[0]=35
sample=(35,64,45)
print(sample)

vowel1=('a','e','i')
vowel2=('o','u')
print( vowel1+vowel2)


#TypeError: 'tuple' object doesn't support item deletion
#del sample[0]
#print(sample)

#Delete the given tuple
#del sample

for item in sample:
    print(item)


