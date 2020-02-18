start=int(input("Enter Start Number:- "))
end=int(input("Enter End Number:- "))


def sum(number1,number2):
    
    if number2!=number1 :
        return number2+sum(number1,number2-1)
        
    else :
        return 0

print(sum(start,end))