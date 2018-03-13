#!python3

def getMode():
    while True:
        print("Encrypt or Decrypt?")
        mode=input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print("Enter correct choice")

def getMessage():
    print("Enter text to convert")
    return input()

def getKey():
    while True:
        print("Enter any key from 1 to 26")
        key=int(input())
        if(key>=1 and key<=26):
            return key

def getTranslatedMessage(mode,message,key):
    if mode[0]=='d':
        key=-key
    translated=""
    for symbol in message:
        if symbol.isalpha():
            num=ord(symbol)
            num+=key
            if symbol.isupper():
                if num>ord('Z'):
                    num-=26
                elif num<ord('A'):
                    num+=26
            elif symbol.islower():
                if num>ord('z'):
                    num-=26
                elif num<=ord('a'):
                    num+=26
            translated+=chr(num)
        else:
            translated+=symbol
    return translated

mode=getMode()
message=getMessage()
key=getKey()

print("Translated text:")
print(getTranslatedMessage(mode,message,key))

        
