n=10
p=100
r=5
#calculate A

A=p * (1+r/100) ** n
print(A)

total=lambda n,p,r: p * (1+r/100) ** n

print(total(10,100,5))

print(total(10,500,5))

print(total(20,100,5))


print(total(10,100,15))

print(total(190,100,5))


