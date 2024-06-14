SELECT 
    First_Name || ' ' || LastName AS EmployeeName,
    Position,
    Email,
    VacationHours AS "Accrued Vacation Hours"
FROM 
    Employees
WHERE 
    VacationHours >= 40;