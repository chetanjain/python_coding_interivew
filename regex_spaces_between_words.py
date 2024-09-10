import re
p = re.compile('[A-Z][a-z]+')
text = 'BruceWayneIsBatman'
data = p.findall(text)

for i in range(0,len(data)):
    data[i]=data[i].lower()
    
print(' '.join(data))
