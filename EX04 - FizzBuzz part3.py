number = int(input("Enter an integer: "))
x = number%3
y = number%5

if x == 0 and y == 0:
    print("FizzBuzz")
else:
    print(number)