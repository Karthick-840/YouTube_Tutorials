
from extract_video_data import Playlist_Info
import pickle 
import pandas as pd


urls = ['https://www.youtube.com/playlist?list=PLOlK8ytA0MghpdMjb0m9zu1v9s_qbRP0q']

print(urls)
    
data = []
for url in urls:
    info = Playlist_Info(url)
    data.append(info.get_info())

print(data)