def sort_an_array(n, arr):
    # Sort the array containing only 0s, 1s, and 2s in-place
    low = 0
    mid = 0
    high = n - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

def move_func(n, arr):
    zero_index = 0
    for i in range(n):
        #print(f'Current Array: {arr}, Zero Index: {zero_index}, Current Index: {i}')
        if arr[i] != 0:
            arr[zero_index], arr[i] = arr[i], arr[zero_index]
            zero_index += 1

    return arr    # Move all zeros to the end of the array while maintaining the order of non-zero elements

def find_missing(arr):
    """
    Find the missing and repeating numbers in the array.
    The array contains numbers from 1 to n with one number missing and one number repeating.    
    """
    n = len(arr)
    A = 0
    B = 0
    counts = [0] * n
    for i in range(n):
        counts[arr[i]-1] += 1
    for i in range(n):
        if counts[i] == 0:
            B = i + 1
        elif counts[i] > 1:
            A = i + 1    
    return (A, B)  # Find the missing and repeating numbers in the array

def first_missing_positive(n, arr):
    for i in range(n):
        if arr[i] <= 0:
            arr[i] = 0
    for i in range(n):
        print(f'Iteration {i}: {arr}')
        print(f'Processing number: {arr[i]} and {arr[arr[i]-1]}')
        if arr[i] > 0 and arr[i] <= n:
            if arr[i] < arr[arr[i] - 1]:
                arr[arr[i] - 1], arr[i] = arr[i], 0
            else:
                print(f'Else: {arr[arr[i] - 1]}')
                print(f'Before Swap: {arr}')
                x = arr[arr[i] - 1] 
                arr[arr[i] - 1] = arr[i]
                arr[i] = x
                print(f'After Swap: {arr}')
        print(f'Iteration {i}: {arr}')
    return arr

def majorityElement(n, arr):
    """
    Find the majority element in an array - Moore's Voting Algorithm. 
    The majority element is the element that appears more than n/2 times.
    There can be any number of diferent elements in the array.
    """
    count = 0
    candidate = None

    for num in arr:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return candidate

def maxProfit(nums, n):
    """
    Best Time to Buy and Sell Stock.
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    """
    purchase_price = nums[0]
    curr_high_price = nums[0]
    max_profit = 0
    
    for i in range(1, n):
        #print(f'Day {i}: Price={nums[i]}, Purchase Price={purchase_price}, Current High Price={curr_high_price}, Max Profit={max_profit}')
        if nums[i] < curr_high_price:
            max_profit += curr_high_price - purchase_price
            purchase_price = curr_high_price = nums[i]
        else:
            curr_high_price = nums[i]   
        #print(f'After Day {i}: Purchase Price={purchase_price}, Current High Price={curr_high_price}, Max Profit={max_profit}')
    max_profit += curr_high_price - purchase_price   

    return max_profit

def first_missing_positive(n, arr):
    """
    Find the smallest missing positive integer.
    Given an unsorted integer array nums, return the smallest missing positive integer.
    You must implement an algorithm that runs in O(n) time and uses constant extra space.
    """
    for i in range(n):
        if arr[i] <=0 or arr[i] > n:
            arr[i] = n+1
    for i in range(n):    
        if abs(arr[i]) < n+1:
            arr[abs(arr[i])-1] = abs(arr[abs(arr[i])-1]) * -1
    for i in range(n):
        if arr[i] > 0:
            return i + 1        
    return n + 1

def max_consecutive(arr):
    # Write your code here
    max_count = 0
    current_count = 0
    for num in arr:
        if num == 1:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
            current_count = 0
    if current_count > max_count:
                max_count = current_count        
    return max_count

def rain_water(hei):
    # Write your code here
    lmax = [0] * len(hei)
    rmax = [0] * len(hei)
    lmax[0] = hei[0]
    n = len(hei)
    total_water = 0
    for idx in range(1, n):
        #print(f'Idx: {idx}, Height: {hei[idx]}, LMax before: {lmax[idx]}')
        if hei[idx] >= lmax[idx - 1]:
            lmax[idx] = hei[idx]
        else:
            lmax[idx] = lmax[idx-1]
        #print(f'Idx: {idx}, Height: {hei[idx]}, LMax: {lmax[idx]}')    
    idx = n - 2
    rmax[-1] = hei[-1]
    while idx >= 0:
        if hei[idx] >= rmax[idx+1]:
            rmax[idx] = hei[idx]
        else:
            rmax[idx] = rmax[idx+1]
        idx -= 1

    for i in range(n):
        total_water += min(lmax[i], rmax[i]) - hei[i]
    
   
    return total_water

def remove_dupli(arr):
    # Write your code here
    curr_val = arr[0]
    mov_idx = 1
    delete_marker = arr[0] - 1
    count = 1
    while mov_idx < len(arr):
        if arr[mov_idx] == curr_val:
            arr[mov_idx] = delete_marker
        else:    
            curr_val = arr[mov_idx]
            count += 1
        mov_idx += 1

    
    return count


def twoSum(target, n, arr):
    # Write your code here
    left_idx = 0
    right_idx = n - 1

    while left_idx < right_idx:
        if arr[left_idx] + arr[right_idx] == target:
            return (left_idx + 1, right_idx + 1)
        elif arr[left_idx] + arr[right_idx] < target:
            left_idx += 1
        else:
            right_idx -= 1
    return (-1, -1)


def left_right(arr):
    n = len(arr)
    if n < 3:  
        return -1

    prefix_max = [0] * n
    prefix_max[0] = arr[0]
    for i in range(1, n):
        prefix_max[i] = max(prefix_max[i-1], arr[i])

    suffix_min = [0] * n
    suffix_min[-1] = arr[-1]
    for i in range(n-2, -1, -1):
        suffix_min[i] = min(suffix_min[i+1], arr[i])

    # interior only: 1..n-2
    for i in range(1, n-1):
        if prefix_max[i-1] <= arr[i] <= suffix_min[i+1]:
            return arr[i]

    return -1

def findDistinctCount(n, arr):
    # Write your code here
    count = 0
    distinct_counts = [-1]*n

    for i in range(n):
        distinct_counts[abs(arr[i])] = 1
    
    for i in range(n):
        if distinct_counts[i] == 1:
            count += 1
    return count        

if __name__ == "__main__":
    print(" Challenges ")
    print(f'Sort Array 012: {sort_an_array(7, [0,2,1,2,0,1,0])}')
    print(f'Move Zeros: {move_func(8, [0,1,0,3,12,0,5,0])}')
    print(f'Find Missing and Repeating: {find_missing([3,1,3,4,2])}')
    print(f'First Missing Positive: {first_missing_positive(5, [3,4,-1,1,2])}')
    print(f'Majority Element: {majorityElement(7, [2,2,1,1,1,2,1])}')
    print(f'Best Time to Buy and Sell Stock: {maxProfit([7,1,5,3,6,4], 6)}')
    print(f'Max Consecutive 1s: {max_consecutive([1,1,0,1,1,1])}')
    print(f'Rain Water Trapped: {rain_water([0,1,0,2,1,0,1,3,2,1,2,1])}')
    print(f'Remove Duplicates: {remove_dupli([0,0,1,1,1,2,2,3,3,4])}')
    print(f'Two Sum: {twoSum(9, 9, [1,2,3,4,6,7,8,9,10])}')
    print(f'Left Right Element: {left_right([5,1,4,3,6,8,10,7,9])}')
    print(f'Distinct Count: {findDistinctCount(7, [1,2,2,3,4,4,5])}')