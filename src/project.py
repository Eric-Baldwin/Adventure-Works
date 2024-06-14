import psycopg2
from dotenv import load_dotenv
import os
import pandas as pd

# Load variables from .env
load_dotenv()

# Define connection parameters
params = {
    "dbname": os.getenv("AW_DB"),
    "user": os.getenv("AW_USER"),
    "password": os.getenv("AW_PASSWORD"),
    "host": os.getenv("AW_HOST"),
    "port": os.getenv("AW_PORT")
}

# Establish the connection
conn = psycopg2.connect(**params)

# Create a cursor object
cur = conn.cursor()

# Get % of employees affected within initial report threshold


def get_employees_affected():
    with open('sql_queries/count_employees.sql', 'r') as sql_file:
        df = pd.read_sql_query(sql_file.read(), conn)
        df.to_excel('excel_reports/affected_employees_report.xlsx', index=False)


get_employees_affected()

# Generate initial report:


def generate_report():
    with open('sql_queries/initial_report.sql', 'r') as sql_file:
        cur.execute(sql_file.read())

        # Fetch all the rows
        rows = cur.fetchall()

        # Print each row
        for row in rows:
            print(row)


# generate_report()

# Generate initial report in xlsx format:


def generate_report_xlsx():

    with open('sql_queries/initial_report.sql', 'r') as sql_file:
        df = pd.read_sql_query(sql_file.read(), conn)
        df.to_excel('excel_reports/initial_report.xlsx', index=False)


# generate_report_xlsx()

# Close the cursor and connection
cur.close()
conn.close()
