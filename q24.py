a=[1,2,3,4,5,6,7,8,9,10,20,30]
len_a=len(a)
S=0
for i in range(1,len_a,2):
    S+=a[i]
S=S/(len_a//2)
print(S)
