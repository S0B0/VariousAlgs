
def titlecard():
    print()
    print()
    
    print("~~~~~~~~~~~~~~~~ [FIBO VARIANTS] ~~~~~~~~~~~~~~~~")
    print("#                                               #")
    print("#          various fibonacci functions          #")
    print("#                 == by S0B0 ==                 #")
    print("#                                               #")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    print()
   


# CLASSIC WAY OF CALCULATING fib(n)

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib (n-2)
    
# MEMOIZED WAY OF CALCULATING fib(n)

memo = {}
def fib2(n):
   if n <= 2:
       return 1
   if n in memo:
       return memo[n]
   else:
       num = fib2(n-1) + fib2(n-2)
       memo[n] = num
       return num


# 'MAIN'
def fibos():
    
    print("\n[1] Classic fib(n)")
    print("[2] Memoized fib(n)")
    print("[0] Exit\n")
    
    print(" ## PLEASE MAKE A NUMERIC SELECTION ## ")
    try :
        option = int(input(">: "))
    except:
        print("====== WARNING! INPUT MUST BE A NUMBER! ====== \n")
        fibos()
        option = 0
    else:
        while option != 0:
            if option == 1:
                print("Please input n for classic fib(n): ")
                try:
                 n = int(input(">: "))
                except:
                    print("====== WARNING! INPUT MUST BE A NUMBER! ====== \n")
                    fibos()
                    option = 0
                else:
                    print(f" \n-----> Classic fib(n) = {fib(n)} <-----\n")
                    print("would you like to try with another function? y/n ")
                    decision = input("\n>: ")
                    if decision == "Y" or decision == "y" or decision == "yes" or decision == "Yes" or decision == "YES":
                        fibos()
                        option = 0
                    elif decision == "N" or decision == "n" or decision == "no" or decision == "No" or decision == "NO":     
                        print("Exiting...Farewell...")
                        option = 0
                
            elif option == 2:
                print("Please input n for memoized fib(n): ")
                try:
                 n = int(input(">: "))
                except:
                    print("====== WARNING! INPUT MUST BE A NUMBER! ====== \n")
                    fibos()
                    option = 0
                else:
                    try: 
                        print(f" \n-----> Memoized fib(n) = {fib2(n)} <-----\n")
                    except: 
                        print("INPUT TOO LARGE --> INCURSION ERROR! ")
                    else:
                        print("would you like to try with another function? y/n ")
                        decision = input("\n>: ")
                        if decision == "Y" or decision == "y" or decision == "yes" or decision == "Yes" or decision == "YES":
                            fibos()
                            option = 0
                        elif decision == "N" or decision == "n" or decision == "no" or decision == "No" or decision == "NO":     
                            print("Exiting...Farewell...")
                            option = 0
            elif option == 3:
                print("option 3 selected ")
            elif option == 0:
                print("Exiting...Farewell...")
                break
            else:
                print("INVALID INPUT! TRY AGAIN")
                fibos()
                


titlecard()
fibos()


#Memoization is a term introduced by Donald Michie in 1968,
# which comes from the latin word memorandum (to be remembered).
# Memoization is a method used in computer science to speed up 
# calculations by storing (remembering) past calculations. 
# If repeated function calls are made with the same parameters,
# we can store the previous values instead of repeating unnecessary
# calculations. In this post, we will use memoization to find terms
# in the Fibonacci sequence.