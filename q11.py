import math

a=4**(-0.25)-(2**(2**0.5))**(-4/3)*math.tan(4)
b=math.cos(2*math.tan(1/5)-math.tan(1/4))

if abs(a)<abs(5*b):
    k=math.log(abs(2*a-3*(math.e)**2*b))
else:
    k=math.log(abs(2*a*(math.e**2)-3*b))
print(k)