select
    query_name
    ,round(100*avg(case when rating < 3 then 1 else 0 end), 2) as poor_query_percentage
    ,round(avg(rating/position), 2) as quality
from Queries
group by query_name
