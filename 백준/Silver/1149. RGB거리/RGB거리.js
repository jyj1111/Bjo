const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const n = +input[0];
let arr = Array.from({ length: 3 }, () => Array(n + 1).fill(0));
for (let i = 1; i <= n; i++) {
  for (let j = 0; j < 3; j++) {
    arr[j][i] = input[i].split(" ").map((item) => Number(item))[j];
  }
}
console.log(solution(n, arr));
function solution(n, array) {
  let dp = Array.from({ length: 3 }, () => Array(n + 1).fill(0));
  dp[0][1]=array[0][1];
  dp[1][1]=array[1][1];
  dp[2][1]=array[2][1];
  for(let i=2;i<=n;i++){
    dp[0][i]=Math.min(dp[1][i-1]+array[0][i],dp[2][i-1]+array[0][i]);
    dp[1][i]=Math.min(dp[0][i-1]+array[1][i],dp[2][i-1]+array[1][i]);
    dp[2][i]=Math.min(dp[0][i-1]+array[2][i],dp[1][i-1]+array[2][i]);
  }
  return Math.min(dp[0][n],dp[1][n],dp[2][n]);
}