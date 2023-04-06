with cte as (
    select
        month,
        country,
        state
        ,count(*) as trans_count
        ,sum(amount) as trans_total_amount
    from (
        select *, substring(trans_date, 1, 7) as month
        from Transactions
    ) t
    group by month, country, state
)

select
    t1.month
    ,t1.country
    ,t1.trans_count
    ,case
        when t2.approved_count is null then 0
        else t2.approved_count
    end approved_count
    ,t1.trans_total_amount
    ,case
        when t2.approved_total_amount is null then 0
        else t2.approved_total_amount
    end approved_total_amount
from (
    select
        month
        ,country
        ,sum(trans_count) as trans_count
        ,sum(trans_total_amount) as trans_total_amount
    from cte
    group by month, country
) t1
left join (
    select
        month
        ,country
        ,trans_count as approved_count
        ,trans_total_amount as approved_total_amount
    from cte
    where state = 'approved'
) t2
on t1.month = t2.month and t1.country = t2.country
