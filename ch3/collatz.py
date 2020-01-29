import sys

#Function recieves a number and returns 
#the following number
def collatz( number ):
    while number != 0:
        if number % 2 == 0:
            print(number//2)
            number = number//2
        else: 
            print( 3*number+1 )
            number = 3*number+1
        return number 

# Function will get user input and validate it 
# to be an integer
def validate():
    while True:
        try:
            # Return will exit the lop and method,
            # returning a value
            return int(input("Choose a number: "))
        except ValueError:
            print("Type an integer!")
            # Continue will re-run the while loop
            # if criterias are met. 
            continue

start = validate()
number = collatz(start)
while number != 1:
    number = collatz(number)
    if number == 1:
        break
    else: 
        continue