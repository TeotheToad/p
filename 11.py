n = str(input())
m = str(input())
i = 0
j = 0
while j < len(m) and i < len(n):
    if n[i]!=m[j] :
        j = j + 1
    else :
        i = i + 1
        j = j + 1     
if j==len(m):
    if n[0]==m[j-1]:
            print('Yes')
    else:
        print('No')
elif j < len(m):
    if n[0]==m[j]:
        print('Yes')
    else:
        print('No')