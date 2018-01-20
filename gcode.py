'''
Pravesh Gaire
Extracting X and Y axis from G_code file 
and saving them into a new file

Not the best one but accurate enough
decimals are removed and duplicate data are deleted for our project need.

Requirements:
g_code file  and a extra file to save data needed in same directory
##########################################################################
import math
file1=open("g_code.nc","r")
#c=0
for lines in file1:
    lineList=lines.split()
    #c+=1
    #print(C)
    if 'X' and 'Y' in lines:
        data=str(math.floor(float((lineList[1][1:]))))+" "+str(math.floor(float((lineList[2][1:]))))+"\n"
        file2=open('test.txt','r')
        lastline=file2.readlines()[-1]
        if data!=lastline:
            file2.close()
            #print(str(round(((c/145000)*100),2))+" % ")
            file2=open("test.txt","a")
            file2.write(data)
            file2.close()
file1.close()        
file2.close()

'''
# Using Regex it was much more easier
# Asked in Stackeroverflow for better approach and I got to know about Regex and its uses in such problems
# Far better approach than previous
#############################################################################

import re
numbers = []

def append_if_different(x, y):
    if not numbers or (x, y) != numbers[-1]:
        numbers.append((x, y))

with open("g_code.nc","r") as inp:
    for line in inp:
        matches = re.findall(r'[XY]([-+]?\d+)', line)
        if len(matches) == 2:
            append_if_different(int(matches[0]), int(matches[1]))

with open("test.txt", "w") as outp:
    for xy in numbers:
        outp.write("{} {}\n".format(*xy))

