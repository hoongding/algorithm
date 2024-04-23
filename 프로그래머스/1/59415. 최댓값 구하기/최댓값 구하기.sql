-- 코드를 입력하세요
-- 동물 id, 종, 보호시작, 보호시작시 상태, 이름, 성별, 중성화 여부
-- NAME: nullable
-- 가장 최근에 들어온 동물 언제 들어왔는지 조회
SELECT MAX(DATETIME) as LAST_TIME FROM ANIMAL_INS