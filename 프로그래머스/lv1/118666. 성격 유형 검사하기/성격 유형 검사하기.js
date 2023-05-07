// survey의 원소는 "RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA" 중 하나.
// 첫번째 알파벳은 비동의
// 두번째 알파벳은 동의
// 비동의 : 1 2 3 
// 4 
// 동의 : 5 6 7
function solution(survey, choices) {
    survey.forEach((question, idx) => {
        const agreeArr = [...question];
        const choice = choices[idx];
        const [targetChoice, targetScore] = calScore(choice);
        score[agreeArr[+targetChoice]] += targetScore;
    })
    return getResult();
}

const score = {
    R: 0, T: 0,
    C: 0, F: 0,
    J: 0, M: 0,
    A: 0, N: 0,
}

const calScore = (choice) => {
    switch(choice){
        case 1:
            return [0, 3];
        case 2:
            return [0, 2];
        case 3:
            return [0, 1];
        case 4:
            return [0, 0];
        case 5:
            return [1, 1];
        case 6:
            return [1, 2];
        case 7:
            return [1, 3];
    }
}

const getResult = () => {
    let result = '';
    if(score['R'] >= score['T']) result += 'R';
    else result += 'T';
    if(score['C'] >= score['F']) result += 'C';
    else result += 'F';
    if(score['J'] >= score['M']) result += 'J';
    else result += 'M';
    if(score['A'] >= score['N']) result += 'A';
    else result += 'N';
    return result;
}