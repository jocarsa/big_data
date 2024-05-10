SELECT 
ciudad,
COUNT(*) AS numero 
FROM ciudades 
GROUP BY ciudad
ORDER BY numero DESC