const rl = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout,
})
let [N, i, O] = [0, 0, []]
function swap(A, i, j) {
  const temp = A[i]
  A[i] = A[j]
  A[j] = temp
}
rl.on('line', function (l) {
  if (!i++) N = +l
  else {
    A = l.split(' ').map(Number)
    for (const x of A) {
      O.push(x)
      let c = O.length - 1
      while (c) {
        const p = ~~((c - 1) / 2)
        if (O[p] < O[c]) break
        swap(O, p, c)
        c = p
      }
      if (O.length > N) {
        const last = O.pop()
        const l = O.length
        if (l) O[0] = last
        let p = 0
        while (p < (l - 1) / 2) {
          const l = p * 2 + 1
          const r = p * 2 + 2
          const c = O[r] < O[l] ? r : l
          if (O[p] < O[c]) break
          swap(O, p, c)
          p = c
        }
      }
    }
  }
}).on('close', function () {
  console.log(O[0])
  process.exit()
})