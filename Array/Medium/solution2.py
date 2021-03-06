#Clockwise Direction
def rotateArray(arr,start,end):
    while(start<end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

def leftrotate(arr,d,n):
    if d == 0:
        return 0
    else:
        rotateArray(arr,d+1,n-1)
        rotateArray(arr,0,d)
        rotateArray(arr,0,n-1)

def print_array(arr):
    for i in range(0,n):
        print(arr[i], end=' ')

if __name__ == '__main__':
    arr = [10, 20, 30, 40, 50]
    print("Write the d Element to rotate the array:")
    d = int(input())
    print("Rotated Array:")
    n = len(arr)
    leftrotate(arr,d,n)
    print_array(arr)