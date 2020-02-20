from multiprocessing import Pool
import time

def myFunction(numList):
    counter=0
    for i in range(100000):
        counter = i*i
    return counter

if __name__ == "__main__":
    t1= time.time()
    pool = Pool()
    result=  pool.map(myFunction, range(100))
    pool.close()
    pool.join()

    print("Timetaken by pool: ", time.time()-t1)

    '''t2 = time.time()
    result=[]
    for i in range(1000000)'''