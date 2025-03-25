def maxmin_select(arr, left, right):
    if left == right: 
        return arr[left], arr[left]
    
    if right - left == 1: 
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]
    
    mid = (left + right) // 2 
    min1, max1 = maxmin_select(arr, left, mid) 
    min2, max2 = maxmin_select(arr, mid + 1, right)
    
    return min(min1, min2), max(max1, max2)  

if __name__ == "__main__":
    arr = [1, 7, 9, 2, 8, 4, 6, 5]
    minimum, maximum = maxmin_select(arr, 0, len(arr) - 1)
    print(f"menor elemento: {minimum}, maior elemento: {maximum}")
