import pandas as pd
import os
import sys

# ----------------------- Configuration ----------------------- #

# Define the path to your CSV file
CSV_FILE_PATH = 'C:/Users/nicho/vscode/vscodeprojects/GenerateSQLData/games.csv'  # Update with your CSV path

# Define the output SQL file path
OUTPUT_SQL_FILE = 'C:/Users/nicho/vscode/vscodeprojects/GenerateSQLData/insert_games.sql'  # Desired SQL output path

# Define your SQL Server table name
TABLE_NAME = 'Games'  # Ensure this matches your actual table name

# Define the maximum number of rows per INSERT statement
MAX_ROWS_PER_INSERT = 1000

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
        # Ensure date is in 'YYYY-MM-DD' format
        try:
            formatted_date = pd.to_datetime(value).strftime('%Y-%m-%d')
            return f"'{formatted_date}'"
        except Exception as e:
            print(f"Error formatting date value '{value}': {e}")
            sys.exit(1)
    elif data_type == 'bit':
        # Convert boolean-like values to 1 or 0
        if isinstance(value, bool):
            return '1' if value else '0'
        elif isinstance(value, (int, float)):
            return '1' if value else '0'
        elif isinstance(value, str):
            value_lower = value.strip().lower()
            if value_lower in ['1', 'yes', 'true']:
                return '1'
            elif value_lower in ['0', 'no', 'false']:
                return '0'
            else:
                print(f"Error: Invalid bit value '{value}'. Expected 1/0, Yes/No, True/False.")
                sys.exit(1)
        else:
            print(f"Error: Unsupported bit value type: {type(value)}")
            sys.exit(1)
    else:
        return str(int(value))  # Assuming numeric types are integers

def generate_insert_statements(df, table_name, max_rows):
    """Generates multiple INSERT INTO statements with batches of rows."""
    insert_statements = []
    total_rows = df.shape[0]
    num_batches = (total_rows // max_rows) + (1 if total_rows % max_rows != 0 else 0)
    
    print(f"Total rows to insert: {total_rows}")
    print(f"Generating {num_batches} INSERT statements with up to {max_rows} rows each.")
    
    for batch_num in range(num_batches):
        start_idx = batch_num * max_rows
        end_idx = min(start_idx + max_rows, total_rows)
        batch_df = df.iloc[start_idx:end_idx]
        
        insert_statement = f"INSERT INTO {table_name} (GameID, SeasonID, GameDate, HomeTeamID, AwayTeamID, VenueID, HomeTeamScore, AwayTeamScore, Overtime, Shootout) VALUES\n"
        tuples = []
        
        # Define the data types for each column
        column_types = {
            'GameID': 'int',
            'SeasonID': 'int',
            'GameDate': 'date',
            'HomeTeamID': 'int',
            'AwayTeamID': 'int',
            'VenueID': 'int',
            'HomeTeamScore': 'int',
            'AwayTeamScore': 'int',
            'Overtime': 'bit',
            'Shootout': 'bit'
        }
        
        # Iterate over each row to create tuple strings
        for index, row in batch_df.iterrows():
            try:
                game_id = format_value(row['GameID'], column_types['GameID'])
                season_id = format_value(row['SeasonID'], column_types['SeasonID'])
                game_date = format_value(row['GameDate'], column_types['GameDate'])
                home_team_id = format_value(row['HomeTeamID'], column_types['HomeTeamID'])
                away_team_id = format_value(row['AwayTeamID'], column_types['AwayTeamID'])
                venue_id = format_value(row['VenueID'], column_types['VenueID'])
                home_team_score = format_value(row['HomeTeamScore'], column_types['HomeTeamScore'])
                away_team_score = format_value(row['AwayTeamScore'], column_types['AwayTeamScore'])
                overtime = format_value(row['Overtime'], column_types['Overtime'])
                shootout = format_value(row['Shootout'], column_types['Shootout'])
    
                # Create the tuple string
                tuple_str = f"({game_id},{season_id},{game_date},{home_team_id},{away_team_id},{venue_id},{home_team_score},{away_team_score},{overtime},{shootout})"
                tuples.append(tuple_str)
            except Exception as e:
                print(f"Error processing row {index}: {e}")
                sys.exit(1)
        
        # Join all tuples with commas
        tuples_with_commas = ",\n".join(tuples)
        insert_statement += tuples_with_commas + ";"
        
        insert_statements.append(insert_statement)
        print(f"Generated INSERT statement for rows {start_idx + 1} to {end_idx}.")
    
    return insert_statements

def write_sql_file(insert_statements, output_path):
    """Writes the INSERT statements to the specified SQL file."""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            for statement in insert_statements:
                f.write(statement + "\n\n")  # Separate statements by two newlines for readability
        print(f"SQL insert script has been generated successfully at '{output_path}'.")
    except Exception as e:
        print(f"Error writing to SQL file: {e}")
        sys.exit(1)

# ----------------------- Main Execution ----------------------- #

def main():
    # Define required columns
    required_columns = ['GameID', 'SeasonID', 'GameDate', 'HomeTeamID', 'AwayTeamID', 'VenueID', 'HomeTeamScore', 'AwayTeamScore', 'Overtime', 'Shootout']
    
    # Read the CSV file
    df = read_csv(CSV_FILE_PATH)
    
    # Validate the required columns
    validate_columns(df, required_columns)
    
    # Generate the INSERT statements with batching
    insert_statements = generate_insert_statements(df, TABLE_NAME, MAX_ROWS_PER_INSERT)
    
    # Write the INSERT statements to the SQL file
    write_sql_file(insert_statements, OUTPUT_SQL_FILE)

if __name__ == "__main__":
    main()
