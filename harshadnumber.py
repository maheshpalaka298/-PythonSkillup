num=int(input('Enter a number'))
sum=rem=0
n=num
while(n > 0):
    rem = n%10;    
    sum = sum + rem;    
    n = n//10;
if (num%sum==0):
    print('Harshed number')
else:
    print('not harshad number')



            
    

