with
    cte1 as (
        select
            product_id
            ,case
                when sale_date < '2010-01-01' or sale_date > '2019-03-31' then 1
                else 0
                end sale_date_ind
        from Sales
    )
    ,cte2 as (
        select
            product_id
            ,sum(sale_date_ind) as not_2023Q1
        from cte1
        group by product_id
    )

select
    t1.product_id
    ,t2.product_name
from cte2 t1
left join Product t2 on t1.product_id = t2.product_id
where t1.not_2023Q1 = 0
