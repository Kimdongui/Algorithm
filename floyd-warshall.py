#######################################################################
# 그래프가 주어졌을 때, 각 노드 간의 최단거리를 구하는 알고리즘, O(n^3)
# Key Idea : start - end의 cost와 start - mid - end 의 cost를 모두 비교한다
#######################################################################

def floyd_warshall(graph):
    # Graph's diagonal is 0, and edges have cost to visit whether it can or infinite
    N = len(graph)
    for mid in range(N):
        for st in range(N):
            for ed in range(N):
                if graph[st][mid] + graph[mid][ed] < graph[st][ed]:
                    graph[st][ed] = graph[st][mid] + graph[mid][ed]
    return graph
