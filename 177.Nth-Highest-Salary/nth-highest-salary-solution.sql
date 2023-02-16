CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    RETURN (
        with
            cte1 as (
                select
                    *
                    ,dense_rank() over (order by salary desc) as salary_rank
                from Employee
            )
            ,cte2 as (
                select null as id, null as salary, salary_rank
                from (values row(N)) v(salary_rank)
            )
            ,cte3 as (
                select * from cte1 where salary_rank = N
                union all
                select * from cte2
            )

        select salary from cte3 limit 1
    );
END
