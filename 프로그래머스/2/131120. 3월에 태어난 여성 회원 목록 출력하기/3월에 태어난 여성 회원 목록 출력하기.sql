-- 생일이 3월인, 여성 회원
-- ID, 이름, 성별, 생년월일
-- NULL인 경우 제외
-- 회원 ID를 기준으로 오름차순
SELECT p.member_id, p.member_name, p.gender, date_format(p.date_of_birth, '%Y-%m-%d') as date_of_birth
FROM MEMBER_PROFILE p
WHERE p.gender = 'W' and month(p.date_of_birth) = '03' and p.tlno is not null 
ORDER BY p.member_id asc