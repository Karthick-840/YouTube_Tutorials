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