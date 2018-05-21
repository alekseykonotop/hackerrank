def catAndMouse(x, y, z):
    if abs(x-z) == abs(y-z):
        return 'Mouse C'
    elif abs(x-z) < abs(y-z):
        return 'Cat A'
    elif abs(x-z) > abs(y-z):
        return 'Cat B'


print(catAndMouse(2, 6, 5))
print(catAndMouse(1, 3, 2))

