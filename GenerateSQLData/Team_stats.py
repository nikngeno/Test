import pandas as pd
import random
import os

# Define the path to the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define file paths
teams_file = os.path.join(script_dir, 'teams.csv')
seasons_file = os.path.join(script_dir, 'seasons.csv')
output_file = os.path.join(script_dir, 'team_stats.csv')

# Load existing data
try:
    teams_df = pd.read_csv(teams_file)       # Ensure this file includes TeamID and TeamName
except FileNotFoundError:
    raise FileNotFoundError(f"'teams.csv' not found in {script_dir}. Please ensure the file exists.")

try:
    seasons_df = pd.read_csv(seasons_file)   # Ensure this file includes SeasonID and SeasonName or Year
except FileNotFoundError:
    raise FileNotFoundError(f"'seasons.csv' not found in {script_dir}. Please ensure the file exists.")

# Verify necessary columns exist
required_team_columns = {'TeamID', 'TeamName'}
required_season_columns = {'SeasonID', 'SeasonName'}

if not required_team_columns.issubset(teams_df.columns):
    raise Exception(f"'teams.csv' must contain columns: {required_team_columns}")

if not required_season_columns.issubset(seasons_df.columns):
    raise Exception(f"'seasons.csv' must contain columns: {required_season_columns}")

# Initialize list to hold TeamStats records
team_stats_records = []

# Function to generate randomized team stats within constraints
def generate_team_stats():
    # Define realistic ranges based on typical hockey statistics
    shots_on_goal = random.randint(2083, 2500)       # Shots on goal in a season (min adjusted to 2083 for GoalsFor >= 800)
    
    # Calculate GoalsFor based on a ~40% conversion rate of ShotsOnGoal
    # Introduce variation between 38% to 42%
    conversion_rate = random.uniform(0.38, 0.42)
    goals_for = int(shots_on_goal * conversion_rate)
    
    # Calculate GoalsAgainst based on GoalsFor, ensuring GoalsAgainst <= 40% GoalsFor and >=30% GoalsFor
    goals_against_min = int(goals_for * 0.3)
    goals_against_max = int(goals_for * 0.4)
    
    # Ensure goals_against_min does not exceed goals_against_max
    if goals_against_min > goals_against_max:
        goals_against_min = goals_against_max
    
    goals_against = random.randint(goals_against_min, goals_against_max)
    
    return goals_against, shots_on_goal, goals_for

# Iterate over each team and each season to assign random stats
for _, team in teams_df.iterrows():
    team_id = team['TeamID']
    team_name = team['TeamName']
    
    for _, season in seasons_df.iterrows():
        season_id = season['SeasonID']
        season_name = season['SeasonName']
        
        # Generate stats
        goals_against, shots_on_goal, goals_for = generate_team_stats()
        
        # Append the record
        team_stats_records.append({
            'TeamID': team_id,
            'SeasonID': season_id,
            'GoalsAgainst': goals_against,
            'ShotsOnGoal': shots_on_goal,
            'GoalsFor': goals_for
        })

# Create DataFrame from records
team_stats_df = pd.DataFrame(team_stats_records)

# Optional: Data Validation
# Ensure ShotsOnGoal is within 2083-2500
assert team_stats_df['ShotsOnGoal'].between(2083, 2500).all(), "ShotsOnGoal out of range (2083-2500)!"

# Ensure GoalsFor is within 800-1050
assert team_stats_df['GoalsFor'].between(800, 1050).all(), "GoalsFor out of expected range (800-1050)!"

# Validate that GoalsAgainst is between 30% and 40% of GoalsFor
for index, row in team_stats_df.iterrows():
    goals_for = row['GoalsFor']
    goals_against = row['GoalsAgainst']
    expected_min = int(goals_for * 0.3)
    expected_max = int(goals_for * 0.4)
    
    if not (expected_min <= goals_against <= expected_max):
        raise AssertionError(f"Row {index} - GoalsAgainst ({goals_against}) not between 30% ({expected_min}) and 40% ({expected_max}) of GoalsFor ({goals_for})")

# Save to CSV
team_stats_df.to_csv(output_file, index=False)

print(f"Season-wise team statistics data generated successfully as '{output_file}'.")
