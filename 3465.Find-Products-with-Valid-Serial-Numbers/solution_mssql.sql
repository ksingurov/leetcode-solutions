SELECT *
FROM products
WHERE description LIKE '%SN[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][^0-9]%'
    OR RIGHT(description, 11) LIKE 'SN[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]'
ORDER BY product_id
