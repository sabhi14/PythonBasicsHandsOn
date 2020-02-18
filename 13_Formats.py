print('{}'.format("format this string"))

fname="abhishek"
lname="sawant"

print('{}....{}'.format(fname,lname))

#Use format to align the output and give width
print(format(fname,"<50s"))
print(format(fname,">50s"))

#Fill Empty spaces

print(format(fname,"@<50s"))
print(format(fname,"$>50s"))


#Format integers
print("Score is {}".format(8))
print("Score is {:,}".format(898978))
print("Score is {:,}".format(456898978))
print("Score is {:15,} only".format(456898978))
print("Score is {:<15,} only".format(456898978))
print("Score is {:@>15,} only".format(456898978))
print("Score is {:@<15,} only".format(456898978))
#Center Alignment
print("Score is {:@^50,} only".format(456898978))


#Integer to Binary
number = 0
print("Binary of 12 is {0:o}".format(number))
while(number <= 20):
    print("Binary of {0} is {1:b} Octal is {2:o} HExa is {3:x}".format(number,number,number,number))
    number+=1

#Format to access list and dictionary items
language=['Python','django','java','node']
print("I love to work with",language[0])
print("I love to work with {0[0]}".format(language))
print("Secure Language is {0[2]}".format(language))

friends = {"mohan":"CHina","rohan":"Japan"}
print("Friend in Chennai: {0[mohan]} \nRohan is from{0[rohan]}".format(friends))

