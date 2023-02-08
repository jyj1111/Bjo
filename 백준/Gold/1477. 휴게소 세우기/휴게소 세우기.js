const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let [N,M,L]=input[0].split(' ').map((item)=>Number(item));
let reststop;
if(N===0){
    reststop=[];
}else{
    reststop=input[1].split(' ').map((item)=>Number(item));    
}
reststop.unshift(0);
reststop.push(L);
reststop.sort((a,b)=>a-b);
let lt=1;
let rt=L-1;
let ans=0;
while(lt<=rt){
    let mid=parseInt((lt+rt)/2);
    let cnt=0;
    for(let i=1;i<reststop.length;i++){
        cnt+=parseInt((reststop[i]-reststop[i-1]-1)/mid);      
    }
    if(cnt>M){
        lt=mid+1;
    }else{
        ans=mid;
        rt=mid-1;
    }
}
console.log(ans);
