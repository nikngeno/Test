import pandas as pd
import random

# Constants
NUM_TEAMS = 32
POSITIONS = {
    'G': 1,   # Goalkeeper
    'LD': 2,  # Left Defense
    'RD': 3,  # Right Defense
    'C': 4,   # Center
    'LW': 5,  # Left Wing
    'RW': 6   # Right Wing
}

# Number of players per position per team
INITIAL_POSITIONS = {
    'G': 2,
    'LD': 3,
    'RD': 3,
    'C': 3,
    'LW': 3,
    'RW': 3
}

# Total initial assignments: 32 teams * 17 players = 544 players
TOTAL_INITIAL_ASSIGNMENTS = NUM_TEAMS * sum(INITIAL_POSITIONS.values())  # 544

# Load players data
players_df = pd.read_csv('players.csv')

# Verify that there are enough players
if len(players_df) < 544:
    raise ValueError(f"Not enough players to assign initial positions. Required: 544, Available: {len(players_df)}")

# Shuffle the DataFrame to ensure random assignment
players_df = players_df.sample(frac=1, random_state=42).reset_index(drop=True)

# Initialize a dictionary to keep track of team assignments
# Each team will have a list of position IDs assigned
team_assignments = {team_id: [] for team_id in range(1, NUM_TEAMS + 1)}

# Initialize team list
team_list = list(range(1, NUM_TEAMS + 1))

# Assign initial positions per team
player_index = 0  # Tracks the current player to assign

for team_id in team_list:
    for position, count in INITIAL_POSITIONS.items():
        for _ in range(count):
            if player_index >= len(players_df):
                raise Exception("Not enough players to assign initial positions.")
            # Assign TeamID and PositionID
            players_df.at[player_index, 'TeamID'] = team_id
            players_df.at[player_index, 'PositionID'] = POSITIONS[position]
            # Update team assignments
            team_assignments[team_id].append(POSITIONS[position])
            player_index += 1

# Calculate remaining players
remaining_players = len(players_df) - player_index  # 950 - 544 = 406

# Distribute remaining players evenly across teams
# Each team gets floor(406 / 32) = 12 extra players
# Remaining: 406 % 32 = 22 teams get 1 additional player
extra_players_per_team = remaining_players // NUM_TEAMS  # 12
extra_players_remainder = remaining_players % NUM_TEAMS  # 22

# Define position distribution for extra players
# To maintain balance, cycle through positions [LD, RD, C, LW, RW]
EXTRA_POSITIONS = ['LD', 'RD', 'C', 'LW', 'RW']

# Assign extra players
for idx, team_id in enumerate(team_list):
    # Determine number of extra players for this team
    num_extra = extra_players_per_team + (1 if idx < extra_players_remainder else 0)
    for _ in range(num_extra):
        if player_index >= len(players_df):
            raise Exception("Not enough players to assign extra positions.")
        # Assign TeamID
        players_df.at[player_index, 'TeamID'] = team_id
        # Assign PositionID in a round-robin fashion to maintain balance
        position = EXTRA_POSITIONS[player_index % len(EXTRA_POSITIONS)]
        players_df.at[player_index, 'PositionID'] = POSITIONS[position]
        # Update team assignments
        team_assignments[team_id].append(POSITIONS[position])
        player_index += 1

# Assign any remaining players (if any)
while player_index < len(players_df):
    team_id = random.choice(team_list)
    position = random.choice(EXTRA_POSITIONS)
    players_df.at[player_index, 'TeamID'] = team_id
    players_df.at[player_index, 'PositionID'] = POSITIONS[position]
    team_assignments[team_id].append(POSITIONS[position])
    player_index += 1

# Final Checks

# 1. Ensure each team has exactly 2 G, 3 LD, 3 RD, 3 C, 3 LW, 3 RW in initial assignment
for team_id in team_list:
    team_data = players_df[players_df['TeamID'] == team_id]
    for position, count in INITIAL_POSITIONS.items():
        actual_count = len(team_data[team_data['PositionID'] == POSITIONS[position]])
        if actual_count < count:
            raise Exception(f"Team {team_id} has {actual_count} players for position {position}, expected {count}.")
    # Ensure at least 15 players per team
    if len(team_data) < 15:
        raise Exception(f"Team {team_id} has only {len(team_data)} players, minimum required is 15.")

# 2. Ensure all players have been assigned
unassigned_players = players_df[players_df['TeamID'].isnull() | players_df['PositionID'].isnull()]
if not unassigned_players.empty:
    raise Exception("There are unassigned players remaining.")

# 3. Verify total number of players
assert len(players_df) == 950, f"Total players should be 950, but got {len(players_df)}"

# Save the updated DataFrame to a new CSV
players_df.to_csv('players_updated.csv', index=False)

print("Player assignments completed successfully. 'players_updated.csv' has been created.")
