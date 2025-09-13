# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    count = 1
    while(count < 1000000):
        if count not in A:
            return count
        count += 1
        
        
solution([1,2,3,4,5])
