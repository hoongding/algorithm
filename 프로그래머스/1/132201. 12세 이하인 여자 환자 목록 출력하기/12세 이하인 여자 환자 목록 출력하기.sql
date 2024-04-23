-- 12세 이하인 여자환자 전체 조회
SELECT p.PT_NAME, p.PT_NO, p.GEND_CD, p.AGE, IFNULL(p.TLNO, 'NONE') as TLNO FROM PATIENT p
WHERE p.AGE <= 12 and p.GEND_CD = 'W'
ORDER BY p.AGE desc, p.PT_NAME asc