import time
import multiprocessing

result=[]
def getSquare(num,ress):
    for n in num:
        ress.append(n*n)
        print("Square :-",n*n)
    print("Result in process 1",ress)

'''def getCube(num,resc):
    for n in num:
        time.sleep(4)
        resc.append(n*n*n)
        print("Cube :-",n*n*n)
print(resc)'''

print("resultSet",result)
if __name__ == '__main__':
    number = [1,2,3,4,5,6,7,8]

    process1 = multiprocessing.Process(target= getSquare,args=(number,result))
    #process2 = multiprocessing.Process(target= getCube,args=(number,))

    process1.start()
    #process2.start()

    process1.join()
    #process2.join()

    print("Result in Main process",result)