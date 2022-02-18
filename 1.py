a = [1,2,3,2,1]
b = []
for i in range(len(a)):
    if a[i] in b:
        print(f'First occured duplicate in the given array : {a[i]}')
        break
    else:
        b.append(a[i])
