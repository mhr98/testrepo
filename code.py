from cs50 import get_string

print("hello world") 
name= get_string("enter your name: ")
for x in range(10):
    print("hello, "+name+ str(x) +"th time") 
    