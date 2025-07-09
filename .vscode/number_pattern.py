num = int(input("Enter a number: "))
if num < 0:
    print("Please enter a positive number.")
else:
    for i in range(num, 0, -1):
        print(" " * ((num+1)-i), end='')
        
        for j in range(i, 0, -1):
            print(j, end='')
        
        for k in range( 2, i + 1):
            print(k, end='')
        
        print()
    for i in range(1, num + 1):
        print(" " * ((num+1) - i), end='')
        
        for j in range(i, 0, -1):
            print(j, end='')
        
        for k in range(2, i + 1):
            print(k, end='')
        
        print()







