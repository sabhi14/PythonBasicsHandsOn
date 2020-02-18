array=["madam","malayalam","chick","peep","Amore, Roma","daga"]

palinList=filter(lambda a: a=="".join(reversed(a)),array)
print(list(palinList))

palinList=filter(lambda a: a==a[::-1],array)
print(list(palinList))