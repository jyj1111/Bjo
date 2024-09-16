const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, m] = input[0].split(" ").map((item) => Number(item));
let board = Array.from({ length: n }, () => Array(m).fill(0));
for (let i = 1; i <= n; i++) {
  board[i] = input[i].split("").map((item) => Number(item));
}
function solution(board) {
  let max = 0;
  let x = board[0].length;
  let y = board.length;
  if (x === 1) return Math.max(...board) ** 2;
  let dp = Array.from({ length: y }, () => Array(x).fill(0));
  for (let i = 0; i < y; i++) {
    dp[i][0] = board[i][0];
  }
  for (let j = 0; j < x; j++) {
    dp[0][j] = board[0][j];
  }
  for (let i = 1; i < y; i++) {
    for (let j = 1; j < x; j++) {
      if (board[i][j])
        dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1;
      max = Math.max(dp[i][j], max);
    }
  }
  return max ** 2;
}
console.log(solution(board));