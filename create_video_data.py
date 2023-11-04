from pytube import YouTube, Playlist
import pandas as pd
from datetime import timedelta
from support_functions import convert_seconds_to_hms, extract_keywords


def create_video_data(playlist_url):
    
    playlist = Playlist(playlist_url)
    # Create an empty DataFrame to store the video data
    df = pd.DataFrame(columns=['Video Title', 'Run Time', 'Video Link', 'Keywords'])

    # Iterate through the videos in the playlist
    for video in playlist.videos:
        # Extract video title, run time, and video link
        video_title = video.title
        video_duration = convert_seconds_to_hms(video.length)
        video_description = video.description

        # Extract keywords from the video title and description
        title_keywords = extract_keywords(video_title)# Extract keywords from the video description (if available)
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
