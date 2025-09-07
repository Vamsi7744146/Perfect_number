#Write a program perfect number with range
ll=int(input())
ul=int(input())
for num in range(ll,ul+1):
    
    summ=0
    for dsumm in range(1,num//2+1):
      
        if num%dsumm==0:
            summ+=dsumm

    if num==summ:
        print(num)