const fs=require("fs");
let input=fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let arr=input[1].split(' ').map((item)=>Number(item));
let n=+input[0];
arr.sort((a,b)=>a-b);
let answer=[0,0,0];
let distance=3000000000;
for(let i=0;i<n-2;i++){
    let lt=i+1;
    let rt=n-1;
    while(lt<rt){
        let sum=arr[i]+arr[lt]+arr[rt];
        if(Math.abs(sum)<distance){
            distance=Math.abs(sum);
            answer=[arr[i],arr[lt],arr[rt]];
        }
        if(sum<0){
            lt++;
        }else if(sum>0){
            rt--;
        }else{
            break;
        }       
        
}
}


console.log(answer.join(' '));