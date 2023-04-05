with
    cte as (
select
    case
        when customer_pref_delivery_date = order_date then 'immediate'
        else 'scheduled'
    end as type
from
(
select
    order_date
    ,customer_pref_delivery_date
    ,row_number() over (partition by customer_id order by order_date) as num
from Delivery
) t
where num = 1
)

,cte2 as (
    select count(*) as count_all from cte
)

select
    round(100 * t1.count_immediate / t2.count_all, 2) as immediate_percentage
from
(
select count(*) as count_immediate
from cte
where type = 'immediate'
group by type
) t1
cross join (select count(*) as count_all from cte) t2
