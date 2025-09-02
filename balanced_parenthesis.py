data = "{[()(]}"
dd={}
for val in data:
    if val in dd.keys():
        count = dd[val]+1
        dd[val]=count
    else:
        dd[val]=1
        
print(dd)

if dd['{']!=dd['}']:
    print('{,}')
if dd['[']!=dd[']']:
    print('[,]')
if dd['(']!=dd[')']:
    print('(,)')
