import random
n=10
S=[]
while(len(S)<n):
    a=random.randint(5,54)
    if a%5==0:
        S.append(a)
print(S)