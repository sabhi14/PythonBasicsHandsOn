search=input("Enter the word to b search:- ")
replace=input("Enter the word to be replaced:- ")

with open("python.txt","r") as fh:
    content= []
    for line in fh.readlines():
        content.append(line.replace(search,replace))
with open("python.txt","w") as f:
    for line in content:
        f.write(line)

with open("python.txt","r") as fh:
    content=fh.readlines()
    print(str(content))
    '''for i in content:
        cont=str(content)
        cont.replace(search,replace)
        fh.truncate(0)
    fh.write(cont)
    print(fh.readlines())'''
    
