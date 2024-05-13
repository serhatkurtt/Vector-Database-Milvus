from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection, utility
from transformers import BertTokenizer, BertModel
import torch
import numpy as np
import pandas as pd
import re
from sentence_transformers import SentenceTransformer
import csv

connections.connect("default",host='localhost',port="19530")
def clean_text(text): 
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    # Remove extra whitespace
    text = ' '.join(text.split())
    return text


with open("\path\to\inputdata", 'r', errors='replace') as file:
    reader = csv.reader(file)

    # Skip header if present
    header = next(reader, None)

    # Create a list of DataFrames using a list comprehension
    dfs = [pd.DataFrame([row], columns=header) for row in reader]

# Concatenate the list of DataFrames into a single DataFrame
df = pd.concat(dfs, ignore_index=True)

model_name = 'paraphrase-MiniLM-L6-v2'
sbert_model = SentenceTransformer(model_name)

data = df[["Job Id","Job Description"]]
data.rename(columns={'Job Id': 'JobId','Job Description':'JobDescription'},inplace=True)
data = data.to_dict('records')
collection = Collection("FindDuplicate")      
collection.load()


SEARCH_PARAM = {
    "metric_type":"COSINE",
    "params":{"nprobe": 20},
}


def search_similarity(query_embedding):
    results = collection.search([query_embedding],'embeddings',param=SEARCH_PARAM,limit=3)
    return results
t = []
for rowIdx in data:
    temp = clean_text(rowIdx["JobDescription"])
    row_embedding = (sbert_model.encode(temp, convert_to_tensor=False))
    result = (search_similarity(row_embedding))
    t.append(result)

outData = pd.DataFrame(t)
outData.to_excel("\path\to\output\folder",index=False)