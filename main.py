# Define the URL of the YouTube playlist
# List of playlist URLs
playlist_urls = ["https://www.youtube.com/playlist?list=PLe0U7sHuld_qIILgg-2ESRCPWu-WBalFJ",
"https://www.youtube.com/playlist?list=PLAeu18HndGgBR-QLw8b8Wzp0gLiVfCS7n",
"https://www.youtube.com/playlist?list=PLe0U7sHuld_pZllkKAojENaQLYeOWfED7",
"https://www.youtube.com/playlist?list=PLOlK8ytA0MgjYGVrz0hS4w3UPQ1-VV2uX",
"https://www.youtube.com/playlist?list=PLqnslRFeH2UqLwzS0AwKDKLrpYBKzLBy2",
"https://www.youtube.com/playlist?list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc",
"https://www.youtube.com/playlist?list=PLUOa-qvvZolCoiF8CuqCyVU9tG2v8cjE6",
"https://www.youtube.com/playlist?list=PLUkh9m2BorqnKWu0g5ZUps_CbQ-JGtbI9",
"https://www.youtube.com/playlist?list=PLAeu18HndGgBR-QLw8b8Wzp0gLiVfCS7n",
"https://www.youtube.com/playlist?list=PLAeu18HndGgDAWJOAPaqARiMkMJ1u-EOm",
"https://www.youtube.com/playlist?list=PLAeu18HndGgD-btpZ7rb358WGAHH1-ZcU",
"https://www.youtube.com/playlist?list=PLAeu18HndGgB-KWCMyZCKCgZbpik2I9A3"]

video_details =list(map(get_runtime_and_title, playlist_urls))
video_details = pd.DataFrame(video_details)
video_details = video_details.assign(Start_Date=None, Start_Time=None, Time_to_Spend=None)
video_details

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


video_details.to_csv("Plant to Learn.csv", index=False)

video_details = pd.read_csv("Plant to Learn.csv")

video_details.sort_values(by='Start Date')
# Display the DataFrame as an interactive table
qgrid.enable()
qgrid_widget = qgrid.show_grid(video_details, grid_options={'editable': True})
qgrid_widget
