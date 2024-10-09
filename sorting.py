def bubble(bubble_list):
    length = len(bubble_list)
    times = 0
    for x in range(length):
        times += 1
        sorted = True
        for y in range(length-x-1):
            if bubble_list[y] > bubble_list[y+1]:
                keep = bubble_list[y]
                bubble_list[y] = bubble_list[y+1]
                bubble_list[y+1] = keep
                sorted = False
        if sorted == True:
            break
    print(times)
    return bubble_list

def selection(selection_list):
    length = len(selection_list)
    for x in range(length):
        min = selection_list[x]
        location = x
        for y in range(length - x):
            if min > selection_list[y+x]:
                min = selection_list[y+x]
                location = y+x
        selection_list[location] = selection_list[x]
        selection_list[x] = min
    return selection_list

def insertion(insertion_list):
    length = len(insertion_list)
    for x in range(length):
        y = x
        while y > 0:
            if insertion_list[y] < insertion_list[y-1]:
                keep = insertion_list[y]
                insertion_list[y] = insertion_list[y-1] 
                insertion_list[y-1] = keep
            else:
                break
            y -= 1
    return insertion_list

def shell(shell_list):
    return(selection(shell_list))

def quicksort(quick_list, low = 0, high = -1):
    if high == -1:
        high = len(quick_list)
    if(low < high):
        pivot_location = partition(quick_list, low, high)
        quick_list = quicksort(quick_list, low, pivot_location)
        quick_list = quicksort(quick_list, pivot_location + 1, high)
    print(quick_list)
    return(quick_list)

def partition(quick_list, low, high):
    midpoint = low + (high - low) // 2
    pivot = quick_list[midpoint]
    leftwall = low

    for i in range(low, high):
        if quick_list[i] < pivot:
            keep = quick_list[i]
            quick_list[i] = quick_list[leftwall]
            quick_list[leftwall] = keep
            leftwall += 1
    keep = quick_list[leftwall]
    quick_list[leftwall] = pivot
    pivot = keep
    return(leftwall)
