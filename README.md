# Text Embeddings
Goal of the project is to calculate similarity between texts, and find duplicate texts using tresholding method. First of all, sentences are converted into embeddings using sentence transformer that consider bi-directional context (BERT), and takes the average of all sentences in a text. In this way semantic meaning of unstructured data is extracted from the text. Texts having similar content are closer in multi-dimensional embedding space. Cosine similarity metric is used to compare the similarity between texts.

  ![](images/embedding.png?raw=true "Text Embeddings")

# Milvus

[](images/milvus.png?raw=true "Text Embeddings")

The Milvus vector database is designed to store and manage high dimensional vector embeddings. It is utilized to accelerate the similarity search. Milvus is installed using Docker Compose. Details can be found in the following link: 

https://milvus.io/docs/v2.0.x/install_standalone-docker.md

