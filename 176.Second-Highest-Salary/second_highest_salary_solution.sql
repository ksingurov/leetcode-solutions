select
    salary as SecondHighestSalary
from (
    select
        salary
        ,dense_rank() over (order by salary desc) as salary_rank
    from Employee
    union all
    select
        null as salary
        ,salary_rank
    from (values row(2)) v(salary_rank)
    ) t
where salary_rank = 2
order by salary desc
limit 1