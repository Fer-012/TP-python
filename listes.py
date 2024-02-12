from cmath import sqrt


l1 = []
for i in range(20):
    if i%2==0:
        l1.append(i)
print(l1)

l2 = l1 [2:5]
print(l2)

l3 = l1 [1:-1]
print(l3)

l4 = list(range(9,-1,-2))
print(l4)

l5 = []
for i in l4:
    l5.append(sqrt(i))
print(l5)