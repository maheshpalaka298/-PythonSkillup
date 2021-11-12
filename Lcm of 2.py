a=int(input('Enter a Number'))
b=int(input('Enter a Number'))
d=1
i=2
while True:
    if a%i==0 and b%i==0:
        a=a//i
        b=b//i
        d*=i
    elif a<=i or b<=i:
        d=d*a*b
        break
    else:
        i+=1
print(d)
