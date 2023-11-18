const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
function sol(n, arr) {
  let answer = Array(n).fill(-1);
  let stack = [];
  for (let i = 0; i < n; i++) {
    while (stack.length > 0 && arr[stack[stack.length - 1]] < arr[i]) {
      
      answer[stack.pop()] = arr[i];
    }
    stack.push(i);
  }
  
  return answer.join(' ');
}

let arr = input[1].split(" ").map((item) => Number(item));

console.log(sol(Number(input[0]), arr));