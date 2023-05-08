// 알아볼 수 없는 번호를 0으로 표기
// 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1, 0
function solution(lottos, win_nums) {
    let curCorrectNum = 0;
    let zeroCount = 0;
    lottos.forEach((number) => {
        if(win_nums.includes(number)) curCorrectNum += 1;
        if(number === 0) zeroCount += 1;
    })
    const highRank = curCorrectNum + zeroCount;
    return [ranking[highRank], ranking[curCorrectNum]];
}

const ranking = {
    6: 1,
    5: 2,
    4: 3,
    3: 4,
    2: 5,
    1 : 6,
    0: 6,
}