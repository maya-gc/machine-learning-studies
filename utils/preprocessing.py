import re
import torch

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-ZÀ-ÿ0-9\s]", "", text)
    return text.strip()

def preprocess_emails(emails):
    return [clean_text(email) for email in emails]

def prepare_logistic_data(emails, labels, test_size=0.3, random_state=42):
    emails = preprocess_emails(emails)

    X_train_texts, X_test_texts, y_train, y_test = train_test_split(
        emails,
        labels,
        test_size=0.3,
        random_state=42,
        stratify=labels
    )

    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    X_train = vectorizer.fit_transform(X_train_texts)
    X_test = vectorizer.transform(X_test_texts)

    return vectorizer, X_train, X_test, y_train, y_test, X_train_texts, X_test_texts

def tokenize(text):
    return clean_text(text).split()

def build_vocab(texts, min_freq=1):
    freq = {}
    for text in texts:
        for token in tokenize(text):
            freq[token] = freq.get(token, 0) + 1

    vocab = {"<PAD>": 0, "<UNK>": 1}
    for token, count in freq.items():
        if count >= min_freq:
            vocab[token] = len(vocab)

    return vocab

def encode_text(text, vocab, max_len=20):
    tokens = tokenize(text)
    encoded = [vocab.get(token, vocab["<UNK>"]) for token in tokens]

    if len(encoded) < max_len:
        encoded += [vocab["<PAD>"]] * (max_len - len(encoded))
    else:
        encoded = encoded[:max_len]

    return encoded

def prepare_transformer_data(emails, labels, test_size=0.3, random_state=42, max_len=20):
    emails = preprocess_emails(emails)

    X_train_texts, X_test_texts, y_train, y_test = train_test_split(
        emails,
        labels,
        test_size=0.3,
        random_state=42,
        stratify=labels
    )

    vocab = build_vocab(X_train_texts)

    X_train = torch.tensor(
        [encode_text(text, vocab, max_len=max_len) for text in X_train_texts],
        dtype=torch.long
    )
    X_test = torch.tensor(
        [encode_text(text, vocab, max_len=max_len) for text in X_test_texts],
        dtype=torch.long
    )

    y_train = torch.tensor(y_train, dtype=torch.long)
    y_test = torch.tensor(y_test, dtype=torch.long)

    return vocab, X_train, X_test, y_train, y_test, X_train_texts, X_test_texts