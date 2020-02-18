alphabets=['a','b','c','d','e','f','g','h','i']
vowels =['a','i','e','o','u']

chVowels = filter(lambda alpha: alpha in vowels,alphabets)
print(list(chVowels))