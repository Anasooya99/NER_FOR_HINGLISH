import re

# Step 1: Extract sentences from the data set.
def extract_sentences(data):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', data)
    return sentences

# Step 2: Extract words from the sentences.
def extract_words(sentence):
    words = re.findall(r'\b\w+\b', sentence)
    return words

# Step 3: Manually annotate each word in the data set.
def manual_annotation(words):
    annotated_data = []
    for word in words:
        annotation = input(f"Annotate '{word}' as Named Entity (e.g., PERSON, LOCATION, ORGANIZATION, TIME, YEAR OTHERS): ")
        annotated_data.append((word, annotation))
    return annotated_data

# Step 4: Annotated Named Entity dataset is ready.
def main():
    # Example data (replace this with your dataset)
    with open("hinglish_sentences.csv", 'r', encoding='utf-8') as file:
        data = file.read()

    # Step 1: Extract sentences
    sentences = extract_sentences(data)

    # Step 2 and 3: Extract words and manually annotate
    annotated_dataset = []
    for sentence in sentences:
        words = extract_words(sentence)
        annotated_words = manual_annotation(words)
        annotated_dataset.extend(annotated_words)

    # Step 4: Display the annotated dataset
    print("\nAnnotated Named Entity dataset:")
    for word, annotation in annotated_dataset:
        print(f"{word}: {annotation}")

if __name__ == "__main__":
    main()
