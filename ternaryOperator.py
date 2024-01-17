#ternary Operator
j=57 if 30<57 else 57
print(j)

x=10
y=30
value= x if x>y else y
print (value)

num="even" if 31%2 ==0 else "odd"
print(num)

a=-4
valuea="positive" if a>0 else "Negative"
print(valuea)

a,b,c=19,20,0
abc= a if (a>b and a>c) else (b if b>c else c)
print(abc)