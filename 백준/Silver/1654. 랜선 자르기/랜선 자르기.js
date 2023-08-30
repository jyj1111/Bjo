const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [k,n]=input[0].split(' ').map((item)=>Number(item));
let have=[];
for(let i=1;i<=k;i++){
    have.push(+input[i]);
}
let answer;
let lt=1;
let rt=Math.max(...have);
while(lt<=rt){
    let mid=parseInt((lt+rt)/2);
    let count=0;
    for(let i=0;i<k;i++){
        count+=parseInt(have[i]/mid);
    }
    if(count>=n){
        answer=mid;
        lt=mid+1;
    }else{
        rt=mid-1;
    }
}
console.log(answer);