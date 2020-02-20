import threading
import time

def getSquare(num):
    print("Sqaure of numbers ")
    for n in num:
        time.sleep(1)
        print("Square :-",n*n)

def getCube(num):
    print("Cube of numbers ")
    for n in num:
        time.sleep(1)
        print("Cube :-",n*n*n)
        

numbers = [1,2,3,4,5,6,7,8]
print("{:-^80}.Single threaded ")
getSquare(numbers)
getCube(numbers)


thread1=threading.Thread(target=getSquare,args=(numbers,))
thread2=threading.Thread(target=getCube,args=(numbers,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()