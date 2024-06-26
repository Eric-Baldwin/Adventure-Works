# Adventure Works - SQL to XLSX Reports

This Python script takes SQL queries stored in a directory as `.sql` files, executes them, and exports the results as Excel workbooks with `.xlsx` file extensions.

## Requirements

- **Python 3.6+**
- **psycopg2**
- **pandas**
- **python-dotenv**
- **argparse**

## Setup

1. **Clone the repository.**
2. **Install the required Python packages using pip:**

   `pip install psycopg2-binary pandas python-dotenv argparse`

3. **Create a .env file in the root directory of the project with your database connection parameters:**
   ```
   AW_DB=your_database_name
   AW_USER=your_username
   AW_PASSWORD=your_password
   AW_HOST=your_host
   AW_PORT=your_port
   ```

## Usage

### As a Python module

Import the `convert_sql_to_xlsx` function from the script in your own Python programs to convert SQL files in a directory to Excel:

`from main import convert_sql_to_xlsx`

# Convert all SQL files in a directory to Excel

`convert_sql_to_xlsx('sql_queries', 'excel_reports')`

### From the command line

You can also run the script from the command line, passing the directory containing the .sql files and the directory where the .xlsx files should be written as arguments:

`python main.py sql_queries excel_reports`

## SQL Queries

The SQL queries should be stored as `.sql` files in the `sql_queries` directory. Each file should contain a single SQL query.

## Excel Reports

The Excel reports generated by the script will be stored in the `excel_reports` directory. The name of each report will match the name of the SQL file it was generated from, with the `.sql` extension replaced by `.xlsx`.

## Collaborators

1. Donna Farris
2. CJ Jones
3. Simon Kanyiva
4. E. Baldwin
