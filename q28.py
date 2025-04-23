A=[1,2,3,4,5,6,7,8,9,20,12,32,-421,231,424]
S=0
for k in A:
    if k>=0:
        S+=k
    else:
        break
print(S)