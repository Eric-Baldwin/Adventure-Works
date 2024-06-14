DAI SQL Case Study Overview
You will be preparing a suite of SQL queries and initial reports using the AdventureWorks dataset.

Remember:

Any reports that will be shown to people should have accurate, human-readable labels and relevant titles.
Code should be commented in a way that will help others (or your future self) understand the purpose of your program and any important design decisions that you have made.
Store each individual query as a properly commented .sql file. Store all of your queries in a directory named sql_queries.


---------------------------------------------------------------------------------


HR Questions
The HR Department would like to proactively encourage employees to take their PTO.


Question 1
Create a SQL query that generates a report for HR that includes:

The employee's name (at least first and last).
The employee's position in the company.
The employee's email address.
How many vacation hours the employee has accrued.
Only employees who have accrued more than a certain number of hours.
HR may like to change this threshold in the future.
Human-readable titles and column headers that reflect the chosen threshold.
They would like to begin by contacting employees who have accrued 40 or more hours of vacation. Create an initial report for this threshold.

Save a copy of this report so it can be opened in Excel.


Question 2
HR would also be interested in how many employees are affected at this threshold.


----------------------------------------------------------------------------


Product Questions
The product team is looking for opportunities to expand offerings and would like to gain some big-picture insight into the AdventureWorks product line.

Some information about product categories and price points may help guide their upcoming brainstorming sessions.


Question 1
The product team thinks it would be helpful to see similar products grouped together and to see the price ranges and number of products in each group.

AdventureWorks products often have a category and a subcategory, so it will probably be helpful to generate two reports.

Price Ranges by Category

The product team would like to know the price range for each product category in the catalog.

This report should include:

The lowest price per category.
The highest price per category.
The difference in cost between the highest and lowest priced items in each category.
The name for each category.
The number of products included in each category.
Price Ranges by Subcategory

This report should include:

The lowest price per subcategory.
The highest price per subcategory.
The difference in cost between the highest and lowest priced items in each subcategory.
The name for each category.
The report should additionally include:

The name for each subcategory.
The number of products included in each subcategory.
It would be helpful if this report were organized by category and then by subcategory.

There are a few items on inventory that do not have a category.

What best describes the reason for this situation?
What should be done about this data as you are creating your reports?
How should null values be handled?


Question 2
At the very end of a meeting with the product team, a team member mentioned that they would like to see a count of products per price bracket. You would like to create an initial report considering all AdventureWorks products without bothering with categories or subcategories. There wasn't any guidance given as to what brackets should be considered.

Count of Products per Price Bracket

Your report should include:

The number of products in each price bracket.
What price brackets make sense and would be useful to consider?
Is there any data that may be useful to exclude or define?


-------------------------------------------------------------------------------------


Sales Questions
The sales team would like a few initial reports created for an upcoming discussion.

The sales team passed this list of Sales Order Status definitions to you to help with your reports.

- 1: In Process
- 2: Approved
- 3: Backordered
- 4: Rejected
- 5: Shipped
- 6: Cancelled


Question 1
Count of Shipped Orders & Subtotals by Month

Prepare a report showing a monthly summary of the number of orders that have shipped and the subtotal (pre-tax and shipping) for the entire history of the company.

This report should:

Group orders by when they were placed.
Only include orders that were shipped.
Provide a monthly subtotal (not including tax and shipping)
Be organized by year and then month
Bonus:
The sales department asks if you could create line graphs for Orders per Month and Subtotals per Month.


Question 2
The sales team would like to see a report of how much each store that purchases from AdventureWorks has spent.

This report should:

Include only orders that were shipped.
Include each store's name, customerid, and storeid
Include the total amount each store ordered (before tax and shipping).
Show the biggest spenders first.
Hint: The last analyst who worked here was muttering something about business entity IDs and store IDs.


Extra Credit: other avenues of inquiry
What product has the greatest profit margin?

Overall
per category
per subcategory
Shrink

Waste

Which locations have the most Scrap by gross cost (Standard Cost)?
Customers (Business to Business & Business to Customer)

B2B:

Which stores orders the most
pre-tax,
pre-shipping dollar value
shipped orders only
What are the top ? orders...
B2C

Sales Order Status definitions:
1: In process
2: Approved
3: Backordered
4: Rejected
5: Shipped
6: Cancelled

-------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

Brief

You will write a Python script file that takes sql queries stored in the sql_queries directory as .sql files, performs the search, and returns the result of the search as an Excel Workbook with an .xlsx file extension.

Your script should be importable and callable as a function. Your program should also be able to be run from the command line, taking a directory full of .sql queries as input, and populating a given folder with .xlsx files as output.

Here is a little code to get you started. You will likely need helper functions in addition to these functions.

It is heavily recommended to search and peruse the Pandas documentation for relevant methods that will assist in your task. You are likely not the first coder to have a similar task. The Python os library may also be useful.

Your .py files should each contain an INEM block.

Here are a few stems to help you get started.


def convert_sql_to_xlsx(sql_in, xlsx_out, xlsx_name=None):
    """
    Runs query in given .sql file, stores result as .xlsx file.

    Parameters:
        sql_in (str): relative filepath to .sql file
        xlsx_out (str): relative filepath to directory where .xlsx will be stored
        xlsx_name (str or None): If not None, file named xlsx_name.xlsx
                                 If None, file named same as sql_in

    Returns:
        None
    """
    pass

def convert_directory_of_queries(sql_in_dir, xlsx_out_dir):
    """
    Runs each query in sql_in_dir directory,
        stores each result as .xlsx in xlsx_out_dir.

    Parameters:
        sql_in_dir (str): relative filepath to directory
                          containing .sql files
        xlsx_out_dir (str): relative filepath to directory
                            where .xlsx will be stored
                            files named same as sql_in

    Returns:
        None
    """
    pass

def convert_sql_to_xlsx_from_cli():
    """
    Converts directory of sql queries to xlsx from CLI.
    """
    pass
