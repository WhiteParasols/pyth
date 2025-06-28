numbers=[1,3,5,7,8,11,13,15,17,19]

def binary_search(numbers, target):
    left=0
    right=len(numbers)-1

    while left<=right:
        mid=(left+right)//2 #몫
        if numbers[mid]==target:
            return mid
        elif numbers[mid]<target:
            left=mid+1
        else:
            right=mid-1
        
    return -1

print(binary_search(numbers,17))