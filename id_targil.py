'''
כתוב תוכנית אשר קולטת מהמשתמש שני ערכים: מס' תעודת זהות + שם מלא. תעודת הזהות
תשמש בתור המפתח במילון, והשם שנקלט ישמש בתור הערך. ראשית בדוק אם מפתח זה קיים
במילון- אם כן, אל תדרוס את הערך הקיים והצג הודעה. אם המפתח לא קיים- הוסף ערך זה
למילון. חזור על הפעולה עד אשר המשתמש יכניס 1 -עבור מספר תעודת הזהות. לאחר שיסתיימו
כל הקלטים- הדפס את כל ערכי המילון שנצברו: מפתח + ערך
'''

d = {}
id = input("Please enter your ID: ")
while id != '-1':
    name = input("Please enter your name: ")

    if d.get(id) == None:
        d [ id ] = name
    else:
        print(f'key {id} already exists!')

    id = input("Please enter your ID: ")

for k,v in d.items():
    print(f'{k} : {v}')
© 2021 GitHub, Inc.
