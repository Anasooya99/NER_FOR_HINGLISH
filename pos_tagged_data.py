import pandas as pd
import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize

# Download NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Load annotated data from CSV file
annotated_data = pd.read_csv("tokenized_data.csv")

# Function to perform POS tagging using NLTK
def pos_tagging(text):
    tokens = word_tokenize(str(text))
    pos_tags = pos_tag(tokens)
    return pos_tags

# Apply POS tagging to each row in the DataFrame
annotated_data["POS Tags"] = annotated_data["Word"].apply(pos_tagging)

# Save the results to a new CSV file
annotated_data.to_csv("pos_tagged_data.csv", index=False)

# Display the DataFrame with POS tags
print(annotated_data)
