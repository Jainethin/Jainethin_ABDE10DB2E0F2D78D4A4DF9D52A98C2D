def factorial(a):
    if a==1 or a==0:
        return 1
    else:
        return a*factorial(a-1)

num=int(input("Emter a number: "))
print("Factorial of",num,"is ",factorial(num))
