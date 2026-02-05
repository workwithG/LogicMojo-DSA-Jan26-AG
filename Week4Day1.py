def binary_search(arr, target):
    found = False
    start_idx = 0
    end_idx = len(arr) - 1
   
    while start_idx <= end_idx:
        mid_idx = start_idx + (end_idx - start_idx) // 2
        if arr[mid_idx] == target:
            found = True
            break
        elif arr[mid_idx] < target:
            start_idx = mid_idx + 1
        else:
            end_idx = mid_idx - 1
    return found

def binary_search_idx(arr, target):
    start_idx = 0
    end_idx = len(arr) - 1

    while start_idx <= end_idx:
        
        mid_idx = start_idx + (end_idx - start_idx) // 2
        
        if arr[mid_idx] == target:
            return mid_idx
        elif arr[mid_idx] < target:
            start_idx = mid_idx + 1
        else:
            end_idx = mid_idx - 1

    return -1

def binary_search_idx_position(arr, target):
    start_idx = 0
    end_idx = len(arr) - 1

    while start_idx <= end_idx:
        
        mid_idx = start_idx + (end_idx - start_idx) // 2
        
        if arr[mid_idx] == target:
            return mid_idx
        elif arr[mid_idx] < target:
            start_idx = mid_idx + 1
        else:
            end_idx = mid_idx - 1
       
    return start_idx


def binary_search_idx_desc(arr, target):
    start_idx = 0
    end_idx = len(arr) - 1

    while start_idx <= end_idx:
        mid_idx = start_idx + (end_idx - start_idx) // 2
        if arr[mid_idx] == target:
            return mid_idx
        elif arr[mid_idx] > target:
            start_idx = mid_idx + 1
        else:
            end_idx = mid_idx - 1
        
    return -1

def binary_search_order_agnostic(arr, target):
    start_idx = 0
    end_idx = len(arr) - 1
    idx = -1

    if arr[start_idx] > arr[end_idx]:
        idx = binary_search_idx_desc(arr, target)
    else:
        idx = binary_search_idx(arr, target)
    
    return idx

def binary_search_idx_floor(arr, target):
    start_idx = 0
    end_idx = len(arr) - 1

    while start_idx <= end_idx:
        mid_idx = start_idx + (end_idx - start_idx) // 2
        if arr[mid_idx] == target:
            return mid_idx
        elif arr[mid_idx] < target:
            start_idx = mid_idx + 1
        else:
            end_idx = mid_idx - 1
       
    return end_idx

def binary_search_idx_ceil(arr, target):
    start_idx = 0
    end_idx = len(arr) - 1

    while start_idx <= end_idx:
        mid_idx = start_idx + (end_idx - start_idx) // 2
        if arr[mid_idx] == target:
            return mid_idx
        elif arr[mid_idx] < target:
            start_idx = mid_idx + 1
        else:
            end_idx = mid_idx - 1
       
    return start_idx


def first_occurrence_target(arr, target):
    start_idx = 0
    end_idx = len(arr) - 1
    best_idx = -1
    while start_idx <= end_idx:
        mid_idx = start_idx + (end_idx - start_idx) // 2
        if arr[mid_idx] == target:
            best_idx = mid_idx
            end_idx = mid_idx - 1
        elif arr[mid_idx] < target:
            start_idx = mid_idx + 1
        else:
            end_idx = mid_idx - 1

    return best_idx


def last_occurrence_target(arr, target):
    start_idx = 0
    end_idx = len(arr) - 1
    best_idx = -1
    while start_idx <= end_idx:
        mid_idx = start_idx + (end_idx - start_idx) // 2
        if arr[mid_idx] == target:
            best_idx = mid_idx
            start_idx = mid_idx + 1
        elif arr[mid_idx] < target:
            start_idx = mid_idx + 1
        else:
            end_idx = mid_idx - 1

    return best_idx

def number_of_occurrences(arr, target):
    first_idx = first_occurrence_target(arr, target)
    if first_idx == -1:
        return 0
    last_idx = last_occurrence_target(arr, target)
    return last_idx - first_idx + 1

if __name__ == "__main__":
    print(" Week 4 Day 1 ")

    #print(f'Binary Search: {binary_search([1,2,3,4,5,6,7,8,9], 5)}')  
    #print(f'Binary Search: {binary_search([10,20,30,40,50], 25)}')  
    #print(f'Binary Search: {binary_search([-10,-5,0,5,10], -5)}')
    #print(f'Binary Search: {binary_search([-3,0,2,4,6], 3)}')

    #print(f'Binary Search Index: {binary_search_idx([-1,0,1,2,3,4,5,6,7,8,9], 5)}')
    #print(f'Binary Search Index: {binary_search_idx([10,20,30,40,50], 25)}')
    #print(f'Binary Search Index: {binary_search_idx([-1,0,3,5,9,12], -2)}')
    #print(f'Binary Search Index: {binary_search_idx([-1,0,3,5,9,12], 9)}')

    #print(f'Binary Search Index Desc: {binary_search_idx_desc([9,8,7,6,5,4,3,2,1,0,-1], 5)}')
    #print(f'Binary Search Index Desc: {binary_search_idx_desc([50,40,30,20,10], 25)}')
    #print(f'Binary Search Index Desc: {binary_search_idx_desc([12,9,5,3,0,-1], 3)}')
    #print(f'Binary Search Index Desc: {binary_search_idx_desc([12,9,5,3,0,-1], 13)}')

    #print(f'Binary Search Order Agnostic: {binary_search_order_agnostic([4,6,10], 10)}')
    #print(f'Binary Search Order Agnostic: {binary_search_order_agnostic([1,2,3,4,5,6,7,8,9], 5)}')
    #print(f'Binary Search Order Agnostic: {binary_search_order_agnostic([10,6,4], 10)}')
    #print(f'Binary Search Order Agnostic: {binary_search_order_agnostic([10,6,4], 4)}')
    #print(f'Binary Search Order Agnostic: {binary_search_order_agnostic([50,40,30,20,10], 25)}')

    #print(f'Binary Search Index Position: {binary_search_idx_position([1,3,5,6], 5)}')
    #print(f'Binary Search Index Position: {binary_search_idx_position([1,3,5,6], 2)}')
    #print(f'Binary Search Index Position: {binary_search_idx_position([1,3,5,6], 7)}')
    #print(f'Binary Search Index Position: {binary_search_idx_position([1,3,5,6], 0)}')
    #print(f'Binary Search Index Position: {binary_search_idx_position([1,3,5,6], 4)}')
    
    #print(f'Binary Search Index Floor: {binary_search_idx_floor([1,3,5,6], 5)}')
    #print(f'Binary Search Index Floor: {binary_search_idx_floor([1,3,5,6], 2)}')
    #print(f'Binary Search Index Floor: {binary_search_idx_floor([1,3,5,6], 7)}')
    #print(f'Binary Search Index Floor: {binary_search_idx_floor([1,3,5,6], 0)}')
    #print(f'Binary Search Index Floor: {binary_search_idx_floor([1,3,5,6], 4)}')
    #print(f'Binary Search Index Floor: {binary_search_idx_floor([1,1,1,1], 1)}')

    
    #print(f'First Occurrence of Target: {first_occurrence_target([1,2,2,2,3,4,5], 2)}')
    #print(f'First Occurrence of Target: {first_occurrence_target([1,1,1,1,1], 1)}')
    #print(f'First Occurrence of Target: {first_occurrence_target([1,2,4,4,4,4,4,6], 4)}')
    #print(f'First Occurrence of Target: {first_occurrence_target([5,7,7,8,8,10], 8)}')


    #print(f'Last Occurrence of Target: {last_occurrence_target([1,2,2,2,3,4,5], 2)}')
    #print(f'Last Occurrence of Target: {last_occurrence_target([1,1,1,1,1], 1)}')
    #print(f'Last Occurrence of Target: {last_occurrence_target([1,2,4,4,4,4,4,6], 4)}')
    #print(f'Last Occurrence of Target: {last_occurrence_target([5,7,7,8,8,10], 8)}')

    #print(f'Number of Occurrences: {number_of_occurrences([1,2,2,2,3,4,5], 2)}')
    #print(f'Number of Occurrences: {number_of_occurrences([1,1,1,1,1], 1)}')
    #print(f'Number of Occurrences: {number_of_occurrences([1,2,4,4,4,4,4,6], 4)}')
    #print(f'Number of Occurrences: {number_of_occurrences([5,7,7,8,8,10], 8)}')