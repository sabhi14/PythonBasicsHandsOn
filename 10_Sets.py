number_set={5,15,5,20,5,30}
print(number_set)

'''mixed_type = {4,5,6,7,[2,7,9,3]}
print(mixed_type)#TypeError: unhashable type: 'list'
'''

mixed_type = {4,5,6,7,(2,7,9,3)}
print(mixed_type)

number_list=[4,5,5,8,8,9,9,10,12]
number_set=set(number_list)
print(number_set)

number_set.add(85)
print(number_set)

number_set.add(9)
print(number_set)

number_set.remove(85)
print(number_set)

number_set.discard(12)
print(number_set)

number_set.pop()
print(number_set)

#Unions And Intersections
score1={58,62,35,45}
score2={58,96,36,45,75}
print(score1.union(score2))
print(score1.intersection(score2))


#Substraction / Difference
score1={58,62,35,45}
score2={58,96,36,45,75}
print(score1-score2)
print(score2-score1)



print(number_set)
number_set.add(44)
print(number_set)
freeze=(frozenset(number_set))
