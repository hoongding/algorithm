-- 길이가 10cm 이하면 NULL
-- 가장 큰 물고기 길이 + cm
SELECT CONCAT(MAX(LENGTH), 'cm') AS MAX_LENGTH FROM FISH_INFO