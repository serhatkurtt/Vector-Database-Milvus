# DUPLICATE DETECTION
Goal of the project is to calculate similarity between texts, and find duplicate texts using tresholding method. Project contains two stages:

* Text Embeddings

* Similarity Search Using Vector Database (Milvus)

## Text Embeddings
First of all, sentences are converted into embeddings using sentence transformer that consider bi-directional context (BERT), and takes the average of all sentences in a text. In this way semantic meaning of unstructured data is extracted from the text. Texts having similar content are closer in multi-dimensional embedding space. Cosine similarity metric is used to compare the similarity between texts.

  ![](images/embedding.png?raw=true "Text Embeddings")

Cosine similarity between two embedding vectors can be calculated as follows.

cos(θ) = (A • B) / (‖A‖ * ‖B‖) 

## Milvus

![](images/milvus.png?raw=true "Vector Database")

The Milvus vector database is designed to store and manage, and index high dimensional vector embeddings. It is utilized to accelerate the similarity search. Milvus is installed using Docker Compose. Details can be found in the following link: 

https://milvus.io/docs/v2.0.x/install_standalone-docker.md





