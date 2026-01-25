def bestTimeToBuyAndSellStock(prices):
    """
    Best Time to Buy and Sell Stock.
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    """
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit

def findMajorityElement(nums):
    """
    Find the majority element in an array - Moore's Voting Algorithm. 
    The majority element is the element that appears more than n/2 times.
    There can be any number of diferent elements in the array.
    """
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return candidate

def findSmallestMissingPositive(nums):
    """
    Find the smallest missing positive integer.
    Given an unsorted integer array nums, return the smallest missing positive integer.
    You must implement an algorithm that runs in O(n) time and uses constant extra space.
    """
    n = len(nums)
    for i in range(n):
        if nums[i] <=0 or nums[i] > n:
            nums[i] = n+1
    for i in range(n):    
        if abs(nums[i]) < n+1:
            nums[abs(nums[i])-1] = abs(nums[abs(nums[i])-1]) * -1
    for i in range(n):
        if nums[i] > 0:
            return i + 1        
    return n + 1

def findSmallestMissingPositive_swap(nums):
    n = len(nums)
    i = 0
    while i < n:
        x = nums[i]
        # place x at index x-1 if it's in range and not already in the right place
        if 1 <= x <= n and nums[x - 1] != x:
            nums[i], nums[x - 1] = nums[x - 1], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1

def dutchNationalFlag(arr):
    """
    Dutch National Flag Problem.
    Given an array with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
    We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
    """
    low = 0
    mid = 0
    high = len(arr) - 1

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


if __name__ == "__main__":
    print(" Week 2 Day 2 ")

    #print(f'Best Profit: {bestTimeToBuyAndSellStock([7,1,5,3,6,4])}')  
    
    #print(f'Majority Element: {findMajorityElement([2,2,1,1,1,2,1])}')  
    
    #print(f'Smallest Missing Positive: {findSmallestMissingPositive([3,4,-1,1])}')  
    #print(f'Smallest Missing Positive: {findSmallestMissingPositive([7,8,9,11,12])}')
    #print(f'Smallest Missing Positive: {findSmallestMissingPositive([1,2,0])}')
    print(f'Smallest Missing Positive: {findSmallestMissingPositive([3,4,-1,1])}')

    #print(f'Smallest Missing Positive - Swap : {findSmallestMissingPositive_swap([3,4,-1,1])}')  
    #print(f'Smallest Missing Positive - Swap : {findSmallestMissingPositive_swap([7,8,9,11,12])}')
    #print(f'Smallest Missing Positive - Swap : {findSmallestMissingPositive_swap([1,2,0])}')
    #print(f'Smallest Missing Positive - Swap : {findSmallestMissingPositive_swap([1,1])}')

    #print(f'Dutch National Flag: {dutchNationalFlag([2,0,2,1,1,0])}')
    #print(f'Dutch National Flag: {dutchNationalFlag([2,0,1])}')
    
    