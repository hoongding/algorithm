// numbers (정수 배열)
// 배열의 각 원소들에 대해 자신보다 뒤에있는 숫자중, 자신보다 크면서 가장 가까이 있는수 => 뒷큰수
// 뒤부터 하면? 자신보다 작은수 있으면 
// 모든 원소에 대한 뒷큰수들을 차례로 담은 배열 return
// 뒷큰수 없으면 -1 담으셈

function solution(numbers) {
    const answer = Array(numbers.length).fill(-1)
    
    const stack = []
    
    for (let index = 0; index < numbers.length; index++){
        
        while(stack.length > 0 && numbers[index] > numbers[stack[stack.length - 1]]){
            const idx = stack.pop()
            answer[idx] = numbers[index]
        }
        
        stack.push(index)
    }
    
    
    
    return answer
}

