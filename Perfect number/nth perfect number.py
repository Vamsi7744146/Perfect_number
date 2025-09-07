#write a program of nth perfect number
n = int(input("Enter the value of n: "))
count = 0
num = 2

while True:
    summ = 0
    for dnum in range(1, num // 2 + 1):
        if num % dnum == 0:
            summ += dnum
    if num == summ:
        count += 1
        if count == n:
            print(num, "is the", n, "th perfect number")
            break
    num += 1
