

name = input( "Enter your name : ")
age = input( "Enter your age: ")
print ("Welcome ",name )
print ("Your age is :",age )
# When the 'input' func takes input it takes input as a str.
#if we want any specific input type then we'll have to typecast it .
print ("Before Typecasting :")
age = input( "Enter your age: ")
print (type(age))
print ("After Typecasting :")
age = int (input( "Enter your age: "))
print (type(age))