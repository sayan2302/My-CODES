#inline sorting

def sort(l):
    if len(l)<=1:return
    m=len(l)//2
    sort(l[:m])
    sort(l[m:])
    merge(l[:m],l[m:],l)
def merge(x,y,l):
    i=j=k=0
    while True:
        if i==len(x) or j==len(y):
            if j==len(y):l=l[:k]+x[i:]
            else:l=l[:k]+y[j:]
            break
        if x[i]>=y[j]:
            l[k]=y[j]
            j+=1
            k+=1
        else:
            l[k]=x[i]
            i+=1
            k+=1
l=[17,21,29,38,4,9,25,32]
sort(l)
print(l)
