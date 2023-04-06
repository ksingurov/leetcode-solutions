with cte as (
    select
        user_id
        ,action
        ,count(*) as count
    from Confirmations
    group by user_id, action
)

select
    s.user_id
    ,case
        when c.confirmation_rate is null then 0
        else c.confirmation_rate
    end as confirmation_rate
from Signups s
left join (
    select
        t1.user_id
        ,round(t2.count / t1.count, 2) as confirmation_rate
    from (
        select user_id, sum(count) as count from cte group by user_id
    ) t1
    left join (
        select user_id, count from cte where action = 'confirmed'
    ) t2
    on t1.user_id = t2.user_id
) c
on s.user_id = c.user_id
