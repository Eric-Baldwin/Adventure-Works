import psycopg2
from dotenv import load_dotenv
from os import getenv, listdir
from os.path import join, isfile
import pandas as pd
import argparse

# Load variables from .env
load_dotenv()

# Define connection parameters
params = {
    "dbname": getenv("AW_DB"),
    "user": getenv("AW_USER"),
    "password": getenv("AW_PASSWORD"),
    "host": getenv("AW_HOST"),
    "port": getenv("AW_PORT")
}

# Establish the connection
conn = psycopg2.connect(**params)

# Create a cursor object
cur = conn.cursor()


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
    filename = sql_in[12:-4]
    with open(sql_in, 'r') as sql_file:
        df = pd.read_sql_query(sql_file.read(), conn)
        if xlsx_name:
            df.to_excel(f"{xlsx_out}/{xlsx_name}.xlsx", index=False)
        else:
            df.to_excel(f"{xlsx_out}/{filename}.xlsx", index=False)


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
    for filename in listdir(sql_in_dir):
        sql_in = join(sql_in_dir, filename)
        convert_sql_to_xlsx(sql_in, xlsx_out_dir)


def convert_sql_to_xlsx_from_cli():
    """
    Converts directory of sql queries to xlsx from CLI.
    """
    parser = argparse.ArgumentParser(
        description="Execute SQL queries and export results to Excel.")
    parser.add_argument("input_dir", type=str,
                        help="Directory containing SQL files")
    parser.add_argument("output_dir", type=str,
                        help="Directory to save Excel files")
    args = parser.parse_args()
    convert_directory_of_queries(args.input_dir, args.output_dir)


if __name__ == "__main__":
    convert_sql_to_xlsx_from_cli()

# Close the cursor and connection
cur.close()
conn.close()
