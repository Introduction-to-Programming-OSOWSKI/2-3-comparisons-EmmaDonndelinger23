#WRITE YOUR CODE IN THIS FILE
def greaterThan(x, y):
    if x > y:
        return True
    else:
        return False

def lessThan(x, y):
    if x < y:
        return True
    else:
        return False

def equalTo(x, y):
    if x == y:
        return True
    else:
        return False

def greaterOrEqual(x, y):
    if x >= y:
        return True
    else:
        return False

def lessOrEqual(x, y):
    if x <= y:
        return True
    else:
        return False
print(greaterThan(10, 2))
print(lessThan(10, 2))
print(equalTo(5, 5))
print(greaterOrEqual(4, 6))
print(lessOrEqual(10, 2))