'''
def funcname(parameter_list):
    pass
'''
counter = 10
def customMessage(message):
    global counter
    if counter > 0 :
        print(message)
        counter -=1
        customMessage(message)

customMessage("Hello")