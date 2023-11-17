import pandas as pd
from ast import literal_eval
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

# Load data from CSV file
df = pd.read_csv('tokenized_data.csv')  

# Convert the string representation of lists to actual lists
df['Word'] = df['Word'].apply(literal_eval)

# Tokenize sentences into words
tokenized_sentences = df['Word'].tolist()

# Train Word2Vec model
model = Word2Vec(sentences=tokenized_sentences, vector_size=100, window=5, min_count=1, workers=4)

# Save the model
model.save("word2vec_model_with_labels.bin")

# Load the model
loaded_model = Word2Vec.load("word2vec_model_with_labels.bin")

# Get the vector representation of a word
vector = loaded_model.wv['Bharat'] 

# Find similar words
similar_words = loaded_model.wv.most_similar('lucknow', topn=5)  

print("Vector representation of 'your_word':", vector)
print("Similar words to 'your_word':", similar_words)
