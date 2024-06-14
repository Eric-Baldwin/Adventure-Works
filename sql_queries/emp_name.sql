select
	person.firstname || ' ' || 	person.lastname as employeename,
	employee.jobtitle
from
	humanresources.employee
join person.person
on
	employee.businessentityid = person.businessentityid
limit 5;