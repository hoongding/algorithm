-- 동일한 회원이 동일한 상품 재구매한 데이터 구하기
-- 재구매한 회원 id, 상품 id 출력
-- 회원 id 오름차순, 상품 id 내림차순
SELECT distinct s.user_id, s.product_id
FROM ONLINE_SALE s
group by s.user_id, s.product_id
having (count(s.product_id) > 1)
ORDER BY s.user_id asc, s.product_id desc