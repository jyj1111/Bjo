const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

function sol(m, n) {
  let checked = Array(m + 1).fill(0);
  let arr1 = [];
  let answer = "";
  function DFS(idx) {
    if (idx === n) {
      answer += arr1.join(" ") + "\n";

      return;
    } else {
      for (let i = 1; i <= m; i++) {
        if (!checked[i]) {
          checked[i] = 1;
          arr1.push(i);
          DFS(idx + 1);
          arr1.pop();
          checked[i] = 0;
        }
      }
    }
  }
  DFS(0);
  return answer;
}


let arr=input[0].split(' ').map((item)=>Number(item));
console.log(sol(arr[0],arr[1]));
