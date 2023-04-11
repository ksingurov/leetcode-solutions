select
    case
        when lead_id is null and odd = 1 then id
        when odd = 1 then lead_id
        else lag_id
    end as id
    ,student
from (
    select
        *
        ,id % 2 as odd
        ,lead(id) over (order by id) as lead_id
        ,lag(id) over (order by id) as lag_id
    from Seat
) t
order by id
