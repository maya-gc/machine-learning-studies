# Machine Learning Studies - Spam Detection Comparison

![GitHub repo size](https://img.shields.io/github/repo-size/maya-gc/machine-learning-studies?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/maya-gc/machine-learning-studies?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/maya-gc/machine-learning-studies?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/maya-gc/machine-learning-studies?style=for-the-badge)
![GitHub pull requests](https://img.shields.io/github/issues-pr/maya-gc/machine-learning-studies?style=for-the-badge)

<img width="2048" height="1365" alt="image" src="https://github.com/user-attachments/assets/a9433380-1cc0-495c-9ec5-feb083348b1a" />

---

> Repositório dedicado a estudos de Machine Learning com foco em projetos práticos, experimentos e comparações entre modelos clássicos e modernos aplicados a problemas reais como detecção de spam.

Este projeto apresenta um comparativo entre regressão logística com TF-IDF e uma arquitetura baseada em Transformer, explorando diferenças de desempenho, treinamento e interpretabilidade.

---

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

* Você instalou a versão mais recente de `Python 3.10+`
* Bibliotecas necessárias: `scikit-learn`, `pandas`, `numpy`, `transformers`, `torch`
* Você tem uma máquina `Windows / Linux / Mac`
* Conhecimento básico em Machine Learning e NLP é recomendado

---

## ☕ Usando Machine Learning Studies

Para executar o projeto:

```
python main.py
```

### Pipeline do projeto

A comparação entre os modelos segue estas etapas:

```
1. Geração de dados sintéticos
2. Pré-processamento de texto
3. Treinamento dos modelos
4. Avaliação de desempenho
```

### Modelos utilizados

* **Modelo clássico**

  * Vetorização: TF-IDF
  * Classificador: Regressão Logística
  * Vantagens: rápido, interpretável, robusto para dados simples

* **Modelo Transformer**

  * Uso de embeddings e mecanismo de atenção
  * Rede neural com múltiplas camadas
  * Vantagens: captura contexto semântico complexo

### Resultados

Ambos os modelos alcançaram **100% de acurácia**, indicando que o dataset sintético é simples e linearmente separável.

Principais diferenças:

* Modelo clássico:

  * Mais rápido
  * Mais interpretável
  * Melhor para problemas simples

* Transformer:

  * Mais complexo e lento
  * Melhor generalização em dados reais
  * Capta contexto semântico mais profundo

### Casos de uso

* Filtro de spam básico
* Classificação de mensagens
* Detecção de fraude
* Análise de sentimentos
* Detecção de phishing

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENSE.md](LICENSE.md) para mais detalhes.

