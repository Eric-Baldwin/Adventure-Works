
SELECT SUM(daily_shipped) as total_shipped, SUM(daily_subtotal) as subtotal, yr, mnth
  FROM (
select
	COUNT(salesorderid) as daily_shipped,
	SUM(subtotal) as daily_subtotal,
	extract(year
from
	orderdate::timestamp) as yr,
	extract(month
from
	orderdate::timestamp) as mnth

from
	sales.salesorderheader
join sales.salesorderdetail
	using(salesorderid)
where
	status = 5
group by
	mnth,
yr,
orderdate
order by
	orderdate)
group by
yr,
mnth
order by
yr,
mnth;