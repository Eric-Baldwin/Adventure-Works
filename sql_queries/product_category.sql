

SELECT
    production.productcategory.name AS category_name,
    MIN(production.product.listprice) AS lowest_price,
    MAX(production.product.listprice) AS highest_price,
    MAX(production.product.listprice) - MIN(production.product.listprice) AS price_difference
FROM
    production.product
JOIN
    production.productsubcategory ON production.product.productsubcategoryid = production.productsubcategory.productsubcategoryid
JOIN
    production.productcategory ON production.productsubcategory.productcategoryid = production.productcategory.productcategoryid
GROUP BY
    production.productcategory.name
ORDER BY
    production.productcategory.name;