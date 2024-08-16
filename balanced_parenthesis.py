data = "[(()}}"
dd = list(data)
dictBracket = {'(':')',
                '{':'}',
                '[':']'}
stack = []
for i in dd:
    if dictBracket[i] == dd[-1]:
        dd.pop()
    else: 
        stack.append(i)
        dd.pop()
        
    print(dd)
    print(stack)

        
