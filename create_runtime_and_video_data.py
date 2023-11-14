from support_functions import convert_seconds_to_hms, extract_keywords

from pytube import YouTube, Playlist
import pandas as pd
from datetime import timedelta



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
