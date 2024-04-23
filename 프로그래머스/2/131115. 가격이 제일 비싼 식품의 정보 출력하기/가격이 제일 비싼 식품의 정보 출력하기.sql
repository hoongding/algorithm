-- 가격이 제일 비싼 식품의 식품 ID, 식품 이름, 코드, 분류, 식품 가격 조회
-- 모든 정보 조회이므로, *로 모든 정보 조회!
SELECT * FROM FOOD_PRODUCT
WHERE PRICE = (SELECT MAX(PRICE) FROM FOOD_PRODUCT)