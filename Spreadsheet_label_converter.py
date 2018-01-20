'''
Pravesh Gaire

Python3.5

Spreadsheets show row and columns in two formats, either R34C56 or 56BC
where R and C are rows and columns respectively and 56 is Column while BC is row
So this program just converts numbers and alphabets into other form.
This converted datas are used to represent the rows and columns.

We do some calculations on input data on basis of their ASCII values and get result
'''

def no_to_alpha(n):
    string = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string
    return string

def alpha_to_no(n):
    expn = 0
    col_num = 0
    for char in reversed(n):
        col_num += (ord(char) - ord('A') + 1) * (26 ** expn)
        expn += 1
    return col_num

while(True):
    print("Enter number to convert to word or word to convert to number ( 1 / 2)")
    enter=input()
    if enter=="1":
        print(no_to_alpha(int(input())))
    if enter=="2":
        print(alpha_to_no(input()))
    print("Continue ? ( y / n)")
    if input()=="n":
        break
            
