-- 코드를 입력하세요
SELECT FIRST_HALF.FLAVOR
FROM FIRST_HALF INNER JOIN ICECREAM_INFO ON FIRST_HALF.FLAVOR = ICECREAM_INFO.FLAVOR 
WHERE INGREDIENT_TYPE = 'fruit_based'
GROUP BY FIRST_HALF.FLAVOR 
HAVING SUM(FIRST_HALF.TOTAL_ORDER) > 3000
ORDER BY SUM(FIRST_HALF.TOTAL_ORDER) DESC;
