select
    user_id as id
    ,count(*) as num
from
(
select
    requester_id as user_id
    ,accepter_id as friend_id
from RequestAccepted
union
select
    accepter_id
    ,requester_id
from RequestAccepted
) t
group by user_id
order by num desc
limit 1
