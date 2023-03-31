with
    cte1 as (
        select
            machine_id
            ,process_id
            ,timestamp as t_start
        from Activity
        where activity_type = 'start'
    )

    ,cte2 as (
        select
            machine_id
            ,process_id
            ,timestamp as t_end
        from Activity
        where activity_type = 'end'
    )

select
    t1.machine_id
    ,round(avg(t2.t_end - t1.t_start), 3) as processing_time
from cte1 t1
left join cte2 t2
on t1.machine_id = t2.machine_id and t1.process_id = t2.process_id
group by t1.machine_id
