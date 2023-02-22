with cte as (
    select
    email
    ,count(*) as count_emails
    from Person
    group by email
)

select email as Email from cte where count_emails > 1
