import pandas as pd
import os
import sys

# ----------------------- Configuration ----------------------- #

# Define the path to your CSV file
CSV_FILE_PATH = 'C:/Users/nicho/vscode/vscodeprojects/GenerateSQLData/Player.csv'  # Update with your CSV path

# Define the output SQL file path
OUTPUT_SQL_FILE = 'C:/Users/nicho/vscode/vscodeprojects/GenerateSQLData/insert_players.sql'  # Desired SQL output path

# Define your MySQL table name
TABLE_NAME = 'Players'  # Your MySQL table name

# ----------------------- Functions ----------------------- #

def read_csv(csv_path):
    """Reads the CSV file and returns a pandas DataFrame."""
    try:
        df = pd.read_csv(csv_path)
        print(f"Successfully read CSV file: {csv_path}")
        return df
    except FileNotFoundError:
        print(f"Error: The file '{csv_path}' was not found.")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{csv_path}' is empty.")
        sys.exit(1)
    except pd.errors.ParserError:
        print(f"Error: The file '{csv_path}' does not appear to be in CSV format.")
        sys.exit(1)

def validate_columns(df, required_columns):
    """Validates that the DataFrame contains the required columns."""
    if not set(required_columns).issubset(df.columns):
        missing = set(required_columns) - set(df.columns)
        print(f"Error: The following required columns are missing from the CSV: {', '.join(missing)}")
        sys.exit(1)
    print("All required columns are present in the CSV.")

def escape_sql(value):
    """Escapes single quotes in string values for SQL."""
    if isinstance(value, str):
        return value.replace("'", "''")
    return value

def format_value(value, data_type):
    """Formats the value based on its data type for SQL."""
    if pd.isnull(value):
        return 'NULL'
    if data_type == 'string':
        return f"'{escape_sql(str(value))}'"
    elif data_type == 'date':
        return f"'{escape_sql(str(value))}'"  # Ensure date is in 'YYYY-MM-DD' format
    else:
        return str(int(value))  # Assuming numeric types are integers

def generate_insert_statement(df, table_name):
    """Generates an INSERT INTO statement with all the tuples."""
    insert_statement = f"INSERT INTO {table_name} (PlayerID, FirstName, LastName, DateOfBirth, Nationality, Height, Weight, TeamID, PositionID) VALUES\n"
    tuples = []

    # Define the data types for each column
    column_types = {
        'PlayerID': 'int',
        'FirstName': 'string',
        'LastName': 'string',
        'DateOfBirth': 'date',
        'Nationality': 'string',
        'Height': 'int',
        'Weight': 'int',
        'TeamID': 'int',
        'PositionID': 'int'
    }

    # Iterate over each row to create tuple strings
    for index, row in df.iterrows():
        try:
            player_id = format_value(row['PlayerID'], column_types['PlayerID'])
            first_name = format_value(row['FirstName'], column_types['FirstName'])
            last_name = format_value(row['LastName'], column_types['LastName'])
            date_of_birth = format_value(row['DateOfBirth'], column_types['DateOfBirth'])
            nationality = format_value(row['Nationality'], column_types['Nationality'])
            height = format_value(row['Height'], column_types['Height'])
            weight = format_value(row['Weight'], column_types['Weight'])
            team_id = format_value(row['TeamID'], column_types['TeamID'])
            position_id = format_value(row['PositionID'], column_types['PositionID'])

            # Create the tuple string
            tuple_str = f"({player_id},{first_name},{last_name},{date_of_birth},{nationality},{height},{weight},{team_id},{position_id})"
            tuples.append(tuple_str)
        except Exception as e:
            print(f"Error processing row {index}: {e}")
            sys.exit(1)

    # Join all tuples with commas, ensuring the last tuple does not have a trailing comma
    tuples_with_commas = ",\n".join(tuples)
    insert_statement += tuples_with_commas + ";"

    return insert_statement

def write_sql_file(sql_content, output_path):
    """Writes the SQL content to the specified file."""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(sql_content)
        print(f"SQL insert script has been generated successfully at '{output_path}'.")
    except Exception as e:
        print(f"Error writing to SQL file: {e}")
        sys.exit(1)

# ----------------------- Main Execution ----------------------- #

def main():
    # Define required columns
    required_columns = ['PlayerID', 'FirstName', 'LastName', 'DateOfBirth', 'Nationality', 'Height', 'Weight', 'TeamID', 'PositionID']

    # Read the CSV file
    df = read_csv(CSV_FILE_PATH)

    # Validate the required columns
    validate_columns(df, required_columns)

    # Generate the INSERT statement
    insert_sql = generate_insert_statement(df, TABLE_NAME)

    # Write the INSERT statement to the SQL file
    write_sql_file(insert_sql, OUTPUT_SQL_FILE)

if __name__ == "__main__":
    main()
