select
  t1.name
  ,case
    when t2.travelled_distance is null then 0
    else t2.travelled_distance
  end as travelled_distance
from
Users t1
left join
(
select
  user_id
  ,sum(distance) as travelled_distance
from Rides
group by user_id
) t2
on t1.id = t2.user_id
order by t2.travelled_distance desc, t1.name
