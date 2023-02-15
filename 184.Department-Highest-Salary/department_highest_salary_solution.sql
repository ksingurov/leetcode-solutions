with rank_table as (
    select
        departmentId
        ,name as Employee
        ,salary as Salary
        ,dense_rank() over (partition by departmentId order by salary desc) as rank_n
    from Employee
)

select
    t2.name as Department
    ,t1.Employee
    ,t1.Salary
from rank_table t1
left join Department t2
on t1.departmentId = t2.id
where t1.rank_n = 1
