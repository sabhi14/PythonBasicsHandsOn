import threading
import time
def callMeForEachThread(threadName,delay):
    counter=0
    while counter <= 10:
        print(threadName,"  ",str(counter))
        time.sleep(delay)
        counter+=1

thread1=threading.Thread(target=callMeForEachThread,args=("Thread1",1))
thread2=threading.Thread(target=callMeForEachThread,args=("Thread2",2))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("Multithreading")