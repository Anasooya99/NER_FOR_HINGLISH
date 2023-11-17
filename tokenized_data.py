import pandas as pd
import nltk

# Download NLTK resources if not already downloaded
nltk.download('punkt')

# Load the annotated data from CSV
annotated_data = pd.read_csv('annotated_data.csv')

# Tokenize each word in the annotated dataset using NLTK
tokenized_data = []
for index, row in annotated_data.iterrows():
    word = row['Word']
    label = row['Label']
    tokens = nltk.word_tokenize(word)
    tokenized_data.append({'Word': tokens, 'Label': label})

# Create a DataFrame from the tokenized data
tokenized_df = pd.DataFrame(tokenized_data)

# Save the tokenized data to a new CSV file
tokenized_df.to_csv('tokenized_data.csv', index=False)

# Display the tokenized data
print(tokenized_df)
