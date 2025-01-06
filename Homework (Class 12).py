#Converting Decimal Numbers into Binary Numbers
dn = float(input("Enter a decimal number : "))

binary = ""
while dn > 0:
    binary = str(dn % 2) + binary
    dn //= 2

print("The Decimal number in Binary is :", binary)