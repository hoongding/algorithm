-- type = suv 인 자동차 평균 일일대여 요금 출력
SELECT ROUND(AVG(DAILY_FEE)) FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV'