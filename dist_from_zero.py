def distance_from_zero(num):
    if type(num) == int or float:
        return abs(num)
    else:
        return("Nope")

print distance_from_zero(-32)