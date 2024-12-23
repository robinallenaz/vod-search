import pandas as pd
from collections import Counter
import re


def load_transcripts(file_path):
    """Load the transcript from a text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def preprocess_text(text):
    """Remove punctuation and convert to lowercase."""
    text = re.sub(r'[\W_]+', ' ', text).lower()
    return text.split()


def calculate_word_frequencies(words):
    """Calculate the frequency of each word in the list."""
    return Counter(words)


def prepare_data_for_visualization(file_path):
    """Prepare the data by loading, preprocessing, and calculating word frequencies."""
    transcript = load_transcripts(file_path)
    words = preprocess_text(transcript)
    word_frequencies = calculate_word_frequencies(words)
    # Convert to DataFrame
    df = pd.DataFrame(word_frequencies.items(), columns=['Word', 'Frequency'])
    return df


# Example usage
if __name__ == "__main__":
    file_path = 'path_to_your_transcript.txt'  # Replace with your actual file path
    df = prepare_data_for_visualization(file_path)
    print(df.head())
