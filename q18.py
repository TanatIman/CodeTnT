import math
cos_num=1
y=0
x=1
for t in range(12):
    y+=math.cos(cos_num*x)/math.sin((cos_num**2)*x)
    cos_num+=1
    print(y)
