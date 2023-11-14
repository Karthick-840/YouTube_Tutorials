import pandas as pd
from datetime import timedelta
import math

def create_learning_group(df,allocated_time_in_min,sort_by_runtime):

    # Create a 'Group' column in the DataFrame
    df[['SortKey','Group']] = 0,''
    # Convert the 'Run Time' column to timedelta
    df['Run Time'] = pd.to_timedelta(df['Run Time'])
    if sort_by_runtime:
        df = df.sort_values(by='Run Time')
    # Initialize variables
    total_time = timedelta()
    part_number = 1
    start_index = 1

    # Create an empty list to store the rows to append
    rows_to_append = []

    # Iterate through the DataFrame and add rows
    for index, row in df.iterrows():
        if row['Run Time'] > timedelta(minutes=allocated_time_in_min):
            # Calculate the number of parts needed
            num_parts = float(row['Run Time'].total_seconds() / (allocated_time_in_min * 60))
            # Always spend 20% more time than the dedicated one for the video

            for part in range(int(math.ceil(num_parts*1.3))):
                new_row = row.copy()
                new_row['SortKey'] = part_number
                rows_to_append.append(new_row)
                part_number += 1
            # Remove the original row from df
            df = df.drop(index)
        else:
            if total_time + row['Run Time'] <= timedelta(minutes=allocated_time_in_min):
                total_time += row['Run Time']
                df.at[index, 'SortKey'] = part_number
            else:
                total_time = row['Run Time']
                part_number += 1
                df.at[index, 'SortKey'] = part_number

    # Append the duplicated rows to the DataFrame
    df = pd.concat([df, pd.DataFrame(rows_to_append)], ignore_index=True)

    # Sort the DataFrame by the 'SortKey' column
    df = df.sort_values(by='SortKey')
    df['SortKey'] = df['SortKey'].diff().eq(1).cumsum() + df['SortKey'].iat[0]
    df['Group'] = 'Part - ' + df['SortKey'].astype(str)
    # Reset the index
    df.reset_index(drop=True, inplace=True)
    # Drop the temporary 'SortKey' column
    df = df.drop(columns='SortKey')

    return df
