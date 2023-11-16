import pandas as pd
import re

def remove_emoji(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F700-\U0001F77F"  # alchemical symbols
                               u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                               u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                               u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                               u"\U0001FA00-\U0001FA6F"  # Chess Symbols
                               u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                               u"\U00002702-\U000027B0"  # Dingbats
                               u"\U000024C2-\U0001F251" 
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

# Load CSV file
input_file_path = 'hinglish_sentences.csv'
output_file_path = 'hinglish_sentences1.csv'

df = pd.read_csv(input_file_path)

# Remove emojis and "@" symbols from the specified columns
columns_to_clean = ['Username', 'Comment Text']  # Add your column names here
for column in columns_to_clean:
    df[column] = df[column].apply(lambda x: remove_emoji(str(x)))

# Save the cleaned data to a new CSV file
df.to_csv(output_file_path, index=False)


