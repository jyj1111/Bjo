const fs=require('fs');
const input=fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const[N,M]=input[0].split(' ').map(Number);
let graph=Array.from({length:N+1},()=>new Array());
for(let i=1;i<=M;i++){
    const[u,v]=input[i].split(' ').map(Number);
    graph[u].push(v);
    graph[v].push(u);
}
let visited=Array(N+1).fill(0);
let queue=[];
let cnt=0;
for(let i=1;i<graph.length;i++){
    if(visited[i]===0){
        visited[i]=1;
        cnt++;
        queue.push(i);
         while(queue.length){
            const vertex=queue.shift();
            for(let connect of graph[vertex]){
                if(visited[connect]===0){
                    visited[connect]=1;
                    queue.push(connect);
                }
            }
            
        }
    }
}

console.log(cnt);


