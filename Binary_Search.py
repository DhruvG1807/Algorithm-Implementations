def binary_search(lst, target):
    first = 0
    last = len(lst) - 1
    
    while (last >= first):
        midpt = (last+first)//2
        
        if lst[midpt] == target:
            return midpt
            
        else:
            if lst[midpt] > target:
                last = midpt-1
            else:
                first = midpt+1
    
    return -1


if __name__ == '__main__':
    
    lst = list(map(int,input().split()))
    el = int(input())
    
    index = binary_search(lst,el)
    
    if index != -1:
        print(f"Element is present at index {index}")
    else:
        print("Element is not present in array")
    
    