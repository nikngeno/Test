import pandas as pd
import os

# Configuration
CSV_FILE_PATH = 'C:/Users/nicho/vscode/vscodeprojects/GenerateSQLData/team_stats.csv'  # Path to your CSV file
OUTPUT_SQL_FILE = 'C:/Users/nicho/vscode/vscodeprojects/GenerateSQLData/insert_team_stats.sql'  # Desired SQL output path
TABLE_NAME = 'TeamStats'  # Your MySQL table name

def read_csv(csv_path):
    """Reads the CSV file and returns a pandas DataFrame."""
    try:
        df = pd.read_csv(csv_path)
        print(f"Successfully read CSV file: {csv_path}")
        return df
    except FileNotFoundError:
        print(f"Error: The file '{csv_path}' was not found.")
        exit(1)
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{csv_path}' is empty.")
        exit(1)
    except pd.errors.ParserError:
        print(f"Error: The file '{csv_path}' does not appear to be in CSV format.")
        exit(1)

def validate_columns(df, required_columns):
    """Validates that the DataFrame contains the required columns."""
    if not set(required_columns).issubset(df.columns):
        missing = set(required_columns) - set(df.columns)
        print(f"Error: The following required columns are missing from the CSV: {', '.join(missing)}")
        exit(1)
    print("All required columns are present in the CSV.")

def escape_value(value):
    """Escapes single quotes in string values for SQL."""
    if isinstance(value, str):
        return value.replace("'", "''")
    return value

def generate_insert_statement(df, table_name):
    """Generates an INSERT INTO statement with all the tuples."""
    insert_statement = f"INSERT INTO {table_name} (TeamStatsID, TeamID, SeasonID, GoalsFor, GoalsAgainst, ShotsOnGoal) VALUES\n"
    tuples = []

    # Iterate over each row to create tuple strings
    for index, row in df.iterrows():
        team_stats_id = int(row['TeamStatsID'])
        team_id = int(row['TeamID'])
        season_id = int(row['SeasonID'])
        goals_for = int(row['GoalsFor'])
        goals_against = int(row['GoalsAgainst'])
        shots_on_goal = int(row['ShotsOnGoal'])

        # Create the tuple string
        tuple_str = f"({team_stats_id},{team_id},{season_id},{goals_for},{goals_against},{shots_on_goal})"
        tuples.append(tuple_str)

    # Join all tuples with commas, except the last one
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
        exit(1)

def main():
    # Define required columns
    required_columns = ['TeamStatsID', 'TeamID', 'SeasonID', 'GoalsFor', 'GoalsAgainst', 'ShotsOnGoal']

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
