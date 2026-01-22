# Create + Inspect + Basic Cleaning
#
# - Create a DataFrame from a dict (at least 10 rows).
# - Show head(), info(), describe(include="all") .
# - Convert a date column to datetime.
# - Trim whitespace from string columns.
#

import pandas as pd

data = {
    "Name": ["  Aaron ", "Piyush  ", "   Prerana", "  Aniket", " Dhanesh", " Rohit", " Yash ", " Arin", " Yuvraj", "   Roshan"],
    "D.O.B.": ['15-01-2003', '24-12-2003', '20-01-2004', '01-02-2003', '04-05-2002', '15-01-2003', '24-12-2003', '20-01-2004', '01-02-2003', '04-05-2002']
}

if __name__ == '__main__':
    df = pd.DataFrame.from_dict(data)

    df["Name"] = df["Name"].str.strip()
    df["D.O.B."] = pd.to_datetime(df["D.O.B."], format="%d-%m-%Y")
    
    print(f'Head:\n{df.head()}')

    print("Info")
    df.info()
        
    print(f'Describe:\n{df.describe(include='all')}')