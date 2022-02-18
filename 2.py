a = [1,2,3,2,1]

p1 = []
p2 = []

x = p2

for i in range(len(a)):
    x.append(a[i])

    if a[i] % 2 == 0:
        x = p2
    else:
        x = p1

print(f'p1 : {sum(p1)}')
print(f'p2 : {sum(p2)}')