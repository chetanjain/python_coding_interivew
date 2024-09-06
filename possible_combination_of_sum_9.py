l = [2, 8, 4, 7, 9, 5, 1]
val=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        print(l[i],l[j])
        print(l[i]+l[j])
        if l[i]+l[j] ==9:
            val.append((l[i],l[j]))
print(val)
        
        

