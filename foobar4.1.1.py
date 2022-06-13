def pair(i, pairing, seen, graph, num_trainers):
        for j in range(num_trainers):
            if graph[i][j] and seen[j] == False:
                seen[j] = True
                if pairing[j] == -1 or pair(pairing[j], pairing, seen):
                    pairing[j] = i
                    return True
        return False
def solution(banana_list):
    num_trainers = len(banana_list)
    graph = [[None] * num_trainers for i in range(num_trainers)]
    for i in range(num_trainers):
        for j in range(i, num_trainers):
            graph[i][j] = converge(banana_list[i], banana_list[j])
            graph[j][i] = graph[i][j]
    pairing = [-1] * num_trainers
    result = 0
    for i in range(num_trainers):
        seen = [False] * num_trainers
        if pair(i, pairing, seen, graph, num_trainers):
            result += 1
    return num_trainers - 2 * (result // 2)
def converge(x, y):
    return ((x%4) + (y%4))%4 != 0

def solution(banana_list):
    # Recursive matching algorithm
    def matching(u, match, seen):
        for v in range(n):

            if graph[u][v] and seen[v] == False:
                seen[v] = True

                if match[v] == -1 or matching(match[v], match, seen):
                    match[v] = u
                    return True
        return False

    # Get the length of the list and make a graph
    n = len(banana_list)
    graph = [[None] * n for _ in range(n)]

    for i in range(n):
        for j in range(i, n):
            graph[i][j] = check_finite(banana_list[i], banana_list[j])
            graph[j][i] = graph[i][j]

    match = [-1] * n

    result = 0
    for i in range(n):
        seen = [False] * n
        if matching(i, match, seen):
            result += 1

    return n - 2 * (result // 2)


def check_finite(x, y):
    z = (x + y) / gcd(x, y)
    return (z & (z - 1)) != 0