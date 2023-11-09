from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity
import torch
from highlight import get_sections

# Load pre-trained BERT model and tokenizer
model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

# Example dictionaries of circular sections
sections1 = get_sections("Pillar 2 - NEW.pdf", 14, 17)

sections2 = get_sections("Pillar 2 - OLD.pdf", 14, 17)

# Combine section names and texts from both dictionaries
section_names1 = list(sections1.keys())
section_texts1 = list(sections1.values())

section_names2 = list(sections2.keys())
section_texts2 = list(sections2.values())

# Tokenize and embed sections from both dictionaries
embeddings1 = []
for section_text in section_texts1:
    inputs = tokenizer(section_text, return_tensors='pt', padding='max_length', truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
        embeddings1.append(outputs.last_hidden_state.mean(dim=1))  # Use mean pooling

embeddings2 = []
for section_text in section_texts2:
    inputs = tokenizer(section_text, return_tensors='pt', padding='max_length', truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
        embeddings2.append(outputs.last_hidden_state.mean(dim=1))  # Use mean pooling

# Convert embeddings to matrices
embedding_matrix1 = torch.cat(embeddings1, dim=0)
embedding_matrix2 = torch.cat(embeddings2, dim=0)

# Calculate cosine similarity between sections using embeddings
similarity_matrix = cosine_similarity(embedding_matrix1, embedding_matrix2)

# Print similarity matrix (for demonstration)
for i in range(len(section_names1)):
    for j in range(len(section_names2)):
        if similarity_matrix[i, j] > 0.9:
            print(f"Similarity between '{section_names1[i]}' and '{section_names2[j]}': {similarity_matrix[i, j]}")
