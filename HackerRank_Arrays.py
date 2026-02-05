import numpy as np


def reverseArray(a):
    # Write your code here
    n = len(a)
    start_idx = 0
    end_idx = n -1
    while start_idx < end_idx:
        a[start_idx], a[end_idx] = a[end_idx], a[start_idx]
        start_idx = start_idx + 1
        end_idx = end_idx - 1
    
    return a

def hourglassSum(arr):
    sums = []
    for row in range(0,4):
       for col in range(0,4):
          sum = 0
          sum = arr[row][col] + arr[row][col + 1] + arr[row][col + 2]
          sum = sum + arr[row+1][col+1] 
          sum = sum + arr[row + 2][col] + arr[row+2][col+1] + arr[row+2][col+2]
          sums.append(sum)
    return max(sums)


def dynamicArray(n, queries):
    # Write your code here
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    answers = []
    for query in queries:
        qType = query[0]
        x = query [1]
        y = query [2]
        idx = (x ^ lastAnswer) % n
        if qType == 1:
            arr[idx].append(y)
        else:
            lastAnswer = arr[idx][y%len(arr[idx])] 
            answers.append(lastAnswer)
    
    return answers

def rotateLeft(d, arr):
    # Write your code here
    n = len(arr)
    out = [0] * n
    d = d%n
    for i in range(0, n):
       out[(i-d)%n] = arr[i]
    return out

def matchingStrings(stringList, queries):
    # Write your code here
    counts = [0] * len(queries)
    for str in stringList:
        for idx, query in enumerate(queries):
            if query == str:
                counts[idx] += 1
        
    return counts

def arrayManipulationV1(n, queries):
    # Write your code here
    ans = [0] * n
    for query in queries:
        a,b,k = query[0], query[1], query[2]
        for idx in range (a-1, b):
            ans[idx] += k

    return max(ans)

def arrayManipulation(n, queries):
    # Write your code here
    diff = [0] * n
    for idx, query in enumerate(queries):
        a,b,k = query[0], query[1], query[2]
        diff[a-1] += k
        if b < n: diff[b] -= k 
    maxval = diff[0]
    runsum = diff[0]
    for idx in range(1,n):
        runsum += diff[idx]
        if runsum > maxval:
            maxval = runsum
    return maxval


if __name__ == "__main__":

    print("Open Challenges")
    arr = [[1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],]
    #print(f' Hour Glass sum ->  {hourglassSum(arr)}')

    #print(f'Dynamic Array - > {dynamicArray(2,[[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]])}')

    #print(f'Left Rotate Array - > {rotateLeft(4,[1,2,3,4,5])}')

    #print(f'String search - > {matchingStrings(['ab','ab','abc'],['ab','abc','bc'])}')
    #print(f'String search - > {matchingStrings(['aba','baba','aba','xzxb'],['aba','xzxb','ab'])}')
    #print(f'String search - > {matchingStrings(['def','de','fgh'],['de','lmn','fgh'])}')
    #print(f'String search - > {matchingStrings(["abcde", "sdaklfj", "asdjf", "na", "basdn", "sdaklfj", "asdjf", "na", "asdjf", "na", "basdn", "sdaklfj", "asdjf"], ["abcde", "sdaklfj", "asdjf", "na", "basdn"])}')

    print(f'String search - > {arrayManipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]])}')

