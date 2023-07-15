const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let [n,k]=input[0].split(' ').map((item)=>Number(item));
let dp=Array(k+1).fill(0);
for(let i=1;i<=n;i++){
    let [w,v]=input[i].split(' ').map((item)=>Number(item));
    for(let j=k;j>=w;j--){
        dp[j]=Math.max(dp[j-w]+v,dp[j]);
    }
}
console.log(dp[k]);