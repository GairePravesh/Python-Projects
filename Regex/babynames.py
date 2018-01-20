'''
Pravesh Gaire

Names extractor from a google regex practise website

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...
So we used regex to filter all the names.
'''
import re
import sys
def extract_names(filename):
  names=[]
  f=open(filename,'rU')#rU opens file in universal line mode
  text=f.read()
  year_match=re.search(r'Popularity\sin\s(\d{4})',text)
  if not year_match:
    sys.stderr.write('Couldnot find year\n')
    sys.exit(1)
  year=year_match.group(1)
  names.append(year)
  tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', text)
  namesDict={}
  for ttuple in tuples:
    rank,boy,girl=ttuple
    if boy not in namesDict:
      namesDict[boy]=rank
    if girl not in namesDict:
      namesDict[girl]=rank
    namess=sorted(namesDict.keys())
  for name in namess:
    names.append(name+" "+namesDict[name])
  return names
#print(extract_names('baby2008.html'))
def main():
  file_name='baby2008.html'
  names=extract_names(file_name)
  text='\n'.join(names)
  print(text)
if __name__=='__main__':
  main()
