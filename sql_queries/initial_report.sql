
select
	person.firstname || ' ' || person.lastname as Employee_Name,
	employee.jobtitle as Job_Title,
	employee.vacationhours as Vacation_Hours,
	emailaddress.emailaddress as Email_Address
from
	humanresources.employee
join person.person
on
	employee.businessentityid = person.businessentityid
join person.emailaddress
  on
	person.emailaddress.businessentityid = person.businessentityid
where employee.vacationhours > 39;