#Design an algorithm that finds the maximum positive integer input by a user.  
# The user repeatedly inputs numbers until a negative value is entered.
num_int = 0
max_int = 0

while num_int >= 0:
    num_int = int(input("Input a number: "))
    if max_int <= num_int:
        max_int = num_int
        
print("The maximum is", max_int)