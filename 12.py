a, b, c, d, e = input()
x=[]
x.append (a)
x.append (b)
x.append (c)
x.append (d)
x.append (e)
if x.count('R')>=3 :
    print('nakhor lite')
elif x.count('R')>=2 and x.count('Y')>=2 :
    print('nakhor lite')
elif x.count('G')==0:
    print('nakhor lite')
else:
    print('rahat baash')