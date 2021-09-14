arr = [1,2,3,5,6,7]
n = len(arr)
total = 0
sum_arr = sum(arr)
for i in range(1,n+2):  
    total += i
number = total-sum_arr
print("Missing Number:",number)