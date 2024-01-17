#Compound Operators--Bitwise AND (&)
j=7 #binary  111
j&=6 #binary 110
print(j) #binary 110 #output 6

i=10 #binary  1010
i&=15 #binary 1111
print(i)#binary 1010 #output 10

a=50 #binary     110010
a&=40 #binary    101000
print(a) #binary 100000 #output 32

b=20 #binary  10100
b&=15 #binary 01111
print(b) #binary 00100 #output4

c=17  #binary 10001
c&=14 #binary 01110
print(c)  #binary 0000 #output 0

#Bitwise OR (|)
d=6 #binary  110
d|=7 #binary 111
print(d)#binary 111 #output 7

e=8 #binary   1000
e|=10 #binary 1010
print (e) #binary 1010 #output 10

f=9 #binary 1001
f|=9 #binary 1001
print(f) #binary 1001 #output 9

g=4 #binary 0100
g|=20  #binary 10100
print(g) #binary 10100 #output 20

h=5 #binary  101
h|=6 #binary 110
print(h) #binary 111 #output 7

#Bitwise XOR (^)
k=7 #binary  111
k^=7 #binary 111
print(7) #binary 111 #output 7

l=11 #binary  1011
l^=15 #binary 1111
print(l) #binary 0100 #output 4

m=18 #binary   10010
m^=20 #binary  10100
print(m) #binary 00110 #output 6

n=30  #binary  011110
n^=35 #binary  100011
print(n)#binary  111101 #output 61

q=40 #binary 101000
q^=20#binary 010100
print(q) #binary 111100 #output 60

#Bitwise NOT (~)
t=25
num=~t
print(bin(t))
print(bin(num))
print(num) 

u=20
value=~u
print(bin(u))
print(bin(value))
print(value)

#Bitwise left shift(<<)

v=12
v1= v<<4
print(v1)


V=15
V1=V<<3
print(V1)

#Bitwise RIGHT shift(>>)
w=25
w1=w>>3
print(w1)

z=40
z1=z>>2

print(z1)




