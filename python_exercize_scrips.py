l1 = []
for x in range(2000,3000):
    if (x%7==0)and(x%5!=0):
        l1.append((str(x)))
print((','.join(l1)))      #python string join method
print('=======================')
'''

print('please enter a text: ')
inputchar = input('please enter text': )
if inputchar:
    string = ''
    for x in inputchar:
        if inputchar.index(x)%2 == 0:
            string += str(x)

print('============================')
print("you entered:", inputchar)
print('the result:')
print(string)
'''

'''
print('please enter text:: ')
y = input()
for letter in range(ord('a'),ord('z')+1):    #ord() gets the ascii value of a char
    letter = chr(letter)                      #chr()gets the char of an ascii value
    count = y.count(letter)
    if count > 0:
        print(letter,count, end='')  #makes it write in collum
        print('\n') #new collum
'''

word = input('please input a word to reverse it: ')
for char in range(len(word)-1,-1,-1):
    print(word[char], end = '')
