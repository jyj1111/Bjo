const fs=require('fs');
let input=fs.readFileSync('dev/stdin').toString().trim().split('\n');
const have=input[1].split(' ').map((item)=>Number(item));
const problem=input[3].split(' ').map((item)=>Number(item));
let solve=[];
have.sort((a,b)=>a-b);
for(let i=0;i<problem.length;i++){
    let lt=0;
    let rt=have.length-1;
    while(lt<=rt){
        let mid=parseInt((lt+rt)/2);
        if(have[mid]===problem[i]){
            solve.push(1);
            break;
        }else if(have[mid]<problem[i]){
            lt=mid+1;
        }else{
            rt=mid-1;
        }
    }
    if(solve.length===i) solve.push(0);
}
console.log(solve.join(' '));