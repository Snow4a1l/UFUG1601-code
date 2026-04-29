n = int(input())
arr = list(map(int, input().split()))
sorted_arr = arr.copy()

is_initial_sorted = True
for k in range(n - 1):
    if sorted_arr[k] > sorted_arr[k + 1]:
        is_initial_sorted = False
        break
if is_initial_sorted:
    print(' '.join(map(str, sorted_arr)))
else:
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if sorted_arr[j] < sorted_arr[min_idx]:
                min_idx = j
        
        swapped = False
        if min_idx != i:
            sorted_arr[i], sorted_arr[min_idx] = sorted_arr[min_idx], sorted_arr[i]
            swapped = True
        
        if swapped:
            print(' '.join(map(str, sorted_arr)))
        
        is_sorted = True
        for k in range(n - 1):
            if sorted_arr[k] > sorted_arr[k + 1]:
                is_sorted = False
                break
        
        if is_sorted:
            if not swapped:
                print(' '.join(map(str, sorted_arr)))
            break 