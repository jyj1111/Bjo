const fs=require('fs');
const input=fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const[n,m]=input[0].split(' ').map(Number);
let graph=Array.from({length:n+1},()=>new Array());
for(let i=1;i<=m;i++){
    const[u,v]=input[i].split(' ').map(Number);
    graph[u].push(v);
    graph[v].push(u);
}
let min=Number.MAX_SAFE_INTEGER;
let kevinBakenArr=[min];
for(let i=1;i<=n;i++){
    let kevinBaken=0;
    let visited=Array(n+1).fill(0);
    let queue=[];
    visited[i]=1;
    queue.push([i,0]);
    while(queue.length){
        let [connect,dis]=queue.shift();
        kevinBaken+=dis;
        for(let neighbor of graph[connect]){
            if(visited[neighbor]===0){
                visited[neighbor]=1;
                queue.push([neighbor,dis+1]);
            }
        }
    }
    kevinBakenArr.push(kevinBaken);
    min=Math.min(min,kevinBaken);
   
}
console.log(kevinBakenArr.indexOf(min));
