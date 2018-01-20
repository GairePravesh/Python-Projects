def no_to_alpha(n):
    string = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        #print(n,remainder)
        string = chr(65 + remainder) + string
       # print(string)
    return string

def alpha_to_no(n):
    expn = 0
    col_num = 0
    for char in reversed(n):
       # print(char,ord(char),ord('A'))
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
            
