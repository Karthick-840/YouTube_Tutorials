from pytube import Playlist
import pandas as pd
from datetime import timedelta
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download("stopwords")
nltk.download("punkt")

# Define the URL of the YouTube playlist
playlist_url = "https://www.youtube.com/playlist?list=PLe0U7sHuld_qIILgg-2ESRCPWu-WBalFJ"

# Create a Playlist object
playlist = Playlist(playlist_url)

# Print the title of the playlist
print("Playlist Title:", playlist.title)

def convert_seconds_to_hms(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        
# Define a function to extract keywords from text
def extract_keywords(text):
    # Tokenize the text
    words = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word.lower() not in stop_words]
    return words

# Create empty lists to store video titles, run times, video links, and keywords
video_titles = []
video_run_times = []
video_links = []
video_keywords = []

# Iterate through the videos in the playlist
for video in playlist.videos:
    # Extract video title, run time, and video link
    video_title = video.title
    video_run_time_seconds = video.length
    video_description = video.description
    video_duration = convert_seconds_to_hms(video_run_time_seconds)
    video_link = video.watch_url

    # Extract keywords from the video title and description
    title_keywords = extract_keywords(video_title)
    # Extract keywords from the video description (if available)
    if video_description:
        description_keywords = extract_keywords(video_description)
    else:
        description_keywords = []
    all_keywords = title_keywords + description_keywords
    keywords_string = ", ".join(all_keywords)

    # Append video information and keywords to respective lists
    video_titles.append(video_title)
    video_run_times.append(video_duration)
    video_links.append(video_link)
    video_keywords.append(keywords_string)

# Create a DataFrame from the lists
video_data = {
    'Video Title': video_titles,
    'Run Time': video_run_times,
    'Video Link': video_links,
    'Keywords': video_keywords
}
df = pd.DataFrame(video_data)

# Print the DataFrame
print(df)
