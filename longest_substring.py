val = 'Hellomynameischetanjain'

substring=''
maxLen=1
for i in val:
    if i not in substring:
        substring =substring+i
        maxLen = max(maxLen,len(substring))
    else:
        substring = substring.split(i)[1]+i
        
    print(substring)

print(maxLen)
    
