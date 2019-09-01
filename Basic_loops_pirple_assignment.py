#Basic loops pirple assignment

for number in range(101):
    if number%3 == 0 and number%5 != 0:
        print("Fizz")
        continue
    if number%5 == 0 and number%3 != 0:
        print("Buzz")
        continue
    if number%3 == 0 and number%5 == 0:
        print("FizzBuzz")
        continue
    else:
        print(number)