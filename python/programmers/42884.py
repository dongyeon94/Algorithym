def solution(routes):
    answer = 1

    routes = sorted(routes, key=lambda x: x[0])

    length = routes[0][1]

    for i in range(len(routes) - 1):
        if length > routes[i][1]:
            length = routes[i][1]

        if length < routes[i + 1][0]:
            length = routes[i + 1][1]
            answer += 1

    return answer