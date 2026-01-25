def pairwithsum(arr, target_sum): 
    """
    Given an array of sorted integers arr and an integer target_sum, 
    return indices of the two numbers such that they add up to target_sum.
    You may assume that each input would have exactly one solution, 
    and you may not use the same element twice.
    You can return the answer in any order.
    """
    start = 0
    end = len(arr) - 1
    while start < end:
        current_sum = arr[start] + arr[end]
        if current_sum == target_sum:
            return (start, end)
        elif current_sum < target_sum:
            start += 1
        else:
            end -= 1
    return (start, end)

def removeduplicatesfromsortedarray(arr):
    """
    Given a sorted array nums, remove the duplicates in-place such that each 
    element appears only once and returns the new length.
    Do not allocate extra space for another array, you must do this by 
    modifying the input array in-place with O(1) extra memory.
    """
    if not arr:
        return 0

    write_index = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[write_index] = arr[i]
            write_index += 1

    return write_index

def squareofsortedarray(arr):
    """
    Given an integer array nums sorted in non-decreasing order, 
    return an array of the squares of each number sorted in non-decreasing order.
    """
    result = [0] * len(arr)
    position = len(arr) - 1
    left = 0
    right = len(arr) - 1
    while position >= 0:
        if abs(arr[left]) > abs(arr[right]):
            result[position] = arr[left] * arr[left]
            left += 1
        else:
            result[position] = arr[right] * arr[right]
            right -= 1
        position -= 1

    return result

def containerwithmostwater(height):
    """
    You are given an integer array height of length n. 
    There are n vertical lines drawn such that the two endpoints of the ith line 
    are (i, 0) and (i, height[i]).
    Find two lines that together with the x-axis form a container, 
    such that the container contains the most water.
    Return the maximum amount of water a container can store.
    Notice that you may not slant the container.
    """
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        current_area = min(height[left], height[right]) * (right - left)
        if current_area > max_area:
            max_area = current_area
        if height[left] < height[right]:   
            left += 1
        else:
            right -= 1
    
    return max_area
    
def finduniquethreesum(nums):
    """
    Given an integer array nums, return all the triplets 
    [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
    and nums[i] + nums[j] + nums[k] == 0.
    Notice that the solution set must not contain duplicate triplets.
    """
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return result

def trappingrainwater(heights):
    """
    Given n non-negative integers representing an elevation map 
    where the width of each bar is 1, compute how much water it can trap after raining.
    """
    left, right = 0, len(heights) - 1
    left_max, right_max = 0, 0
    water_trapped = 0

    while left < right:
        #print(f'Left: {left}, Right: {right}, Left Max: {left_max}, Right Max: {right_max}, Water Trapped: {water_trapped}')
        if heights[left] < heights[right]:
            if heights[left] >= left_max:
                left_max = heights[left]
            else:
                water_trapped += left_max - heights[left]
            left += 1
        else:
            if heights[right] >= right_max:
                right_max = heights[right]
            else:
                water_trapped += right_max - heights[right]
            right -= 1

    return water_trapped

def trappingrainwater_bruteforce(heights):
    """
    Brute Force approach to trapping rain water problem.
    Given n non-negative integers representing an elevation map 
    where the width of each bar is 1, compute how much water it can trap after raining.
    """
    n = len(heights)
    water_trapped = 0

    for i in range(n):
        left_max = max(heights[:i+1]) if i > 0 else heights[i]
        right_max = max(heights[i:]) if i < n - 1 else heights[i]
        water_trapped += min(left_max, right_max) - heights[i]

    return water_trapped

if __name__ == "__main__":
    print(" Week 3 Day 1 ")
    #print(f'Pair with Sum: {pairwithsum([1,2,3,4,6], 6)}')
    
    #print(f'Remove Duplicates: {removeduplicatesfromsortedarray([0,0,1,1,1,2,2,3,3,4])}')
    #print(f'Remove Duplicates: {removeduplicatesfromsortedarray([2,3,3,3,6,9,9])}')

    #print(f'Squares of Sorted Array: {squareofsortedarray([-4,-1,0,3,10])}')
    #print(f'Squares of Sorted Array: {squareofsortedarray([-2,-1,0,2,3])}')
    #print(f'Squares of Sorted Array: {squareofsortedarray([-3,-1,0,1,2])}')

    #print(f'Container with Most Water: {containerwithmostwater([1,8,6,2,5,4,8,3,7])}')
    #print(f'Container with Most Water: {containerwithmostwater([1,1])}')

    #print(f'Find Unique Three Sum: {finduniquethreesum([-1,0,1,2,-1,-4])}')

    print(f'Trapping Rain Water: {trappingrainwater([0,1,0,2,1,0,1,3,2,1,2,1])}')
    #print(f'Trapping Rain Water: {trappingrainwater([4,2,0,3,2,5])}')