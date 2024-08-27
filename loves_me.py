def loves_me(num):
    result = ''

    for i in range(num):

        if(i % 2 == 0):
            if (i == num - 1):
                result += 'LOVES ME'
                continue
            result += 'Loves me, '
        else:
            if (i == num - 1):
                result += 'LOVES ME NOT'
                continue
            result += 'Loves me not, '
    return result

print(loves_me(3))
print(loves_me(6))
print(loves_me(1))