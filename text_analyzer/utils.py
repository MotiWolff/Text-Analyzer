PUNCTUATIONS = ".,:;!?\"'()[]{}"

def read_file(file_path):
    try: 
        with open(file_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found.."
    except PermissionError:
        return f"Error: No permission to read '{file_path}'."
    except UnicodeDecodeError:
        return f"Error: Cannot decode file '{file_path}'. Try a different encoding."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def clean_text(data):
    """Common function to clean and split words"""
    words = data.split()
    clean_words = [word.strip(PUNCTUATIONS).lower() for word in words if word.strip()]
    return clean_words

def count_word_frequencies(words):
    """Common function to count word frequencies"""
    word_count = {}
    for word in words:
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count

def sum_of_sentences(data):
    sentences = data.split(".")
    return [sentence.strip() for sentence in sentences if sentence.strip()]

def most_common_word(data):
    clean_words = clean_text(data)
    word_count = count_word_frequencies(clean_words)
    
    if not word_count:
        return "", 0
    
    return max(word_count.items(), key=lambda x: x[1])

def longest_word(data):
    clean_words = clean_text(data)
    
    if not clean_words:
        return [], 0
    
    max_length = max(len(word) for word in clean_words)
    longest_words = list(set(word for word in clean_words if len(word) == max_length))
    
    return longest_words, max_length

def count_unique_words(data):
    clean_words = clean_text(data)
    return len(set(clean_words))

def words_with_frequency(data, frequency):
    clean_words = clean_text(data)
    word_count = count_word_frequencies(clean_words)
    return [word for word, count in word_count.items() if count == frequency]

def find_equal_length_sequences(data):
    clean_words = clean_text(data)
    sequences = []
    current_seq = []
    current_len = 0
    
    for word in clean_words:
        if current_len == 0:  # First word in potential sequence
            current_seq = [word]
            current_len = len(word)
        elif len(word) == current_len:  # Word with same length
            current_seq.append(word)
        else:  # Different length word
            if len(current_seq) >= 2:  # If we found a valid sequence
                sequences.append(current_seq.copy())
            current_seq = [word]
            current_len = len(word)
    
    # Check the last sequence
    if len(current_seq) >= 2:
        sequences.append(current_seq)
        
    return sequences

import re
from collections import Counter
from typing import Dict, List, Tuple

def analyze_text(text: str) -> Dict:
    """
    Analyze text and return various statistics and patterns.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        Dict containing analysis results
    """
    # Clean and prepare text
    text = text.strip()
    words = re.findall(r'\b\w+\b', text.lower())
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # Basic statistics
    word_count = len(words)
    sentence_count = len(sentences)
    unique_words = set(words)
    unique_words_count = len(unique_words)
    
    # Word frequency
    word_freq = Counter(words)
    most_common_word = word_freq.most_common(1)[0] if word_freq else ('', 0)
    
    # Length analysis
    word_lengths = [len(word) for word in words]
    avg_word_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    max_word_length = max(word_lengths) if word_lengths else 0
    longest_words = [word for word in words if len(word) == max_word_length]
    
    # Find sequences of words with equal length
    equal_length_sequences = []
    current_sequence = []
    current_length = None
    
    for word in words:
        if current_length is None:
            current_length = len(word)
            current_sequence = [word]
        elif len(word) == current_length:
            current_sequence.append(word)
        else:
            if len(current_sequence) > 1:
                equal_length_sequences.append(current_sequence)
            current_length = len(word)
            current_sequence = [word]
    
    if len(current_sequence) > 1:
        equal_length_sequences.append(current_sequence)
    
    return {
        'word_count': word_count,
        'sentence_count': sentence_count,
        'unique_words_count': unique_words_count,
        'most_common_word': most_common_word,
        'average_word_length': avg_word_length,
        'longest_words': longest_words,
        'frequency_words': dict(word_freq),
        'equal_length_sequences': equal_length_sequences
    }