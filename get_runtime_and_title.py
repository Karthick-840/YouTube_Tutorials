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

        video_data = {"Title":playlist.title,"Run Time": convert_seconds_to_hms(total_runtime), "Video Count": video_count,"Video Link": url}

    else:
        video = YouTube(url)
        title = video.title
        runtime = video.length
        video_data = [{"Title": title, "Run Time": convert_seconds_to_hms(runtime),"Video Count":1,"Video Link": url}]
   
    return video_data
