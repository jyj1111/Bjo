const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
class MinBinaryHeap {
  constructor() {
    this.values = [];
  }
  empty() {
    return this.values.length === 0 ? true : false;
  }
  insert(element) {
    this.values.push(element);
    this.bubbleUp();
  }
  bubbleUp() {
    let idx = this.values.length - 1;
    let child = this.values[idx];
    while (idx > 0) {
      let parentIdx = Math.floor((idx - 1) / 2);
      let parent = this.values[parentIdx];
      if (child > parent) break;
      [this.values[parentIdx], this.values[idx]] = [child, parent];
      idx = parentIdx;
    }
  }
  pop() {
    let min = this.values[0];
    let idx = this.values.length - 1;
    let last = this.values[idx];
    [this.values[0], this.values[idx]] = [last, min];
    this.values.pop();
    this.sinkDown();
    return min;
  }
  sinkDown() {
    let idx = 0;
    let parent = this.values[idx];
    let length = this.values.length;
    while (idx < length) {
      let leftIdx = 2 * idx + 1;
      let rightIdx = 2 * idx + 2;
      let leftChild = this.values[leftIdx] || Number.MAX_SAFE_INTEGER; //왼쪽자식이 없는경우 숫자의 최대값 할당
      let rightChild = this.values[rightIdx] || Number.MAX_SAFE_INTEGER; //오른쪽 자식이 없는 경우 숫자의 최대값 할당
      if (parent <= Math.min(leftChild, rightChild)) break;
      if (leftChild < rightChild) {
        [this.values[idx], this.values[leftIdx]] = [leftChild, parent];
        idx = leftIdx;
      } else {
        [this.values[idx], this.values[rightIdx]] = [rightChild, parent];
        idx = rightIdx;
      }
    }
  }
}
let minHeap=new MinBinaryHeap();
const n=+input[0];

for(let i=1;i<=n;i++){
    minHeap.insert(+input[i]);
}
let sum=0;
for(let i=1;i<n;i++){
    let first=minHeap.pop();
    let second=minHeap.pop();
    sum+=first+second;
    minHeap.insert(first+second);
}

console.log(sum);



