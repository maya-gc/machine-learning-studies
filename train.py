import torch
import torch.nn as nn

from data.dataset import load_data
from models.logistic_model import build_logistic_model
from models.mini_transformer import MiniTransformer
from utils.preprocessing import prepare_logistic_data, prepare_transformer_data
from utils.metrics import evaluate_predictions

def train_logistic():
    emails, labels = load_data()

    vectorizer, X_train, X_test, y_train, y_test, _, _ = prepare_logistic_data(emails, labels)

    model = build_logistic_model()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    results = evaluate_predictions(y_test, y_pred, model_name="Logistic Regression")

    return {
        "model": model,
        "vectorizer": vectorizer,
        "results": results
    }

def train_transformer(epochs=15, lr=0.001, max_len=20):
    emails, labels = load_data()

    vocab, X_train, X_test, y_train, y_test, _, _ = prepare_transformer_data(
        emails, labels, max_len=max_len
    )

    model = MiniTransformer(
        vocab_size=len(vocab),
        embed_dim=64,
        num_heads=4,
        hidden_dim=128,
        num_layers=2,
        max_len=max_len,
        num_classes=2
    )

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    model.train()
    for epoch in range(epochs):
        optimizer.zero_grad()
        outputs = model(X_train)
        loss = criterion(outputs, y_train)
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 5 == 0:
            print(f"Epoch {epoch+1}/{epochs} - Loss: {loss.item():.4f}")

    model.eval()
    with torch.no_grad():
        outputs = model(X_test)
        y_pred = torch.argmax(outputs, dim=1).cpu().numpy()

    results = evaluate_predictions(y_test.cpu().numpy(), y_pred, model_name="MiniTransformer")

    return {
        "model": model,
        "vocab": vocab,
        "results": results,
        "max_len": max_len
    }