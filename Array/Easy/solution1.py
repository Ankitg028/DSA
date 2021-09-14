N = int(input())
odd = []
even = []
for i in range(0,N):
    if(i%2!=0):
        odd.append(i)
    else:
        even.append(i)
print("Even Number:",even)
print("Odd Number:",odd)