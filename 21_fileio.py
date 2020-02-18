'''
File IO
1. Open the file
2. It will return file handle
3. Use the file handle to do file operations(read,write, change,delete, change attributes)
4. Close the file handle
'''

fh = open("asgn.py","r")
print(fh.name)
print(fh.mode)
print(fh.closed)
fh.close()
print(fh.closed)
print("<---------------------->")
with open("asgn.py","r") as fh:
    print(fh.name)
    print(fh.mode)
    print(fh.closed)
    fh.close()
    print(fh.closed)

#Open the file in write mode and write data to the same
with open("python.txt","w" ) as fh:
    fh.write("Hello from Python")
    fh.write("\nIn a new line")

fh=None
# print(fh.name)
# fh.write("try to write")

#Open file in append mode and append data to same
with open("python.txt","a") as fh:
    fh.write("\nHello Again from Python")
    fh.write("\nNext is Fun")

#open file in read only mode and write to console
with open("python.txt","r") as fh:
    content=fh.readlines()
    print(content)
    for i in content:
        print(i)

#Read data from file in chunk size
with open("python.txt","r") as fh:
    content1=fh.read(10)
    content2=fh.read(10)
    content3=fh.read(10)
    print(content1)
    print(content2)
    print(content3)
    print(fh.tell())

    # seek(how much I want to seek, from where)
    # possible values of from where
    # 0-> pointer shift will start from beginning of file
    # 1-> pointer shift will start from current offset
    # 3_> EOF will be the current offset!
    fh.seek(11,0)
    print(fh.tell())
    print(fh.read(7))
    print(fh.tell())
    

#Copy data from one file to another
with open("python.txt","r") as fh:
    content = fh.readlines()
    tempfh=open("python1.txt","w")
    for eachline in content:
        tempfh.write(eachline)
    tempfh.close()

#Copy data from one image to another
with open("ss.png","rb") as fh:
    content = fh.readlines()
    tempfh=open("screens.png","wb")
    for eachline in content:
        tempfh.write(eachline)
    tempfh.close()