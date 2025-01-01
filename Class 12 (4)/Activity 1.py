#Character occurence
string = input('Enter a word (string): ')
char = input('Enter a character (letter) : ')
n = 0
count = 0

while n < len(string):
    if string[n] == char:
        count = count + 1
    n = n + 1
print("The number of ",char,"'s in ",string,"is ",count)