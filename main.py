# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')
from extract_video_data import Playlist_Info
import pickle 
import pandas as pd

if __name__ == '__main__':
    #app.run(debug=True)
    #video_data = get_runtime_data("https://www.youtube.com/playlist?list=PLe0U7sHuld_qIILgg-2ESRCPWu-WBalFJ")
    #print(video_data)
    
    # %%
    url1 = "https://www.youtube.com/playlist?list=PLwFJcsJ61ouizyVPDIjomZFb2S_zcJebP"
    url = "https://www.youtube.com/playlist?list=PLe0U7sHuld_qIILgg-2ESRCPWu-WBalFJ"
    print(url)
    
    # %%

    urls = ['https://www.youtube.com/playlist?list=PL4cUxeGkcC9hxjeEtdHFNYMtCpjNBm3h7',
            'https://www.youtube.com/playlist?list=PL_Ct8Cox2p8UlTfHyJc3RDGuGktPNs9Q3',
            'https://www.youtube.com/playlist?list=PLwFJcsJ61ouizyVPDIjomZFb2S_zcJebP',
            'https://www.youtube.com/playlist?list=PLwFJcsJ61oujAqYpMp1kdUBcPG0sE0QMT',
            'https://www.youtube.com/playlist?list=PLlOuZAcnp6h4j8IXBqpJT89SZLWyu0QFk',
            'https://www.youtube.com/playlist?list=PLDoIcTNj_voXjx4nR_oXpZg1aiPytNgzC',
            'https://www.youtube.com/playlist?list=PLtqF5YXg7GLmCvTswG32NqQypOuYkPRUE',
            'https://www.youtube.com/playlist?list=PLhYDP66xNTKSBSqiQeJcbamwh-UCqqa0j',
            'https://www.youtube.com/playlist?list=PLyNBB9VCLmo1hyO-4fIZ08gqFcXBkHy-6',
            'https://www.youtube.com/playlist?list=PLOlK8ytA0MgjYGVrz0hS4w3UPQ1-VV2uX',
            'https://www.youtube.com/playlist?list=PLMVV8yyL2GN_n41v1ESBvDHwMbYYhlAh1',
            'https://www.youtube.com/playlist?list=PLEt8Tae2spYlxiF1scFTTIGG37TouiF2t',
            'https://www.youtube.com/playlist?list=PLpoANyiDUFjmwBQgKoh8h5e5q06blWsHc',
            'https://www.youtube.com/playlist?list=PL0MniIVMkp8cDQSFRgqmPlUVdqz097dXE',
            'https://www.youtube.com/playlist?list=PLWZJrkeLOrbbmGIW-7znaSpRinp8d-1Dt',
            'https://www.youtube.com/playlist?list=PLe0U7sHuld_qIILgg-2ESRCPWu-WBalFJ'
            ]
    
    data = []
    for url in urls:
        info = Playlist_Info(url)
        data.append(info.get_info())
        
    
    if data:
        with open('data.pkl', 'wb') as f:
            # Pickle the data using the highest protocol version for compatibility
            pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
        df = pd.DataFrame(data)  # Create the DataFrame
        df.to_csv("concert_data.csv", index=False)  # Save as XLSX without index column
        print("Concert data saved successfully to 'concert_data.xlsx'.")
    else:
        print("No concert data retrieved or processed.")


"""
https://www.youtube.com/watch?v=VK9PGcGx2xk

try using the youtube function directly 
https://developers.google.com/youtube/v3

Boosan - portfolio -https://www.youtube.com/watch?v=Ji5Cg2O_XDs
"""
# %%
