s='aabxaabxcaabxaabxay'
z=[0]

for i in range(1,len(s)):
    p1=0
    p2=i
    c=0
    while p2<len(s) and s[p1]==s[p2]:
        c+=1
        p1+=1
        p2+=1
    z.append(c)
  
print('maximum length: ',max(z))
print('start position: ',z.index(max(z)))
print('end position: ',z.index(max(z))+max(z))
print('substring: ',s[z.index(max(z)):z.index(max(z))+max(z)])
