# Text Embeddings
Goal of the project is to calculate similarity between texts. First of all, sentences are converted into embeddings using sentence transformer that consider bi-directional context (BERT), and takes the average of all sentences in a text. In this way semantic meaning of unstructured data is extracted from the text. After creating embeddings, the cosine similarity metric is used to compare the similarity between texts. The Milvus vector database is utilized to enhance the efficiency of the comparison.

# Milvus

