
#qustion:Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.


l1 = []
for x in range(2000,3000):
    if (x%7==0)and(x%5!=0):
        l1.append((str(x)))
print((','.join(l1)))      #python string join method
print('=======================')
'''
#Please write a program which accepts a string from console and print it in reverse order

word = input('please input a word to reverse it: ')
for char in range(len(word)-1,-1,-1):
    print(word[char], end = '')
