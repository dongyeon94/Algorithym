
def solution(a):
    answer = 0
    for ind, val in enumerate(a):
        if ind == 0 or ind == len(a) - 1:
            answer += 1
        else:
            leftmin = min(a[:ind])
            rightmin = min(a[ind + 1:])

            if (max(leftmin, rightmin) > val):
                answer += 1
    return answer