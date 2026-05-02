import torch

from utils.preprocessing import preprocess_emails, encode_text

def predict_logistic(model, vectorizer, emails):
    emails = preprocess_emails(emails)
    X = vectorizer.transform(emails)
    preds = model.predict(X)

    results = []
    for email, pred in zip(emails, preds):
        results.append({
            "email": email,
            "label": int(pred),
            "classificacao": "SPAM" if pred == 1 else "NÃO SPAM"
        })

    return results

def predict_transformer(model, vocab, emails, max_len=20):
    emails = preprocess_emails(emails)

    X = torch.tensor(
        [encode_text(email, vocab, max_len=max_len) for email in emails],
        dtype=torch.long
    )

    model.eval()
    with torch.no_grad():
        outputs = model(X)
        preds = torch.argmax(outputs, dim=1).cpu().numpy()

    results = []
    for email, pred in zip(emails, preds):
        results.append({
            "email": email,
            "label": int(pred),
            "classificacao": "SPAM" if pred == 1 else "NÃO SPAM"
        })

    return results