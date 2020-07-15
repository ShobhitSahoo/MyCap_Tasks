def fibonacci(n):
    if n < 0:
        print("Incorrect Input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return (fibonacci(n-1) + fibonacci(n-2))

#print(fibonacci(int(input("Enter the number of fibonacci numbers u want"))))

n = int(input("Enter the number of fibonacci numbers u want...\n"))
print("The sequence is:")
for i in range(n):
    print(fibonacci(i))