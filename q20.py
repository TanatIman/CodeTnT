import math
i=1
y=0
x=2
for n in range(10):
    y+=(math.sin(x)**i)/x**i
    i+=1
    print(y)