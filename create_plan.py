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
