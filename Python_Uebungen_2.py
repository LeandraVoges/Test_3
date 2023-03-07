l1 = [1,4,4,4,4,4,4,4]

l2 = []

for zahl in l1:
    if zahl != 4:
        l2.append(zahl)

l1 = l2
        
print(l1)