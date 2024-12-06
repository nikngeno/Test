import pandas as pd
import random

# Constants
NUM_TEAMS = 32
POSITIONS = {
    1: 'G',    # Goalkeeper
    2: 'LD',   # Left Defense
    3: 'RD',   # Right Defense
    4: 'C',    # Center
    5: 'LW',   # Left Wing
    6: 'RW'    # Right Wing
}

# Load existing data
players_df = pd.read_csv('players_updated.csv')  # Updated players with TeamID and PositionID
games_df = pd.read_csv('games.csv')             # Existing games data

# Verify necessary columns exist
required_player_columns = {'PlayerID', 'TeamID', 'PositionID'}
required_game_columns = {'GameID', 'SeasonID', 'Date', 'HomeTeamID', 'AwayTeamID', 'VenueID', 'HomeTeamScore', 'AwayTeamScore', 'Overtime', 'Shootout'}

if not required_player_columns.issubset(players_df.columns):
    raise Exception(f"players_updated.csv must contain columns: {required_player_columns}")

if not required_game_columns.issubset(games_df.columns):
    raise Exception(f"games.csv must contain columns: {required_game_columns}")

# Initialize list to hold PlayerStats records
player_stats_records = []

# Function to generate random stats
def generate_stats(position):
    # Define possible ranges based on position
    if position == 'G':
        goals = random.randint(0, 1)        # Goalkeepers rarely score
        assists = random.randint(0, 1)
        shots_on_goal = random.randint(0, 3)
        blocked_shots = random.randint(0, 5)
        time_on_ice = random.randint(20, 35) # Typically more time on ice
    elif position in ['LD', 'RD']:
        goals = random.randint(0, 3)
        assists = random.randint(0, 4)
        shots_on_goal = random.randint(0, 5)
        blocked_shots = random.randint(0, 7)
        time_on_ice = random.randint(15, 25)
    elif position in ['C', 'LW', 'RW']:
        goals = random.randint(0, 5)
        assists = random.randint(0, 6)
        shots_on_goal = random.randint(0, 7)
        blocked_shots = random.randint(0, 5)
        time_on_ice = random.randint(10, 20)
    else:
        goals = assists = shots_on_goal = blocked_shots = time_on_ice = 0
    
    return goals, assists, shots_on_goal, blocked_shots, time_on_ice

# Iterate over each game to assign stats to players
for index, game in games_df.iterrows():
    game_id = game['GameID']
    season_id = game['SeasonID']
    home_team = game['HomeTeamID']
    away_team = game['AwayTeamID']
    
    # Get players from home and away teams
    home_players = players_df[players_df['TeamID'] == home_team]
    away_players = players_df[players_df['TeamID'] == away_team]
    
    # Combine players
    game_players = pd.concat([home_players, away_players])
    
    for _, player in game_players.iterrows():
        player_id = player['PlayerID']
        position_id = player['PositionID']
        position = POSITIONS.get(position_id, 'Unknown')
        
        # Generate stats based on position
        goals, assists, shots_on_goal, blocked_shots, time_on_ice = generate_stats(position)
        
        # Append to records
        player_stats_records.append({
            'PlayerID': player_id,
            'GameID': game_id,
            'Goals': goals,
            'Assists': assists,
            'ShotsOnGoal': shots_on_goal,
            'BlockedShots': blocked_shots,
            'TimeOnIce': time_on_ice
        })

# Create DataFrame from records
player_stats_df = pd.DataFrame(player_stats_records)

# To prevent excessively large CSV, consider sampling or splitting
# For demonstration, we'll export the entire DataFrame
player_stats_df.to_csv('player_stats.csv', index=False)

print("Player statistics data generated successfully as 'player_stats.csv'.")
