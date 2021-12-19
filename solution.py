def find_min(numbers):
    _min = 0
    flag = False
    for i in numbers:
        if flag == False or i < _min:
            _min = i
            flag = True
    if flag:
        return _min
    else:
        return None


def find_max(numbers):
    _max = 0
    flag = False
    for i in numbers:
        if flag == False or i > _max:
            _max = i
            flag = True
    if flag:
        return _max
    else:
        return None

def find_sum(numbers):
    _sum = 0
    flag = False
    for i in numbers:
        _sum += i
        flag = True
    if flag:
        return _sum
    else:
        return None


def find_product(numbers):
    prod = 1
    flag = False
    for i in numbers:
        prod *= i
        flag = True
    if flag:
        return prod
    else:
        return None


with open("input.txt", "r") as file:
    numbers = [int(i) for i in file.read().split()]
print("Минимальное:", find_min(numbers))
print("Макимальное:", find_max(numbers))
print("Сумма:", find_sum(numbers))
print("Произведение:", find_product(numbers))
