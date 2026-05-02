from sklearn.metrics import accuracy_score, classification_report

def evaluate_predictions(y_true, y_pred, model_name="Modelo"):
    acc = accuracy_score(y_true, y_pred)
    report = classification_report(y_true, y_pred, digits=4)

    print(f"\n===== {model_name} =====")
    print(f"Acurácia: {acc * 100:.2f}%")
    print("Relatório de classificação:")
    print(report)

    return {
        "model": model_name,
        "accuracy": acc,
        "report": report
    }