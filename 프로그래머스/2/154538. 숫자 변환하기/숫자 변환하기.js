// x -> y 로 변환
// 1. x + n
// 2. x * x
// 3. x + 2x
// 연산횟수 return, x -> y 못하면 -1을 return

function solution(x, y, n) {
    if (x === y) return 0
    if (x > y) return -1
    
    const queue = []
   // [현재값, 연산횟수]
    queue.push([y, 0])
    
    const visited = new Set()
    visited.add(y);
    
    while (queue.length) {
        const [current, steps] = queue.shift()
        
        const prevValues = []
        
        if (current - n >= x) prevValues.push(current - n)
        if (current % 2 === 0 && current/2 >= x) prevValues.push(current / 2)
        if (current % 3 === 0 && current/3 >= x) prevValues.push(current / 3)
        
        for (let prev of prevValues) {
            if (prev === x) {
                return steps + 1
            }
            
            if(!visited.has(prev)){
                visited.add(prev)
                queue.push([prev, steps + 1])
            }
        }
        
    }
    
    return -1
}