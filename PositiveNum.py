a = []
n = int(input("Enter the number of list items u want...\n"))
print("Enter the list items...")
for i in range(0, n):
    a.append(int(input()))

print("The positive numbers in the range are:")
for j in a:
    if j > 0:
        print(j);