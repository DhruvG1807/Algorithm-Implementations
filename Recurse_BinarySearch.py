def binary_search(lst, target, first, last):
    
    if (first>last):
        return -1
        
    else:
        midpt = (last+first)//2
    
        if (lst[midpt] == target):
            return midpt
            
        else:
            if (lst[midpt] > target):
                return binary_search(lst,target,first,midpt-1)
            else:
                return binary_search(lst,target,first+1,last)
    
    


if __name__ == '__main__':
    
    lst = list(map(int,input().split()))
    el = int(input())
    
    index = binary_search(lst,el,0,len(lst)-1)
    
    if index != -1:
        print(f"Element is present at index {index}")
    else:
        print("Element is not present in array")
    
    