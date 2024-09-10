# write a code to separate out integers and strings and sum the integers.
# Examples
# st = "50GS50HH100HT50GG" -> 50,50,100,50 and sum will be 250

# option 1
import re
pattern = r'\d+'
st = "50GS50HH100HT50GG" 
data = re.findall(pattern,st)
print(data)

#OR Option 2

data=[]
single_var='0'
for index,i in enumerate(st):
  if i.isdigit():
    single_var = single_var+i
    if len(st)==index+1:
      data.append(int(single_var))
  else:
    data.append(int(single_var))
    single_var = '0'
print(data)
print(sum(data))
