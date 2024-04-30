# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')
from extract_video_data import Playlist_Info
import pickle 

if __name__ == '__main__':
    #app.run(debug=True)
    #video_data = get_runtime_data("https://www.youtube.com/playlist?list=PLe0U7sHuld_qIILgg-2ESRCPWu-WBalFJ")
    #print(video_data)
    url1 = "https://www.youtube.com/playlist?list=PLwFJcsJ61ouizyVPDIjomZFb2S_zcJebP"
    url = "https://www.youtube.com/playlist?list=PLe0U7sHuld_qIILgg-2ESRCPWu-WBalFJ"
    info = Playlist_Info(url)
    
    # with open('saved_dictionary.pkl', 'wb') as f:
    #     pickle.dump(info, f)
    
    print(info.get_info())
