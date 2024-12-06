import pandas as pd
import random

# Define the positions mapping
POSITIONS = {
    1: 'G',    # Goalkeeper
    2: 'LD',   # Left Defense
    3: 'RD',   # Right Defense
    4: 'C',    # Center
    5: 'LW',   # Left Wing
    6: 'RW'    # Right Wing
}

# Load existing data
players_df = pd.read_csv('players_updated.csv')  # Ensure this file includes PlayerID, TeamID, PositionID
games_df = pd.read_csv('games.csv')             # Ensure this file includes SeasonID

# Verify necessary columns exist
required_player_columns = {'PlayerID', 'TeamID', 'PositionID'}
required_game_columns = {'GameID', 'SeasonID', 'Date', 'HomeTeamID', 'AwayTeamID', 'VenueID', 
                         'HomeTeamScore', 'AwayTeamScore', 'Overtime', 'Shootout'}

if not required_player_columns.issubset(players_df.columns):
    raise Exception(f"players_updated.csv must contain columns: {required_player_columns}")

if not required_game_columns.issubset(games_df.columns):
    raise Exception(f"games.csv must contain columns: {required_game_columns}")

# Extract unique seasons from games_df
seasons = games_df['SeasonID'].unique()

# Initialize list to hold PlayerSeasonStats records
player_season_stats_records = []

# Function to generate randomized season stats within constraints
def generate_season_stats():
    goals = random.randint(1, 50)            # Goals between 1 and 50
    assists = random.randint(1, 50)          # Assists between 1 and 50
    shots_on_goal = random.randint(0, 80)    # Shots on goal up to 80
    blocked_shots = random.randint(0, 80)    # Blocked shots up to 80
    time_on_ice = random.randint(1000, 3840) # Time on ice up to 3840 mins
    return goals, assists, shots_on_goal, blocked_shots, time_on_ice

# Iterate over each player and each season to assign random stats
for _, player in players_df.iterrows():
    player_id = player['PlayerID']
    position_id = player['PositionID']
    position = POSITIONS.get(position_id, 'Unknown')
    
    for season in seasons:
        # Optionally, you can introduce a participation probability
        # For simplicity, we'll assume every player participates in every season
        goals, assists, shots_on_goal, blocked_shots, time_on_ice = generate_season_stats()
        
        # Append the record
        player_season_stats_records.append({
            'PlayerID': player_id,
            'SeasonID': season,
            'Goals': goals,
            'Assists': assists,
            'ShotsOnGoal': shots_on_goal,
            'BlockedShots': blocked_shots,
            'TimeOnIce': time_on_ice
        })

# Create DataFrame from records
player_season_stats_df = pd.DataFrame(player_season_stats_records)

# Optionally, you can introduce filters such as excluding players with zero participation
# For this script, since we assigned stats to all player-season combinations, no need for filtering

# Save to CSV
player_season_stats_df.to_csv('player_season_stats.csv', index=False)

print("Season-wise player statistics data generated successfully as 'player_season_stats.csv'.")
