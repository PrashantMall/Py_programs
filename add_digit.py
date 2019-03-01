# Python Program - Add Digits of a Number

print("Enter 'x' for exit.")
num = int(input("Enter any number: "))
if num == 'x':
    exit()
else:
    sum = 0
    temp = num
    while num > 0:
    	rem = num % 10
    	sum += rem
    	num //= 10
    print(f"Sum of all digits of {temp} is {sum}")