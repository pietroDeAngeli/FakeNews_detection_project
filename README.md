# 📰 Fake News Detection with NLP and Neural Networks

This project explores two distinct approaches to detecting fake news articles using **Natural Language Processing** and **supervised machine learning** techniques. The models were developed and evaluated as part of a university project for the Computational Social Science course at the University of Trento.

> 🔍 We compare a transparent TF-IDF classifier with a high-performing Multilayer Perceptron (MLP) trained on OpenAI-generated embeddings.

---

## 🎯 Objective

Develop a system capable of **automatically distinguishing real from fake news** using only the article’s text content, through:

- Data preprocessing and normalization
- Embedding generation via **OpenAI API**
- Classification with **TF-IDF** and **MLP**
- Evaluation and visualization of performance and language patterns

---

## 🗂 Dataset

- Source: [Fake and Real News Dataset](https://huggingface.co/datasets/ErfanMoosaviMonazzah/fake-news-detection-dataset-English)
- ~44,000 labeled articles (`real` vs `fake`)
- Fields: `title`, `text`, `subject`, `date`, `label`
- Preprocessing:
  - Merging `title` and `body`
  - Lowercasing, punctuation removal, stopword removal
  - Subject label normalization (e.g., "US", "Middle-east" → "News")

---

## 🧠 Models

### 1. TF-IDF + Logistic Regression
- Simple, interpretable baseline
- Accuracy: **98.17%**
- Reveals key term-based indicators of fake news (e.g., emotional, vague language)

### 2. MLP + OpenAI Embeddings
- Used OpenAI’s embedding API to obtain 1536-dim vectors
- MLP with 2 hidden layers (256, 128)
- Accuracy: **99.10%**
- Outperforms TF-IDF but behaves as a black box

---

## 📊 Evaluation

| Metric      | TF-IDF | MLP   |
|-------------|--------|-------|
| Accuracy    | 98.17% | 99.10% |
| Mislabel real as fake | 0.023% | 0.011% |
| Mislabel fake as real | 0.013% | 0.007% |

Confusion matrices for both models are strongly diagonal, confirming high reliability.

---

## 📈 Analysis

- **UMAP** visualizations show semantic separation between fake and real articles in the embedding space.
- **Word clouds** reveal stylistic patterns:
  - Fake news: emotionally charged, speculative words (e.g., “think”, “claim”, “Twitter”)
  - Real news: formal, source-based vocabulary (e.g., “statement”, “government”)

---

## 📌 Highlights

- Comparative analysis of **accuracy vs interpretability**
- Insight into **topic-wise classification difficulty** (e.g., political articles are harder to distinguish)
- Discussion on ethical considerations and model misuse risks


---

## 📚 Further Reading

- [🧾 Final Report PDF](./Fake_news_detection.pdf)
- [📝 Project Design](./Project%20design.md)

---

## 👤 Authors

- Pietro De Angeli
- Vadim Mnev  
- Otto Vanto  

---

## 🏁 Conclusion

This project shows that automatic fake news detection is a tractable task using both shallow and deep NLP approaches. While MLPs offer higher accuracy, TF-IDF models provide transparency and interpretability — essential for high-stakes applications like journalism and public policy.




