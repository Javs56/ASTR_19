#Write a Python program that defines a function f(x) that returns x**3 + 8. 
#In the main function of the program, call f(x) with x = 9 and print the result.  
#Use an if statement that executes if the result is larger than 27 and prints “YAY!”.

def problem(x):
    a = (x ** 3) + 8
    print(a)

    if a > 27: #notice the if statement is inside the function
        print('YAY!')

problem(5) #user input
