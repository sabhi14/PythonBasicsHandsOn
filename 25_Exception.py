'''try:
    pass
except expression as identifier:
    pass
else:
    pass'''

try:
    fh =open("myfile.txt","wb")
    fh.write(b"operation successful")
except BaseException as be:
    print("Error while working with file",be)
else:
    fh.close()
    print("File Operations success")

