x=0
print(x)

#Re define to variable
x="abc"
print(x)

#strongly typed language
#print("This is a string "+123)

#Global variable & Local variable

def func():
    x="def"
    print(x)

#Get different value of x
func()
print(x)

del x #deleted of the definition of the variable
print(x)