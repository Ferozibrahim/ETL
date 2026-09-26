import pandas as pd
import numpy as np
import random
import os
from datetime import datetime, timedelta

# 1. Setup basic parameters for our mock data
num_rows = 500
policy_types = ['Auto', 'Home', 'Health', 'Life']
start_date = datetime(2025, 1, 1)
data = []

# 2. Loop 500 times to create 500 unique claims
for i in range(1, num_rows + 1):
    
    # Generate a standard Claim_ID (e.g., CLM-001, CLM-002)
    claim_id = f"CLM-{i:03d}"
    
    # Generate Policy_Type with a 5% chance of being missing (NaN)
    if random.random() < 0.05:
        policy = np.nan
    else:
        policy = random.choice(policy_types)
        
    # Generate Claim_Amount with messiness
    if random.random() < 0.05:
        amount = np.nan # 5% chance of missing amount
    else:
        # Generate a random float between 500 and 50,000
        raw_amount = round(random.uniform(500.0, 50000.0), 2)
        
        # 20% chance to format it as a messy string with a '$' and commas
        if random.random() < 0.20:
            amount = f"${raw_amount:,.2f}"
        else:
            amount = raw_amount
            
    # Generate Claim_Date with inconsistent formats
    random_days = random.randint(0, 365)
    claim_date = start_date + timedelta(days=random_days)
    
    # Randomly pick one of three date formats
    format_choice = random.random()
    if format_choice < 0.33:
        date_str = claim_date.strftime("%Y-%m-%d") # Standard (e.g., 2025-04-15)
    elif format_choice < 0.66:
        date_str = claim_date.strftime("%d/%m/%Y") # UK format (e.g., 15/04/2025)
    else:
        date_str = claim_date.strftime("%B %d, %Y") # Text format (e.g., April 15, 2025)
        
    # 5% chance of missing date
    if random.random() < 0.05:
        date_str = np.nan

    # 3. Add this specific claim to our master list
    data.append([claim_id, policy, amount, date_str])

# 4. Convert our list into a Pandas DataFrame
df = pd.DataFrame(data, columns=['Claim_ID', 'Policy_Type', 'Claim_Amount', 'Claim_Date'])

# 5. Create the 'data' folder if it doesn't exist, and save the CSV
os.makedirs('data', exist_ok=True)
df.to_csv('data/raw_claims.csv', index=False)

print("Success! Messy dataset generated at 'data/raw_claims.csv'")