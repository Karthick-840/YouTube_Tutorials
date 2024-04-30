# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

from extract_video_data import get_runtime_and_title

if __name__ == '__main__':
    #app.run(debug=True)
    video_data = get_runtime_and_title("https://www.youtube.com/playlist?list=PLe0U7sHuld_qIILgg-2ESRCPWu-WBalFJ")
    print(video_data)
