# SEND + MORE = MONEY---->

for S in range(1, 10):
    for E in range(10):
        for N in range(10):
            for D in range(10):
                for M in range(1, 10):
                    for O in range(10):
                        for R in range(10):
                            for Y in range(10):

                                digits = [S,E,N,D,M,O,R,Y]

                                if len(set(digits)) != 8:
                                    continue

                                SEND = 1000*S + 100*E + 10*N + D
                                MORE = 1000*M + 100*O + 10*R + E
                                MONEY = 10000*M + 1000*O + 100*N + 10*E + Y

                                if SEND + MORE == MONEY:
                                    print("SEND =", SEND)
                                    print("MORE =", MORE)
                                    print("MONEY =", MONEY)




# Best First Search---->

graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':[],
    'F':[]
}

h = {
    'A':5,
    'B':3,
    'C':2,
    'D':6,
    'E':1,
    'F':4
}

open = ['A']
visited = []

while open:
    open.sort(key=lambda x: h[x])
    node = open.pop(0)

    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        open += graph[node]
       



# Depth First Search---->

graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':[],
    'F':[]
}

visited = []

def dfs(node):
    print(node, end=" ")
    visited.append(node)

    for x in graph[node]:
        if x not in visited:
            dfs(x)

dfs('A')





# Breadth First Search---->

graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':[],
    'F':[]
}

queue = ['A']
visited = []

while queue:
    node = queue.pop(0)

    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        queue += graph[node]