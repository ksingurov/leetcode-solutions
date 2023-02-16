with
    parents_cte as (
        select distinct p_id
        from Tree
        where p_id is not null
    ),

    relatives_cte as (
        select
            t1.id
            ,t1.p_id
            ,t2.p_id as is_parent
        from Tree t1
        left join parents_cte t2
        on t1.id = t2.p_id
    )

select
    id
    ,case
        when p_id is null then 'Root'
        when is_parent is null then 'Leaf'
        else 'Inner'
        end as type
from relatives_cte
