
num = int(input("What number do you want to find out if its a prime number or not : "))
def is_prime(num):
    for i in range(1,num+1):
        if i != 1 and i != num:
            if num % i == 0:
                return False
    
    return True
print(is_prime(num))
