const fs=require("fs");
let input=fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let arr=input[1].split(' ').map((item)=>Number(item));
arr.sort((a,b)=>a-b);
let answer=[0,0];
let distance=2000000000;
let lt=0;
let rt=arr.length-1;
while(lt<rt){
     
     if(Math.abs(arr[lt]+arr[rt])<distance){
         distance=Math.abs(arr[lt]+arr[rt]);
         answer=[arr[lt],arr[rt]];
     }
     if(arr[lt]+arr[rt]<0){
         lt++;
     }else if(arr[lt]+arr[rt]>0){
         rt--;
     }else{
         break;
     }       
        
}
console.log(answer.join(' '));
