# Kadane's algorithm: Largest Sum Contiguous Subarray

if __name__ == '__main__':
    
    arr = list(map(int,input().split()))
    mx = 0
    sum = 0
    
    for num in arr:
        sum += num
        
        if sum>mx:
            mx = sum
        
        if sum<0:
            sum = 0
    
    print(mx)
