import random
s=[]
n=1
while (len(s)<n):
    a=random.randint(4,47)
    if a%3==1:
        s.append(a)

product=1
for k in s:
    product*=k
print (product)