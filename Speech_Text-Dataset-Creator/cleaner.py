import glob
import string
import re

FileList = glob.glob('./raw data/*.txt')
print('Select a file: type a number: 1, 2, 3...')
counter = 1
for file in FileList:
    print(counter+') '+file+'\n')

print('?')
select = int(input())
# load text
file = open(FileList[select-1], 'r', encoding='utf-8')
text = file.read()
file.close()

print(re.sub(r"[^\u0900-\u0963]+", " ", text))
cleaned = re.sub(r"[^\u0900-\u0963]+", " ", text)
# print('   ' , cleaned)

cleaned_word = cleaned.split()
# print('one word ' , cleaned_word[1])
# counter = 0
      
with open('cleaned.txt', 'w+', encoding='utf-8') as f:
    
    for i, word in enumerate(cleaned_word):
        f.write(word)
        # print(i, word)
        if ((i+1) % 12 == 0):
            f.write('\n')
        else:
            f.write(' ')
