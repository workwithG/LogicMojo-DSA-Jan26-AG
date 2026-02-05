from Week4Day1 import binary_search_idx, first_occurrence_target, binary_search_idx_floor, binary_search_idx_ceil


def num_of_rotations(arr):
    n = len(arr)
    start_idx = 0
    end_idx = n - 1
    mid_idx = 0
    if arr[start_idx] <= arr[end_idx]:
        return 0
    while start_idx <= end_idx:
        mid_idx = start_idx + (end_idx - start_idx) // 2
        prv = (mid_idx - 1 + n) % n
        nxt = (mid_idx + 1) % n
        if (arr[mid_idx] <= arr[prv] and arr[mid_idx] <= arr[nxt]):
            return mid_idx
        if arr[start_idx] > arr[mid_idx]:
            end_idx = mid_idx - 1
        elif arr[mid_idx] > arr[end_idx]:
            start_idx = mid_idx + 1
    return 0

def num_of_rotations_duplicates(arr):
    n = len(arr)
    start_idx, end_idx = 0, n - 1

    while start_idx < end_idx:
        # If strictly increasing, start is the minimum
        if arr[start_idx] < arr[end_idx]:
            return start_idx

        mid_idx = start_idx + (end_idx - start_idx) // 2

        # Ambiguous due to duplicates: shrink safely
        if arr[start_idx] == arr[mid_idx] == arr[end_idx]:
            start_idx += 1
            end_idx -= 1
            continue

        # Decide which half contains the minimum (compare mid vs end)
        if arr[mid_idx] <= arr[end_idx]:
            end_idx = mid_idx
        else:
            start_idx = mid_idx + 1

    return start_idx

def binary_search_rotated(arr, target):
    pivot = num_of_rotations_duplicates(arr)
    if arr[pivot] == target:
        return pivot
        
    
    l_block = binary_search_idx(arr[:pivot], target)
    if l_block != -1:
        return l_block
    r_block = binary_search_idx(arr[pivot+1:], target)
    if r_block != -1:
        return pivot + 1 + r_block

    return -1


def search_infinite_array(arr, target):
    start_idx = 0
    end_idx = 1
    while start_idx <= end_idx:
        if arr[end_idx] < target:
            start_idx = end_idx + 1
            end_idx = end_idx * 2
            if end_idx >= len(arr):
                end_idx = len(arr) - 1
        else:
            break
    result = binary_search_idx(arr[start_idx:end_idx+1], target)

    return result if result == -1 else start_idx + result


def first_occurrence_infinite_binary_array(arr, target):
    start_idx = 0
    end_idx = 1
    while start_idx <= end_idx:
        if arr[end_idx] < target:
            start_idx = end_idx + 1
            end_idx = end_idx * 2
            if end_idx >= len(arr):
                end_idx = len(arr) - 1
        else:
            break
    result = first_occurrence_target(arr[start_idx:end_idx+1], target)
    return result if result == -1 else start_idx + result


def min_diff_sorted_array(arr, target):
    """
    Find the element in a sorted array that has the minimum difference with the given target.
    """
    floor_idx = binary_search_idx_floor(arr, target)
    ceil_idx = binary_search_idx_ceil(arr, target)

    if floor_idx < 0:
        floor_idx = 0
    if ceil_idx >= len(arr):
        ceil_idx = len(arr) - 1

    if abs(arr[floor_idx] - target) <= abs(arr[ceil_idx] - target):
        return arr[floor_idx]
    else:
        return arr[ceil_idx]


if __name__ == "__main__":
   print(" Week 4 Day 2")

   #print(f'Index of Rotation: {num_of_rotations([15, 18, 2, 3, 6, 12])}')
   #print(f'Index of Rotation: {num_of_rotations([7, 9, 11, 12, 5])}')
   #print(f'Index of Rotation: {num_of_rotations([7, 9, 11, 12, 15])}')
   #print(f'Index of Rotation: {num_of_rotations([7, 8, 9, 1, 2, 3,4,5,6])}')

   #print(f'Index of Rotation with Duplicates: {num_of_rotations_duplicates([2, 2, 2, 3, 4, 2])}')
   #print(f'Index of Rotation with Duplicates: {num_of_rotations_duplicates([10, 10, 10, 1, 10, 10])}')
   #print(f'Index of Rotation with Duplicates: {num_of_rotations_duplicates([1, 1, 1, 1, 1])}') 
   print(f'Index of Rotation with Duplicates: {num_of_rotations_duplicates([4,5,6,7,0,0,0,1,2])}')


   #print(f'Binary Search in Rotated Array: {binary_search_rotated([15, 18, 2, 3, 6, 12], 3)}')
   #print(f'Binary Search in Rotated Array: {binary_search_rotated([7, 9, 11, 12, 5], 9)}')
   #print(f'Binary Search in Rotated Array: {binary_search_rotated([7, 9, 11, 12, 15], 15)}')
   #print(f'Binary Search in Rotated Array: {binary_search_rotated([7, 8, 9, 1, 2, 3,4,5,6], 4)}')

   #print(f'Search in Infinite Array: {search_infinite_array([3,5,7,9,10,90,100,130,140,160,170], 10)}')
   #print(f'Search in Infinite Array: {search_infinite_array([3,5,7,9,10,90,100,130,140,160,170], 160)}')
   #print(f'Search in Infinite Array: {search_infinite_array([3,5,7,9,10,90,100,130,140,160,170], 3)}')
   #print(f'Search in Infinite Array: {search_infinite_array([3,5,7,9,10,90,100,130,140,160,170], 175)}')

   #print(f'First Occurrence in Infinite Binary Array: {first_occurrence_infinite_binary_array([0,0,0,0,0,0,1,1,1,1,1,1,1,1,1], 1)}')
   #print(f'First Occurrence in Infinite Binary Array: {first_occurrence_infinite_binary_array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], 1)}')
   #print(f'First Occurrence in Infinite Binary Array: {first_occurrence_infinite_binary_array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 1)}')

   #print(f'Minimum Difference in Sorted Array: {min_diff_sorted_array([4,6,10], 7)}')
   #print(f'Minimum Difference in Sorted Array: {min_diff_sorted_array([4,6,10], 4)}')
   #print(f'Minimum Difference in Sorted Array: {min_diff_sorted_array([1,3,8,10,15], 12)}')
   #print(f'Minimum Difference in Sorted Array: {min_diff_sorted_array([4,6,10], 17)}')