const fs=require('fs');
const input=fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [n,m]=input[0].split(' ').map(Number);
let graph=Array.from({length:n+1},()=>new Array());
for(let i=1;i<=m;i++){
    const [u,v]=input[i].split(' ').map(Number);
    graph[u].push(v);
    graph[v].push(u);
};
let visited=Array(n+1).fill(0);
visited[1]=1;
let queue=[];
for(let neighbor of graph[1]){
    visited[neighbor]=1;
    queue.push([neighbor,1]);
}
let distance=Array.from({length:n},()=>new Array());
while(queue.length){
    let [connect, dis]=queue.shift();
    distance[dis].push(connect);
    for(let neighbor of graph[connect]){
        if(visited[neighbor]===0){
            visited[neighbor]=1;
            queue.push([neighbor,dis+1]);
            
        }
    }
}
let answer;
for(let j=n-1;j>0;j--){
    if(distance[j].length>0){
        distance[j].sort((a,b)=>a-b);
        answer=`${distance[j][0]} ${j} ${distance[j].length}`;
        break;
    }
}
console.log(answer);




