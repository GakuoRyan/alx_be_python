positive_integer = int(input("Enter the size of the pattern:"))
n = positive_integer
for i in range(n):
    for j in range(n):
        print("*", end= "")
    print()
