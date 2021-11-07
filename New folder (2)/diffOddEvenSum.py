def diffOddEvenSum(num):
    odSum = 0
    evenSum = 0
    for i in num[0::2]:
        odSum = odSum + int(i)
    for i in num[1::2]:
        evenSum = evenSum + int(i)
    diff = odSum - evenSum
    return diff

print(diffOddEvenSum("12345"))
