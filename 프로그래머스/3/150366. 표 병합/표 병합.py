
def solution(commands):
    answer = []
    indexInfo=[[(i,j) for j in range(51)] for i in range(51)]
    graph=[['EMPTY']*(51) for i in range(51)]
    for command in commands:
        commandSplit=command.split(' ')
        if len(commandSplit)==3:
            str,a,b=commandSplit
            if str=='UPDATE':
                for r in range(51):
                    for c in range(51):
                        if graph[r][c]==a:
                            graph[r][c]=b

            elif str=="UNMERGE":
                a,b=int(a),int(b)
                x,y=indexInfo[a][b]
                tmp = graph[x][y]
                for r in range(51):
                    for c in range(51):
                        if indexInfo[r][c] == (x,y):
                            indexInfo[r][c] = (r,c)
                            graph[r][c] = "EMPTY"
                graph[a][b] = tmp

            elif str=="PRINT":
                a,b=int(a),int(b)
                x,y=indexInfo[a][b] 
                answer.append(graph[x][y])
        elif len(commandSplit)==4:
            str,r,c,val=commandSplit
            r,c=int(r),int(c)
            x,y=indexInfo[r][c] 
            graph[x][y]=val
        elif len(commandSplit)==5:
            str,r1,c1,r2,c2=commandSplit
            r1,c1,r2,c2=int(r1),int(c1),int(r2),int(c2)
            x1,y1 = indexInfo[r1][c1]
            x2,y2 = indexInfo[r2][c2]
            if graph[x1][y1] == "EMPTY":
                graph[x1][y1] = graph[x2][y2]
            for i in range(51):
                for j in range(51):
                    if indexInfo[i][j] == (x2,y2):
                        indexInfo[i][j] = (x1,y1)

    return answer
