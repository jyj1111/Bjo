const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const[N,M]=input[0].split(' ').map(Number);
let graph = Array.from({ length: N + 1 }, () =>
  Array.from({ length: 2 }, () => new Set())
);
for(let i=1;i<=M;i++){
    const[big,small]=input[i].split(' ').map(Number);
    graph[big][1].add(small);
    graph[small][0].add(big);
}
let answer=0;
for(let i=1;i<=N;i++){
    let smallQueue=[];
    let largeQueue=[];
    let visited=Array(N+1).fill(0);
    visited[i]=1;
    smallQueue.push(...graph[i][0]);
    while(smallQueue.length){
        let small=smallQueue.shift();
        visited[small]=1;
        for(let neighbor of graph[small][0]){
            if(visited[neighbor]===0){
                graph[i][0].add(neighbor);
                smallQueue.push(neighbor);
            }
        }
    }
    largeQueue.push(...graph[i][1]);
    while(largeQueue.length){
        let large=largeQueue.shift();
        visited[large]=1;
        for(let neighbor of graph[large][1]){
            if(visited[neighbor]===0){
                graph[i][1].add(neighbor);
                largeQueue.push(neighbor);
            }
        }
    }
    let mid=(N-1)/2;
    if(graph[i][0].size>mid || graph[i][1].size>mid ){
        answer++;
    }
   
}
console.log(answer);
