n = int(input("Enter a number:"))
i = 1
while (i <= n):
    j = 1
    while(j <= i):
        print("*", end= "")
        j = i
    print()
    i = i + 1
    
