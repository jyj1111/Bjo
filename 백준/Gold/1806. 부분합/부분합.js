const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

function sol(n, s, arr) {
  let p1 = 0;
  let p2 = 0;
  let min = n + 1;
  let hap = arr[0];
  while (p1 < n && p2 < n) {
    if (hap >= s) {
      min = Math.min(min, p2 - p1 + 1);

      hap -= arr[p1++];
    } else {
      hap += arr[++p2];
    }
  }
  if (min === n + 1) {
    min = 0;
  }

  return min;
}
const [n, s] = input[0].split(" ");
let arr = input[1].split(" ").map((item) => +item);

console.log(sol(+n, +s, arr));