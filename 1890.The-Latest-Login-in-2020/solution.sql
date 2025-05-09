select
    user_id
    ,time_stamp as last_stamp
from
(
select
    user_id
    ,time_stamp
    ,row_number() over (partition by user_id order by time_stamp desc) as num
from Logins
where year(time_stamp) = 2020
) t
where num = 1
