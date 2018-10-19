#Returns the sum of the two lowest positive integers
#entered into the function

def sum_two_smallest_numbers(numbers):
    size = 2
    number1 = numbers[0]
    number2 = numbers[1]
    while size< len(numbers):
        if number1 > number2:
            if number1 > numbers[size]:
                number1 = numbers[size]    
        elif number2 >= number1:
            if number2 > numbers[size]:
                number2 = numbers[size]
        size = size + 1
    return number1 + number2