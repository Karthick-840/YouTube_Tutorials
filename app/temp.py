import pickle
import pandas as pd
import nltk
from collections import Counter

# Download necessary NLTK resources (may need internet connection)
nltk.download('punkt')
nltk.download('stopwords')

with open("data.pkl", "rb") as f:
    # Load the pickled data
    imported_data = pickle.load(f)
    merged_df = pd.concat(imported_data, axis=0)
    
print(merged_df)

# Tokenize the text (split into words)
merged_df['video_Title_Tokens'] = merged_df['Video Title'].apply(nltk.word_tokenize)

# Convert words to lowercase
merged_df['video_Title_Tokens'] = merged_df['video_Title_Tokens'].apply(lambda x: [word.lower() for word in x])

# Remove stop words (common words like "the", "a")
stop_words = nltk.corpus.stopwords.words('english')
# Filter to keep only non-stop words
merged_df['non_stop_words'] = merged_df['video_Title_Tokens'].apply(lambda x: [word for word in x if word not in stop_words])

# Flatten the list of non-stop words from all videos into one list
all_words = [word for words in merged_df['non_stop_words'].tolist() for word in words]

# Count occurrences using Counter
word_counts = Counter(all_words)


# Print all words and their counts
print("All non-stop words and their counts:")
for word, count in word_counts.items():
  print(f"- {word} ({count} occurrences)")
  
# Convert word counts to a DataFrame
word_counts_df = pd.DataFrame.from_dict(word_counts, orient='index', columns=['Count'])
word_counts_df.sort_values(by='Count', ascending=False, inplace=True)  # Sort by count (descending)

# Save as CSV
word_counts_df.to_csv('non_stop_word_counts.csv', index=True)

print("Non-stop word counts saved to 'non_stop_word_counts.csv'.")


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
