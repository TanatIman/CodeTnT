import random
n=9
s=[]
while len(s)<n:
    a=random.randint(-12,24)
    if a<0:
        s.append(a)


product=1
for k in s:
    product*=k
print(product)