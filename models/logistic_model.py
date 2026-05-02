from sklearn.linear_model import LogisticRegression

def build_logistic_model():
    model = LogisticRegression(
        max_iter=1000,
        random_state=42
    )
    return model