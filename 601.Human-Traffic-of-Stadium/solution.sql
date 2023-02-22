with cte1 as (
        select
            *
            ,lead(people, 1) over (order by id) as people_lead1
            ,lead(people, 2) over (order by id) as people_lead2
            ,lead(id, 1) over (order by id) as id_lead1
            ,lead(id, 2) over (order by id) as id_lead2
        from Stadium
    )
    ,cte2 as (
        select
            id, id_lead1, id_lead2
        from cte1
        where people >= 100 and people_lead1 >= 100 and people_lead2 >= 100
    )
    ,cte3 as (
        select id from cte2
        union
        select id_lead1 as id from cte2
        union
        select id_lead2 as id from cte2
    )

select
    t1.*
from Stadium t1
inner join cte3 t2 on t1.id = t2.id
