from support_functions import convert_seconds_to_hms, extract_keywords
from icalendar import Calendar, Event
from datetime import datetime, timedelta
from pytube import YouTube, Playlist
import pandas as pd



def get_runtime_and_title(url):
    if 'playlist' in url:
        playlist = Playlist(url)
        total_runtime = 0
        video_count = 0
        for video in playlist.videos:
            total_runtime += video.length
            video_count += 1
            video_thumbnails.append(video.thumbnail_url)

        average_playtime = total_runtime / video_count if video_count > 0 else 0

        video_data = {
            "Title": playlist.title,
            "Average Playtime": convert_seconds_to_hms(average_playtime),
            "Total Runtime": convert_seconds_to_hms(total_runtime),
            "Video Count": video_count,
            "Video Thumbnails": video_thumbnails,
            "Video Link": url
        }

    else:
        video = YouTube(url)
        title = video.title
        runtime = video.length
        video_data = {"Title": title, "Run Time": convert_seconds_to_hms(runtime),"Video Count":1,"Video Link": url}
   
    return video_data


def create_video_data(playlist_url):
    
    playlist = Playlist(playlist_url)
    # Create an empty DataFrame to store the video data
    df = pd.DataFrame(columns=['Video Title', 'Run Time', 'Video Link', 'Keywords'])

    # Iterate through the videos in the playlist
    for video in playlist.videos:
        # Extract video title, run time, and video link
        video_title = video.title
        video_duration = convert_seconds_to_hms(video.length)

        # Extract keywords from the video title and description
        title_keywords = extract_keywords(video_title)

        # Extract keywords from the video.keywords (if available)
        video_keywords = video.keywords
        if video_keywords:
            keyword_string = ", ".join(video_keywords)
        else:
            keyword_string = ""

        all_keywords = title_keywords + video_keywords
        keywords_string = ", ".join(all_keywords)

        # Append video information and keywords to the DataFrame
        df = df.append({'Video Title': video_title, 'Run Time': video_duration, 'Video Link': video.watch_url, 'Keywords': keywords_string}, ignore_index=True)
        
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