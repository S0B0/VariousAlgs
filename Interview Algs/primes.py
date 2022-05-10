def title():
    print()
    print()
    
    print("=-=-=-=-=-=-=-=- [PRIME CHECKER] =-=-=-=-=-=-=-=-")
    print("#                                               #")
    print("#      check if a natural  number is prime      #")
    print("#                 ~ by S0B0 ~                   #")
    print("#                                               #")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    
    print()


def primes(num):
    for i in range(2,(num//2)):
        if num % i == 0:
            print(f"{num} is Not Prime")
            break
    else:
        print(f"{num} is Prime")
        
        
def menu():
    print("Please choose n \n")
    try:
        n = int(input(">: "))
    except:
        print(" PLEASE CHOOSE A NUMERIC VALUE ONLY! \n")
    else:
        primes(n)


menu()