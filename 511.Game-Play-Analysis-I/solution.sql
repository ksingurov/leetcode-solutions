with cte as (
    select
        player_id
        ,event_date
        ,row_number() over (partition by player_id order by event_date) as login_n
    from Activity
)

select player_id, event_date as first_login
from cte where login_n = 1
