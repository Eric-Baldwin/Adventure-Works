SELECT 
    CASE 
        WHEN listprice BETWEEN 0 AND 100 THEN '$0 - $100'
        WHEN listprice BETWEEN 101 AND 200 THEN '$101 - $200'
        WHEN listprice BETWEEN 201 AND 300 THEN '$201 - $300'
        ELSE '$300+'
    END AS price_bracket,
    COUNT(*) AS product_count
FROM 
    production.product
GROUP BY 
    CASE 
        WHEN listprice BETWEEN 0 AND 100 THEN '$0 - $100'
        WHEN listprice BETWEEN 101 AND 200 THEN '$101 - $200'
        WHEN listprice BETWEEN 201 AND 300 THEN '$201 - $300'
        ELSE '$300+'
    END
ORDER BY 
    price_bracket;