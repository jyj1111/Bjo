const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const cnt = +input.shift()

input = input[0].split(' ').map(item=>Number(item))

let count = {};
for(let c in input){
    if(!count[input[c]]){
        count[input[c]] = 1;
    }else{
        count[input[c]]++;
    }
}

const stack = []
const result = new Array(cnt).fill(-1)
for(let i=0;i<cnt;i++){
    while(stack.length >0 && count[input[i]] > count[input[stack[stack.length-1]]]){
        result[stack.pop()]=input[i]
    }
    stack.push(i)
}

console.log(result.join(' '))
