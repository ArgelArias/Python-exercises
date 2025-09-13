def solution(X, Y):
    my_arr = []
    result = 0

    for i in range(len(X)):
        my_arr.append(X[i] / Y[i])

    for i in range(len(my_arr)):
        for j in range(i + 1, len(my_arr)):
            if my_arr[i] + my_arr[j] == 1:
                result += 1

    return int(result)

print(solution([1,1,2],[3,2,3]))
print(solution([1,1,1],[2,2,2]))
print(solution([1,2,3,1,2,12,8,4],[5,10,15,2,4,15,10,5]))
