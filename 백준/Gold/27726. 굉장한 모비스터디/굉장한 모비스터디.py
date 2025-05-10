import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            self.parent[y_root] = x_root


N = int(input())
M1, M2, M3 = map(int, input().split())

dsus = [DSU(N) for _ in range(3)]
M_values = [M1, M2, M3]

for i in range(3):
    for _ in range(M_values[i]):
        a, b = map(int, input().split())
        dsus[i].union(a, b)

group_map = dict()
for person in range(1, N + 1):
    triple = (dsus[0].find(person),dsus[1].find(person),dsus[2].find(person))

    if triple not in group_map:
        group_map[triple] = []
    group_map[triple].append(person)

amazing_studies = [sorted(group) for group in group_map.values() if len(group) >= 2]
amazing_studies.sort(key=lambda x: x[0])  

print(len(amazing_studies))
for group in amazing_studies:
    print(*group)