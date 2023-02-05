const fs=require('fs');
let input=fs.readFileSync('dev/stdin').toString().trim().split('\n');
let have=input[1].split(' ').map((item)=>Number(item));
const problem=input[3].split(' ').map((item)=>Number(item));
let haveMap = new Map();
have.forEach((item) => {
  haveMap.get(item)
    ? haveMap.set(item, haveMap.get(item) + 1)
    : haveMap.set(item, 1);
});
have = [...haveMap];
let solve = [];
have.sort((a, b) => a[0] - b[0]);
for (let i = 0; i < problem.length; i++) {
  let lt = 0;
  let rt = have.length - 1;
  while (lt <= rt) {
    let mid = parseInt((lt + rt) / 2);
    if (have[mid][0] === problem[i]) {
      solve.push(have[mid][1]);
      break;
    } else if (have[mid][0] < problem[i]) {
      lt = mid + 1;
    } else {
      rt = mid - 1;
    }
  }
  if (solve.length === i) solve.push(0);
}
console.log(solve.join(" "));