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


def create_calender(video_details):
    
    # Initialize the iCalendar
    cal = Calendar()

    for _,ROW in video_details.iterrows():
        
        # Define a start date and time
        start_date = pd.to_datetime(ROW['Start Date'] + ' ' + ROW['Start Time']) 
        
        playlist_data = create_video_data(ROW['Video Link'])
        if ROW['Title'] == 'hg':
            sort_by_runtime= True
        else:
            sort_by_runtime=False
            
        df = create_learning_group(playlist_data,int(ROW['Time to Spend']),sort_by_runtime)

        # Group the DataFrame by 'Category'
        df_dict = dict(iter(df.groupby('Group')))
        
        for group, dft in df_dict.items():
        # Calculate event duration from Run Time
            duration = timedelta(minutes=int(ROW['Time to Spend']))

            # Skip weekends (Saturday and Sunday)
            while start_date.weekday() >= 5:  # 5 and 6 correspond to Saturday and Sunday
                start_date += timedelta(days=1)

            # Create an event for each row
            event = Event()
            event.add('summary',ROW['Title']+ group)
            event.add('dtstart', start_date)
            event.add('dtend', start_date + duration)

            # Combine Video Link and Description in the description field
            event.add('description', dft)

            cal.add_component(event)

            # Increment start date for the next event
            start_date += timedelta(days=1)


    return cal


from support_functions import create_calender
from create_runtime_and_video_data import get_runtime_and_title


video_details =list(map(get_runtime_and_title, playlist_urls))
video_details = pd.DataFrame(video_details)
video_details = video_details.assign(Start_Date=None, Start_Time=None, Time_to_Spend=None)

# Create empty columns for Start Date, Start Time, and Time to Spend
video_details['Start Date'] = ""
video_details['Start Time'] = ""
video_details['Time to Spend'] = ""

# Iterate through each row to get user input
for index, row in video_details.iterrows():
    print(f"Row {index + 1}: {row['Title']}")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    start_time = input("Enter start time (HH:MM:SS): ")
    time_to_spend = input("Enter time to spend (HH:MM:SS): ")
    
    video_details.at[index, 'Start Date'] = start_date
    video_details.at[index, 'Start Time'] = start_time
    video_details.at[index, 'Time to Spend'] = time_to_spend



# Display the DataFrame as an interactive table
qgrid.enable()
qgrid_widget = qgrid.show_grid(video_details, grid_options={'editable': True})
qgrid_widget
