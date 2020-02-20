import time
import multiprocessing

result=[]
def getSquare(num,ress):
    print(num)
    print(ress)
    for index,n in enumerate(num):
        print(index," ",n)
        ress[index] = n*n
    print("Result in process 1",list(ress))


if __name__ == '__main__':
    number = [1,2,3,4,5,6,7,8]
    result= multiprocessing.Array('i',8)
    
    process1 = multiprocessing.Process(target= getSquare,args=(number,result))

    process1.start()
    
    process1.join()
    
    print("Result in Main process",list(result))