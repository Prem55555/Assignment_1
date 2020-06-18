print("Please select operation 1=add 2=sub 3=mul 4=div 5=mod 6=exp 7=floor div")  
  
  
 
c=int(input())

number_1 = int(input("Enter first number: ")) 
number_2 = int(input("Enter second number: ")) 
  
if c==1: 
    print(number_1, "+", number_2, "=", 
                    number_1+number_2) 
  
elif c==2: 
    print(number_1, "-", number_2, "=", 
                    number_1-number_2) 
  
elif c==3: 
    print(number_1, "*", number_2, "=", 
                    number_1*number_2) 
  
elif c==4: 
    print(number_1, "/", number_2, "=", 
                    number_1/number_2) 
elif c==5: 
    print(number_1, "%", number_2, "=", 
                    number_1%number_2)
elif c==6: 
    print(number_1, "**", number_2, "=", 
                    number_1**number_2)
elif c==7: 
    print(number_1, "//", number_2, "=", 
                    number_1//number_2) 
else: 
    print("Invalid input")