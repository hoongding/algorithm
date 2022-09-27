def solution(phone_book):
    # 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
    # phone_book: 전화번호부에 적힌 전화번호를 담은 배열
    # 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false
    # ["119", "97674223", "1195524421"]	-> false
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return answer