// 일정한 금액 지불하면 10일동안 회원 자격을 부여
// 회원 대상으로 한가지 제품을 할인
// 할인은 하루에 하나씩만 구매 가능
// want: 원하는 제품
// number: 제품 수량
// discount 배열 -> 모두 할인 받을 수 있는 회원등록 날짜 총 일수를 return
// 조건: 10일 연속으로 일치할 경우

// 1. discount 배열 돌아서 {want, number} 객체 만들기
// 2. edge case 생각 -> discount 배열에서 want 배열에 있는놈 없으면? 0 return
// 14개 -> 10 11 12 13 14
function solution(want, number, discount) {
    let answer = 0;
    
    const needs = getMyNeeds(want, number)
    const discountProducts = getMap(discount)
    
    if (Object.keys(needs).length > Object.keys(discountProducts).length) return 0
    
    for (let i = 0; i <= discount.length - 10; i++){
        if(compareMap(getMap(discount.slice(i, i+10)), needs)) answer += 1
    }
    
    return answer;
}

const getMap = (discountArr) => {
    return discountArr.reduce((acc, cur) => {
        if (acc?.[cur]) acc[cur] += 1
        else acc[cur] = 1
        
        return acc
    }, {})
}

const getMyNeeds = (want, number) => {
    const needs = {}
    want.map((product, index) => {
        needs[product] = number[index]
    })
    
    return needs
}

const compareMap = (a, b) => {
    const aKeys = Object.keys(a)
    return aKeys.every((key) => {
        return a[key] === b[key]
    })
}