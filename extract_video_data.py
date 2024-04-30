from icalendar import Calendar, Event
from datetime import datetime, timedelta
from pytube import YouTube, Playlist, Search
from pytube.exceptions import VideoUnavailable
import pandas as pd
from datetime import timedelta
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download("stopwords")
nltk.download("punkt")


class Playlist_Info():
    def __init__(self,url) -> None:
        self.url = url
        
        if not self.url or not isinstance(self.url, str):
            raise ValueError("Invalid URL provided.")
        
            
    def get_info(self):
        
        info = []
        if 'playlist' in self.url: 
            info = self.get_playlist_data()
        else:
            info = self.get_video_data(self.url)
            
        video_details = pd.DataFrame(info)
        video_details = video_details.assign(Start_Date=None, Start_Time=None, Time_to_Spend=None)
        return video_details
                
    def get_playlist_data(self):
        playlist = Playlist(self.url)
        # Create an empty DataFrame to store the video data
        playlist_data = []
        
        for url in playlist.video_urls:
            playlist_data.append(self.get_video_data(url))
            
        return playlist_data
    
    @staticmethod
    def get_video_data(url):
        try:
             yt = YouTube(url)
        except VideoUnavailable:
             print(f'Video {url} is unavaialable, skipping.')
        else:
            video = YouTube(url)
            video_title = video.title
            video_runtime = Playlist_Info.convert_seconds_to_hms(video.length)
            

            # extract keywords from the video
            keywords_string = []
            #keywords_string = extract_keywords(video_title) + extract_keywords (video.keywords)
            #keywords_string =  ", ".join(keywords_string)

            video_data = {"Video Title": video_title, "Run Time": video_runtime, "Video Link": url,"Video Keywords": keywords_string}
            
            return video_data
    
    @staticmethod
    def convert_seconds_to_hms(seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    
    @staticmethod
    # Define a function to extract keywords from text
    def extract_keywords(video_keywords):

        while bool(video_keywords):
            if isinstance(video_keywords,list):
                text = ", ".join(video_keywords)
            else:
                text = video_keywords

            # Use regular expressions to remove special characters, symbols, and numbers
            cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
            
            # Tokenize the cleaned text
            words = word_tokenize(cleaned_text)
            # Create a list of English stopwords and additional common words to exclude
            custom_stopwords = set(stopwords.words("english") + ["for", "or", "and", "the", "is", "are", "it", "in", "on"])
            
            # Remove punctuation, stopwords and common words and also lowercase the words
            words = [word.lower() for word in words if word.isalpha()]
            words = [word for word in words if word not in custom_stopwords]
        
            return words

    def search_similar():
        
        s = Search('YouTube Rewind')
        len(s.results)
        print(s.results)
        s.get_next_results()
        s.completion_suggestions


    # Define the URL of the YouTube playlist


# List of playlist URLs
sample_playlist_urls = ["https://www.youtube.com/playlist?list=PLe0U7sHuld_qIILgg-2ESRCPWu-WBalFJ",
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