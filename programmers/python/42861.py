def solution(n, costs):
    answer = 0
    costs = sorted(costs, key=lambda x: x[2])
    set_target = set([costs[0][0]])

    while len(set_target) < n:
        for i, val in enumerate(costs):
            if val[0] in set_target and val[1] in set_target:
                continue

            if val[0] in set_target or val[1] in set_target:
                set_target.update([val[0], val[1]])
                answer += val[2]
                costs[i] = [-1, -1, -1]
                break

    return answer