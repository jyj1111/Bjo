const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let [n,m]=[+input[0],+input[1]];
let visited=Array(n+1).fill(0);
let graph = Array.from({ length: n + 1 }, () =>new Set());
for(let i=2;i<2+m;i++){
    let[u,v]=input[i].split(' ').map(Number);
    graph[u].add(v);
    graph[v].add(u);
}
visited[1]=1;
for(let neighbor of graph[1]){
    visited[neighbor]=1;
}
let copy1 = new Set([...graph[1]]);
for(let neighbor of copy1){
    for(let connection of graph[neighbor]){
        if(visited[connection]===0){
            visited[connection]=1;
            graph[1].add(connection);
        }
    }
}
console.log(graph[1].size);


