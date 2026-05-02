from train import train_logistic, train_transformer
from predict import predict_logistic, predict_transformer

def main():
    novos_testes = [
        "Ganhe dinheiro fácil agora",
        "Reunião sobre o projeto amanhã",
        "Promoção exclusiva para você",
        "Envio do relatório final em anexo"
    ]

    print("Treinando Logistic Regression...")
    logistic_artifacts = train_logistic()

    print("\nTreinando MiniTransformer...")
    transformer_artifacts = train_transformer()

    print("\nPredições com Logistic Regression:")
    logistic_preds = predict_logistic(
        logistic_artifacts["model"],
        logistic_artifacts["vectorizer"],
        novos_testes
    )
    for item in logistic_preds:
        print(f"Email: {item['email']}")
        print(f"Classificação: {item['classificacao']}\n")

    print("Predições com MiniTransformer:")
    transformer_preds = predict_transformer(
        transformer_artifacts["model"],
        transformer_artifacts["vocab"],
        novos_testes,
        max_len=transformer_artifacts["max_len"]
    )
    for item in transformer_preds:
        print(f"Email: {item['email']}")
        print(f"Classificação: {item['classificacao']}\n")

if __name__ == "__main__":
    main()