with lead_cte as (
    select
        *
        ,lead(num, 1) over (order by id) as lead1
        ,lead(num, 2) over (order by id) as lead2
    from Logs
)

select distinct
    num as ConsecutiveNums
from lead_cte
where num = lead1 and lead1 = lead2
