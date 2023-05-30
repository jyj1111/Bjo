const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

function sol(n, arr) {
  const dx = [1, 0, -1, 0];
  const dy = [0, -1, 0, 1];
  let ch = Array.from({ length: n }, () => Array(n).fill(0));
  let queue = [];
  let num_arr = [];
  let count = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (arr[i][j] === 1 && ch[i][j] === 0) {
        ch[i][j] = 1;
        count++;
        queue.push([i, j]);
      }
      let num = 0;
      while (queue.length) {
        num++;
        let [x, y] = queue.shift();
        for (let k = 0; k < 4; k++) {
          let nx = x + dx[k];
          let ny = y + dy[k];
          if (
            0 <= nx &&
            nx < n &&
            0 <= ny &&
            ny < n &&
            arr[nx][ny] === 1 &&
            ch[nx][ny] === 0
          ) {
            ch[nx][ny] = 1;
            queue.push([nx, ny]);
          }
        }
      }
      if (num > 0) {
        num_arr.push(num);
      }
    }
  }
  num_arr.sort((a, b) => a - b);
  let answer = count + "\n";
  for (let x of num_arr) {
    answer += x + "\n";
  }
  return answer;
}

let n = Number(input[0]);

const arr = [];
for (let i = 1; i <= n; i++) {
  const item = input[i].split("").map((item) => Number(item));
  arr.push(item);
}
console.log(sol(n, arr));