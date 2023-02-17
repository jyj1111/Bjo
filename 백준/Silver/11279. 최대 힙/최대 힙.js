const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0]);
const commands = input.slice(1, 1 + N).map(Number);
class MaxBinaryHeap {
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
      if (child <= parent) break;
      [this.values[parentIdx], this.values[idx]] = [child, parent];
      idx = parentIdx;
    }
  }
  pop() {
    let max = this.values[0];
    let idx = this.values.length - 1;
    let last = this.values[idx];
    [this.values[0], this.values[idx]] = [last, max];
    this.values.pop();
    this.sinkDown();
    return max;
  }
  sinkDown() {
    let idx = 0;
    let parent = this.values[idx];
    let length = this.values.length;
    while (idx < length) {
      let leftIdx = 2 * idx + 1;
      let rightIdx = 2 * idx + 2;
      let leftChild = this.values[leftIdx] || Number.MIN_SAFE_INTEGER; //왼쪽자식이 없는경우 숫자의 최솟값 할당
      let rightChild = this.values[rightIdx] || Number.MIN_SAFE_INTEGER; //오른쪽 자식이 없는 경우 숫자의 최솟값 할당
      if (parent >= Math.max(leftChild, rightChild)) break;
      if (leftChild > rightChild) {
        [this.values[idx], this.values[leftIdx]] = [leftChild, parent];
        idx = leftIdx;
      } else {
        [this.values[idx], this.values[rightIdx]] = [rightChild, parent];
        idx = rightIdx;
      }
    }
  }
}

const solution = (N, commands) => {
  const maxHeap = new MaxBinaryHeap();
  let answer = '';
  commands.forEach((command) => {
    if (command === 0) {
      if (maxHeap.empty()) answer += '0\n';
      else answer += maxHeap.pop() + '\n';
    } else {
      maxHeap.insert(command);
    }
  });
  return answer;
};

console.log(solution(N, commands));