with
    cte1 as (
        select
            *
            ,out_time - in_time as office_time
        from Employees
    )
    ,cte2 as (
        select
            event_day as day
            ,emp_id
            ,sum(office_time) as total_time
        from cte1
        group by emp_id, event_day
    )

select * from cte2
