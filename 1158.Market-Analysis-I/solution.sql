with orders_in_2019 as (
    select
        buyer_id
        ,count(*) as orders_in_2019
    from Orders
    where year(order_date) = 2019
    group by buyer_id
)

select
    t1.user_id as buyer_id
    ,t1.join_date
    ,case
        when t2.orders_in_2019 is null then 0
        else t2.orders_in_2019
    end as orders_in_2019
from Users t1
left join orders_in_2019 t2
on t1.user_id = t2.buyer_id
