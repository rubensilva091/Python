def bfs(adj, o):
    queue = [o]
    vis = {o}
    pai = {}
    while(queue):
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)
    return pai


def shortest_path(adj, o, d):
    pai = bfs(adj, o)
    caminho = [d]
    while d in pai:
        d = pai[d]
        caminho.insert(0, d)
    return caminho


def dijkstra(adj, o):
    pai = {}
    dist = {}
    dist[o] = 0
    orla = {o}
    while orla:
        v = min(orla, key=lambda x: dist[x])
        orla.remove(v)
        for d in adj[v]:
            if d not in dist:
                orla.add(d)
                dist[d] = float("inf")
            if dist[v] + adj[v][d] < dist[d]:
                pai[d] = v
                dist[d] = dist[v] + adj[v][d]
    return pai


def prim(adjsorted):
    pai = {}
    cost = {}
    o = sorted(adjsorted)[0]
    cost[o] = 0
    orla = {o}
    while orla:
        v = min(orla, key=lambda x: cost[x])
        orla.remove(v)
        for d in adjsorted[v]:
            if d not in cost:
                orla.add(d)
                cost[d] = float("inf")
            if adjsorted[v][d] < cost[d]:
                pai[d] = v
                cost[d] = adjsorted[v][d]
    return pai


def floyd_warshall(adj):
    dist = {}
    for o in adj:
        dist[o] = {}
        for d in adj:
            if o == d:
                dist[o][d] = 0
            elif d in adj[o]:
                dist[o][d] = adj[o][d]
            else:
                dist[o][d] = float("inf")
    for k in adj:
        for o in adj:
            for d in adj:
                if dist[o][k] + dist[k][d] < dist[o][d]:
                    dist[o][d] = dist[o][k] + dist[k][d]
    return dist
