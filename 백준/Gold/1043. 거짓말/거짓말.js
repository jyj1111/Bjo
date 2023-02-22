const fs=require('fs');
const input=fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const[N,M]=input[0].split(' ').map(Number);
const [True,...TrueMembers]=input[1].split(' ').map(Number);
let answer=M;

let graph=Array.from({length:N+1},()=>new Set());
for(let i=2;i<2+M;i++){
    const[num,...arr]=input[i].split(' ').map(Number);
    for(let j=0;j<num-1;j++){
        for(let k=j+1;k<num;k++){
            graph[arr[j]].add(arr[k]);
            graph[arr[k]].add(arr[j]);
        }
    }
}
let visited=Array(N+1).fill(0);
let queue=[];
for(let TrueMember of TrueMembers){
    visited[TrueMember]=1;
    queue.push(TrueMember);
}

while(queue.length){
    let Truemember=queue.shift();
    for(let neighbor of graph[Truemember]){
        if(visited[neighbor]===0){
            visited[neighbor]=1;
            queue.push(neighbor);
            TrueMembers.push(neighbor);
        }
    }
}

function hasIntersection(arr1,arr2){
    return arr1.filter((item)=>arr2.includes(item)).length>0?true:false;
};

for(let i=2;i<2+M;i++){
    const[num,...arr]=input[i].split(' ').map(Number);
    if(hasIntersection(arr,TrueMembers)){
        answer--;
    }
}
console.log(answer);









