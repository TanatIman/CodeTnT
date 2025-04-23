signsymbol=1
P=0
x=1
for i in range(1,21):
    P+=signsymbol*((x**i)/i)
    signsymbol=-signsymbol
    print(P)