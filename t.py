# Install the required libraries if you haven't already
# !pip install transformers

import numpy as np
from nltk.tokenize import sent_tokenize
import torch
from transformers import DistilBertTokenizer, DistilBertModel
from highlight import get_sections

# Load pre-trained DistilBERT model and tokenizer
model_name = 'distilbert-base-uncased'
tokenizer = DistilBertTokenizer.from_pretrained(model_name)
model = DistilBertModel.from_pretrained(model_name)

embeddings = []
for section in sections:
    inputs = tokenizer(sections[section], return_tensors='pt', padding='max_length', truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
        embeddings.append(outputs.last_hidden_state.mean(dim=1))

embedding_matrix = torch.cat(embeddings, dim=0)

similarity_matrix = cosine_similarity(embedding_matrix, embedding_matrix)

for i in range(len(sections)):
    for j in range(i + 1, len(sections)):
        print(f"Similarity between sections {i} and {j}: {similarity_matrix[i, j]}")