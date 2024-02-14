class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

# 각 정점에 대한 이름을 포함하는 사전 생성
vertex_names = {
    0: '문별',
    1: '솔라',
    2: '휘인',
    3: '쯔위',
    4: '선미',
    5: '화사'
}

G1 = None
stack = []
visitedAry = []

G1 = Graph(6)
G1.graph[0][1] = 1; G1.graph[0][2] = 1
G1.graph[1][0] = 1; G1.graph[1][3] = 1
G1.graph[2][0] = 1; G1.graph[2][3] = 1
G1.graph[3][1] = 1; G1.graph[3][2] = 1; G1.graph[3][4] = 1; G1.graph[3][5] = 1
G1.graph[4][3] = 1; G1.graph[4][5] = 1
G1.graph[5][3] = 1; G1.graph[5][4] = 1;

print('## G1 무방향 그래프 ##')
for row in range(6):
    for col in range(6):
        print(G1.graph[row][col], end = ' ')
    print()

current = 0
stack.append(current)
visitedAry.append(current)

while(len(stack) != 0):
    next = None
    for vertex in range(6):
        if G1.graph[current][vertex] == 1:
            if vertex in visitedAry:
                pass
            else:
                next = vertex
                break
    if next != None:
        current = next
        stack.append(current)
        visitedAry.append(current)
    else:
        current = stack.pop()

print('방문 순서:', end = ' ')
for i in visitedAry:
    print(vertex_names[i], end = ' ')  # 각 정점에 대한 이름을 출력
