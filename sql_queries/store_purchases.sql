select
	soh.customerid
,
	cust.storeid
,
	store.name as store_name
,
	SUM(soh.subtotal) as sum_subtotal
from
	sales.salesorderheader as soh
join sales.customer as cust
		using(customerid)
left join sales.store as store
on
	cust.storeid = store.businessentityid
where
	soh.status = 5
	and cust.storeid is not null
group by
	1,
	2,
	3
order by
	4 desc;