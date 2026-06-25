-- 코드를 입력하세요
-- 동물 이름 중, 이름에 "EL"이 들어가는 개의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 
-- 이때 결과는 이름 순으로 조회해주세요. 만약 이름이 같은 경우 아이디를 기준으로 조회해주세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME
LIKE '%EL%'
AND  ANIMAL_TYPE = 'DOG'
ORDER BY NAME, ANIMAL_ID;