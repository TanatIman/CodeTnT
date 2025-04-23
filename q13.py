a=1
b=2
c=3
x=1
while x<=7:
    if x<3:
        y=a*x*x+b*x+c
    elif x==3:
        y=2*x+c*x+b
    else:
        y=3*x*x-x-1
    x+=0.5
    print(y)