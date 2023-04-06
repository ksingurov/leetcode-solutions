select
    t1.contest_id
    ,round(100*count(*)/t2.total, 2) as percentage
from Register t1
cross join (select count(*) as total from Users) t2
group by t1.contest_id
order by percentage desc, t1.contest_id
