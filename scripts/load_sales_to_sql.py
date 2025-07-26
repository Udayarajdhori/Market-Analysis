import pandas as pd
from sqlalchemy import create_engine

# Load CSV data
sales_df = pd.read_csv('data/vgsales.csv')

# Create SQLite engine
engine = create_engine('sqlite:///data/sales.db')

# Write data to SQL table
sales_df.to_sql('sales', con=engine, if_exists='replace', index=False)

print('Sales data loaded into SQLite database.') 