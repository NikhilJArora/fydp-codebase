import pandas as pd
import os

update_path = '/Users/nikhilarora/data/fydp/pi_data/output.csv'

df = pd.read_csv(update_path)

df.loc[2,'state'] = False

df.to_csv(update_path, index=False)
