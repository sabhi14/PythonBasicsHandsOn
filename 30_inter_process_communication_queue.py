import time
import multiprocessing

result=[]
def getSquare(num,queue):
    for n in num:
        queue.put(n*n)
    


if __name__ == '__main__':
    number = [1,2,3,4,5,6,7,8]
    sharedQueue=multiprocessing.Queue()
    print("Ststus of Queue is:-" , sharedQueue.empty())
    process1 = multiprocessing.Process(target=getSquare, args=(number,sharedQueue))
    process1.start()
    process1.join()

    print(sharedQueue.empty())
    while sharedQueue.empty() is False:
        print(sharedQueue.get())