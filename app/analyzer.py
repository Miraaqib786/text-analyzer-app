import re
from collections import Counter

def analyze_text(text):
    characters = len(text)
    words = re.findall(r'\b\w+\b', text)
    word_count = len(words)
    sentences = len([s for s in re.split(r'[.!?]', text) if s.strip()])
    paragraphs = len([p for p in text.split('\n') if p.strip()])
    average_word_length = round(sum(len(w) for w in words)/word_count, 2) if word_count else 0

    counter = Counter([w.lower() for w in words])
    top_words = counter.most_common(5)

    return {
        "characters": characters,
        "words": word_count,
        "sentences": sentences,
        "paragraphs": paragraphs,
        "average_word_length": average_word_length,
        "top_words": top_words
    }