print("a: ",23,sep="0.")
#sep - ayraç kelimeler arasındaki boşluğun nasıl olacağını belirler
#end - yazılan ifadelerin sonuna ne gelecek


A,B=50,75
# Adding two numbers A+B
result = A + B

print("Result of {0} and {1} is {2}" .format(A, B, result))
#here we set the format of the numbers as well
#format() is one of the string formatting methods in Python3, which allows multiple substitutions and value formatting. This method lets us concatenate elements within a string through positional formatting.

# it will print new line after the messages
print("Hello")
print("World")

# it will print new line
print()

# it will print new line after printing "Hello"
print("Hello",end="\n")

# it willprint new line after printing "World"
print("World")

# it will print new line 
print()

# it will not print new line after printing "Hello"
# it will print space " "
print("Hello",end=" ")
# it will print new line after printing "World"
print("World")



