#wrie a program of 1 to nth perfect  number

n = int(input("Enter how many perfect numbers you want: "))
count = 0
num = 2

while count < n:
    summ = 0
    for dnum in range(1, num // 2 + 1):
        if num % dnum == 0:
            summ += dnum
    if num == summ:
        count += 1
        print(count, "→", num, "is a perfect number")
    num += 1


