def find_total_water(arr, n):
    
    total_water = 0
    
    left_max = 0
    right_max = 0
    
    lo = 0
    hi = n-1
      
    while(lo <= hi):
     
        if(arr[lo] < arr[hi]):
         
            if(arr[lo] > left_max):
                left_max = arr[lo]
            else:
                total_water += left_max - arr[lo]
            lo+= 1        
        else:
            if(arr[hi] > right_max):
                right_max = arr[hi]
            else:
                total_water += right_max - arr[hi]
            hi-= 1
         
    return total_water

if __name__ == '__main__':
    arr = [4,2,0,3,2,5]
    n = len(arr)
    print(find_total_water(arr,n))