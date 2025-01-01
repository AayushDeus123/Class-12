num = int(input("Enter a number greater than 3 digits: "))
t = num
numlen = 0
mid1 = 0
mid2 = 0

while t > 0:
    numlen = numlen + 1
    t = int(t / 10)

if numlen >= 4:
    numlen = int(numlen / 2)
    check = 0
    while num > 0:
        rem = num % 10
        if check == numlen:
            mid1 = rem
        elif check == (numlen - 1):
            mid2 = rem
        num = int(num / 10)
        check = check + 1
    prod = mid1 * mid2
    print("The product of the 2 middle numbers is ", prod)
else:
    print("The given number should be 4 or greater")