#write a program to check the given number is perfect or not
n=int(input())
summ=0

for dnum in range(1,n//2+1):

    if n%dnum==0:
        summ+=dnum
if n==summ:
   print('n is perfect')
else:
   print(' n is not perfect') 