#Define a simple function

def firstFunction():
    print("This is the first function")

# firstFunction()
# print(firstFunction())
# print(firstFunction)
#Return function definition itself: <function firstFunction at 0x000001D833A8DF70>

#   Python methods does not return anything, 
#   then return None

#

def funcSum(num1,num2):
    return num1+num2

print(funcSum(7,5))

#function with default parameter (x is a default one)
def pow(num,x=1):
    result=1
    for i in range(x):
        result*=num
    return result

print(pow(2))
print(pow(2,3))

#reversing function parameter
print(pow(x=2,num=3))


#Argument list
def multipleAdd(*args):
    result=0
    for i in args:
        result+=i
    return result

print(multipleAdd(2,3,4,5))
