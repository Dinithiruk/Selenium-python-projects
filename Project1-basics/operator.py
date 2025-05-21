print("------------Arithmetic operators------------")
value1 = 50
value2 = 100
value3 = 2
value4 = 3

print( value1 + value1)
print(value1 + value2)
print(value2 - value1)
print(value2 / value1)
print(value2 // value1)
print(value2 * value1)
print(value2%value1)
print(value3 ** value4) #power

print("------------Comparison operators------------")
a = 10
b = 4

print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)

print("------------Logical operators------------")
bool1 = True
bool2 = False

print(bool1 and bool2)
print(bool1 or bool2)
print(not bool2) # gives the opposite of the variable

print("------------Assignment operators------------")
a = 10
a = a+5
print(a)

a+=5
print(a)

a*=5
print(a)

a-=5
print(a)

a/=5
print(a)

print("------------Identity operators------------")
bool2 = True
bool3 = False

print(bool2 is not bool3)
print(bool2 is bool3)

print("------------Memebrship operators------------")
listTest = [13,4,56,5]
print(5 in listTest)
print(4 not in listTest)



