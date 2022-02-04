def power(baseNum, power):
    result = 1
    for index in range(power):
        result *= baseNum
    return result


print(power(4, -2))  # Does not work with negative exponents
print(pow(4, -2))
