import random
s=[]
for n in range(10):
    s.append(random.randint(0,23))
product=1

for k in s:
    product*=k
print(product)