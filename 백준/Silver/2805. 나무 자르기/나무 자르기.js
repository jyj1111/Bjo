const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n,m]=input[0].split(' ').map((item)=>Number(item));
let have=input[1].split(' ').map((item)=>Number(item));
let answer;
let lt=0;
let rt=Math.max(...have);
while(lt<=rt){
    let mid=parseInt((lt+rt)/2);
    let tree=0;
    for(let i=0;i<n;i++){
        have[i]>mid?tree+=(have[i]-mid): tree+=0;
    }
    if(tree>=m){
        answer=mid;
        lt=mid+1;
    }else{
        rt=mid-1;
    }
}
console.log(answer);