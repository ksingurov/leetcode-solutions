select stock_name, capital_gain_loss
from
(
select
  stock_name
  ,operation
  ,sum - lead(sum) over (order by stock_name, operation) as capital_gain_loss
from
(
select
  stock_name
  ,operation
  ,sum(price) as sum
from Stocks
group by stock_name, operation
order by stock_name, operation
) t1
) t2
where operation = 'Sell'
