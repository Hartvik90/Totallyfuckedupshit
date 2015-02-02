def cube(number):
    return number*number*number
    
def by_three(number):
    if number % 3 == 0:
        cube(number)
        return cube(number)
    else:
        return "Not divisible by three"

print by_three(9)