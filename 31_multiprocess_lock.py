import multiprocessing
import time

def depositMoney(money,lock):
    for i in range(50):
        lock.acquire()
        money.value+=1
        lock.release()
        print("Deposit!")


def withdrawMoney(money,lock):
    for i in range(50):
        lock.acquire()
        money.value-=1
        lock.release()
        print("Withdrawn!")

if __name__ == "__main__":
    balanceMoney = multiprocessing.Value('i',0)
    lockProcess=multiprocessing.Lock()
    process1=multiprocessing.Process(target=depositMoney, args=(balanceMoney,lockProcess))
    process2=multiprocessing.Process(target=withdrawMoney, args=(balanceMoney,lockProcess))

    process1.start()
    process2.start()
    process1.join()
    process2.join()


    print("Final Balance: ",balanceMoney.value)