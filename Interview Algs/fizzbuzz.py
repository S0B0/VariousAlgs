def title():
    
    print()
    print()
    
    print(" ===========================[      FIZZBUZZ     ]==========================")
    print("{                                                                          }")
    print("{  Write a program which iterates the integers from 1 to n.                }")
    print("{  For multiples of three print Fizz                                       }")
    print("{  and for the multiples of five print Buzz.                               }")
    print("{  For numbers which are multiples of both three and five print FizzBuzz.  }")
    print("{                                                                          }")
    print("===========================[      by S0B0     ]============================")
    
    print()
    print()

    
def fizzbuzz(n):
    for i in range(n):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FIZZBUZZ")
            
        elif i % 3 == 0:
            print("FIZZ")
            
        elif i % 5 == 0:
            print("BUZZ")
        else:    
            print(i)
        


def menu():
 title()
 print("### PLEASE MAKE A NUMERIC SELECTION ###\n")
 print("[1] Start")
 print("[0] Exit")
 
 try:
  option = int(input(">: "))
 except: print("please input only numeric values! ")
 else:
    while option != 0:
        if option == 1:
            print("\nSelect n for fizzbuzz(n) \n")
            try:
             n = int(input(">: "))
            except:
                print("please input only numeric values! ")
            else:
             fizzbuzz(n)
            print("\n would you like to try another n ? Y/N ")
            n = input(">: ")
            if n == "Y" or n == "y" or n == "yes" or n == "YES" or n == "Yes":
                menu()
                option = 0
            elif n == "N" or n == "n" or n == "no" or n == "NO" or n == "No":
                print("Exiting...Farwell...")
                option = 0
        elif option == 0:
            print("Exiting...Farewell")
                    
                
                
            
menu()
