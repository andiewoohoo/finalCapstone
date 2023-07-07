# To give the user options to either enter equations to calculate or read the file.

# Apply def funtion to do equation
def do_calc(num1, num2, operator):
     num1 = int(num1)
     num2 = int(num2)

     if operator == "+":
      return num1 + num2
     elif operator == "-":
      return num1 - num2   
     elif operator == "*":
      return num1 * num2    
     elif operator == "/":
      return num1 / num2
    
# To open a file   
file = open("output.txt", "a")

while True:
   option = input("Please choice: \n1. Enter equations. \n2. Read the file. \n3. Exit \nYour choice: ")
 # user input numbers and opertator
   if option == "1":
      while True:
       #Try and except funtion
       #Let user pick two numbers to do the euation
       try:  
        num1 = int(input("Please enter the first number: "))
        num2 = int(input("Please enter the second number: "))
        break
       except ValueError:
         print("Enter a numeric value and try again.")
       except Exception:
         print("Some error occured, please try again later.")

      
      # Let user choose which operation they want to put in the equation
      try:
       operator = input("Please enter the operation (+ , - , * , /) that you would like to perform: ")
       if operator in ('+', '-', '*', '/'):
        if operator == "+":
           print("Your answer is: " ,str((num1) + (num2)))
        elif operator == "-":
           print("Your answer is: " ,str((num1) - (num2)))
        elif operator == "*":
           print("Your answer is: " ,str((num1) * (num2)))
        else:
           print("Your answer is: " ,str((num1) / (num2)))
       else:
         print("Please enter an operator.")  
         continue
       print("Equation: ", num1 , operator , num2, "\nAnswer: ", str(do_calc(num1, num2, operator)))
       file.write("Your equation: " + str(num1) + " " + str(operator) + " " + str(num2) + " = " + str(do_calc(num1, num2, operator)) + "\n")
      except ZeroDivisionError:
         print("Please enter a number greater than 0 for number 2.")
      except Exception:
         print("Some error occured, please try again later.")
    
   elif option == "3":
     exit()   
      
      

   # To read the file option 
 
   else:
     while True:
      file_name = input("Please enter the name of the file : ")
      try:
        file = open(file_name, "r")
        print(file.read())
        file.close() # To close the file
        break
      except FileNotFoundError:
        print("File not found, please try again.")
      except Exception:
        print("Some error occured, please try again.")


       
     





 
