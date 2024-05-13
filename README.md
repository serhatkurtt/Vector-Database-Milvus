# Text Embeddings
Goal of the project is to calculate similarity between texts. First of all, sentences are converted into embeddings using sentence transformer that consider bi-directional context (BERT), and takes the average of all sentences in a text. In this way semantic meaning of unstructured data is extracted from the text. Texts having similar content are closer in multi-dimensional embedding space. Cosine similarity metric is used to compare the similarity between texts.

  ![](images/embedding.png?raw=true "Text Embeddings")

# Milvus
The Milvus vector database is designed to store and manage high dimensional vector embeddings. It is utilized to enhance the efficiency of the similarity search. It is installed using Docker Compose.Pymilvus library is used to use Milvus database with Python.
