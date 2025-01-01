#Finding Prime Number between given numbers
s = int(input('Enter the Initial Number : '))
e = int(input('Enter the Final Number : '))

print('The Prime Numbers in between',s,'and',e,'is : ')

for i in range(s, e+1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i) 
             