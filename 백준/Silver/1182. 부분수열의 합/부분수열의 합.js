const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

function sol(n, hap, arr) {
  let answer = 0;
  let arr1 = [];
  function DFS(idx, sum) {
    if (idx === n) {
      if (sum === hap && arr1.length > 0) {
        answer++;
        return;
      }
    } else {
      arr1.push(arr[idx]);
      DFS(idx + 1, sum + arr[idx]);
      arr1.pop();
      DFS(idx + 1, sum);
    }
  }
  DFS(0, 0);
  return answer;
}


let [a,b]=input[0].split(' ').map((item)=>Number(item));
let arr=input[1].split(' ').map((item)=>Number(item));
console.log(sol(a,b,arr));
