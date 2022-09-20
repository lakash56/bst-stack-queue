
S =[]
x= input("inset number separated by space")
S =x.split()
for i in range (len(S)):
    S[i]= int(S[i])
print (S)


print ('initial stack: ', S)
l= len(S)
for i in range(l,0,-1):
    stack=[]
    stack.append(S.pop())
    print(stack)

    
