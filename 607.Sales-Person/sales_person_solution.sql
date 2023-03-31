with cte as (
    select distinct
        t1.sales_id
        # ,t2.name
    from Orders t1
    left join Company t2
    on t1.com_id = t2.com_id
    where t2.name = 'RED'
)

select
    t1.name
from SalesPerson t1
left join cte t2
on t1.sales_id = t2.sales_id
where t2.sales_id is null
