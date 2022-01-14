def mergesort(a):
    if len(a) <= 1:
        return a
    x = mergesort(a[0:len(a)//2])
    y = mergesort(a[len(a)//2:len(a)])
    sorted_array = []
    i = j = 0

    while i < len(x) and j < len(y):
            
            if x[i]< y[j]:
                sorted_array.append(x[i])
                i += 1
                
            else:
                sorted_array.append(y[j])
                j += 1

    for k in range(i, len(x)):
            sorted_array.append(x[k])

    for l in range(j, len(y)):
            sorted_array.append(y[l])
            
    return sorted_array

x = list(map(int,input().split()))
print(mergesort(x))
