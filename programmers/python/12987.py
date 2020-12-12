def solution(A, B):
    answer = 0
    A = sorted(A)
    B = sorted(B)

    for i in A:
        for i2 in range(len(B)):
            if i < B[i2]:
                answer += 1
                B.pop(i2)
                break

    return answer