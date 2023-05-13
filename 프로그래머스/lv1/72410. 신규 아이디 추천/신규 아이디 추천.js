//아이디의 길이는 3자 이상 15자 이하여야 합니다.
//아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
//, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.
function solution(new_id) {
    let changeId = '';
    changeId = firstStep(new_id);
    changeId = secondStep(changeId)
    changeId = thirdStep(changeId);
    changeId = fourthStep(changeId);
    changeId = fifthStep(changeId);
    changeId = sixthStep(changeId);
    changeId = seventhStep(changeId);
    return changeId.reduce((acc, cur) => acc + cur, '');
}

const firstStep = (new_id) => {
    return new_id.toLowerCase();
}

const secondStep = (id) => {
    const regex = /^[a-z0-9\-\.\_]+$/;
    return [...id].filter((str) => regex.test(str));
}

const thirdStep = (id) => {
    const stack = [];
    for(str of id){
        if(stack[stack.length - 1] === '.' && str === '.') stack.pop();
        stack.push(str)
    }
    return stack
}

const fourthStep = (id) => {
    if (id[0] === '.') id.shift();
    if(id[id.length - 1] === '.') id.pop();
    return id;
}

const fifthStep = (id) => {
    if (id.length === 0) id.push('a');
    return id;
}

const sixthStep = (id) => {
    if (id.length >= 16) id.splice(15);
    if(id[id.length - 1] === '.') id.pop();
    return id
}

const seventhStep = (id) => {
    if(id.length <= 2){
        const lastStr = id[id.length - 1];
        while(id.length < 3) id.push(lastStr);
    }
    
    return id;
}
