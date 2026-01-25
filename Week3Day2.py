def sumofsubarrays(n,arr,size):
    total = 0
    current_sum = 0
    start_idx  = 0
    end_idx = 0
    while end_idx < n:
        current_sum += arr[end_idx]
        end_idx += 1
        if end_idx - start_idx == size:
            total += current_sum
            current_sum -= arr[start_idx]
            start_idx += 1        

    return total

def maxsumofsubarrays(n,arr,size):
    max_sum = 0
    current_sum = 0
    start_idx  = 0
    end_idx = 0
    while end_idx < n:
        current_sum += arr[end_idx]
        end_idx += 1
        if end_idx - start_idx == size:
            if current_sum > max_sum:
                max_sum = current_sum
            current_sum -= arr[start_idx]
            start_idx += 1        

    return max_sum

def maxnumofvowelsinsubstring(arr, k):
    vowels = set('aeiouAEIOU')
    max_count = 0
    current_count = 0
    start_idx = 0
    end_idx = 0
    while end_idx < len(arr):
        if arr[end_idx] in vowels:
            current_count += 1
        end_idx += 1
        if end_idx - start_idx == k:
            if current_count > max_count:
                max_count = current_count
            if arr[start_idx] in vowels:
                current_count -= 1
            start_idx += 1

    return max_count

def lengthoflongestsubarray(arr, k):
    """
    Length of longest subarray with sum at max k. 
    """
    max_length = 0
    current_sum = 0
    start_idx = 0
    end_idx = 0
    while end_idx < len(arr):
        current_sum += arr[end_idx]
        end_idx += 1
        while current_sum > k:
            current_sum -= arr[start_idx]
            start_idx += 1
        if end_idx - start_idx > max_length:
            max_length = end_idx - start_idx

    return max_length

def minsizesubarray(arr, target):
    """
    Minimum size subarray sum >= target
    """
    min_length = 0
    current_sum = 0
    start_idx = 0
    end_idx = 0
    while end_idx < len(arr):
        current_sum += arr[end_idx]
        end_idx += 1
        while current_sum >= target:
            if min_length == 0 or end_idx - start_idx < min_length:
                min_length = end_idx - start_idx
            current_sum -= arr[start_idx]
            start_idx += 1

    return min_length

def maxconsecutiveoneswithflips(arr,k):
    """
    Given a binary array, find the maximum number of consecutive 1s in this array. K flips are allowed.
    """
    max_count = 0
    start_idx = 0
    end_idx = 0
    current_count = 0 
    zero_count = 0

    while end_idx < len(arr):
        if arr[end_idx] == 1:
            current_count += 1
        else:
            zero_count += 1
            while zero_count > k:
                if arr[start_idx] == 0:
                    zero_count -= 1
                else:
                    current_count -= 1
                start_idx += 1
        end_idx += 1
        if current_count + zero_count > max_count:
            max_count = current_count + zero_count


    return max_count

if __name__ == "__main__":
    print(" Week 3 Day 2 ")

    #print(f'Sum of Subarrays: {sumofsubarrays(5, [1,2,3,4,5], 3)}')
    #print(f'Sum of Subarrays: {sumofsubarrays(8, [2,1,5,1,3,2,4,1], 4)}')
    #print(f'Sum of Subarrays: {sumofsubarrays(6, [1,3,2,5,1,1], 2)}')

    #print(f'Max Sum of Subarrays: {maxsumofsubarrays(5, [1,2,3,4,5], 3)}')
    #print(f'Max Sum of Subarrays: {maxsumofsubarrays(5, [1,9,2,7,5], 3)}')
    #print(f'Max Sum of Subarrays: {maxsumofsubarrays(5, [1,0,3,4,6], 3)}')

    #print(f'Max Num of Vowels in Substring: {maxnumofvowelsinsubstring("abciiidef", 3)}')
    #print(f'Max Num of Vowels in Substring: {maxnumofvowelsinsubstring("aeiou", 2)}')
    #print(f'Max Num of Vowels in Substring: {maxnumofvowelsinsubstring("leetcode", 3)}')

    #print(f'Length of Longest Subarray: {lengthoflongestsubarray([1,2,3,4,5], 7)}')
    #print(f'Length of Longest Subarray: {lengthoflongestsubarray([2,1,5,1,3,2], 7)}')
    #print(f'Length of Longest Subarray: {lengthoflongestsubarray([4,1,1,1,2,3], 5)}')

    #print(f'Min Size Subarray: {minsizesubarray([2,3,1,2,4,3], 7)}')
    #print(f'Min Size Subarray: {minsizesubarray([1,4,4], 4)}')
    #print(f'Min Size Subarray: {minsizesubarray([1,1,1,1,1,1,1,1], 11)}')
    #print(f'Min Size Subarray: {minsizesubarray([1,2,3,4,5], 15)}')

    print(f'Max Consecutive Ones with Flips: {maxconsecutiveoneswithflips([1,1,1,0,0,0,1,1,1,1,0], 2)}')
    print(f'Max Consecutive Ones with Flips: {maxconsecutiveoneswithflips([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)}')
    print(f'Max Consecutive Ones with Flips: {maxconsecutiveoneswithflips([1,0,1,0,1,0,1,0,1], 4)}')