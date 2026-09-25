#7. Earliest Connectivity
#There are n initially disconnected computers. Connections are added one by one:

#(u,v,time)

#Find the earliest time at which every computer belongs to a single connected component.

n = 5

connections = [
    (0, 1, 10),
    (2, 3, 20),
    (1, 2, 30),
    (3, 4, 40)
]

parent = list(range(n))
components = n


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]


def union(a, b):

    global components

    rootA = find(a)
    rootB = find(b)

    if rootA != rootB:
        parent[rootB] = rootA
        components -= 1
        return True

    return False


for u, v, time in connections:

    if union(u, v):

        if components == 1:
            print("Earliest time:", time)
            break