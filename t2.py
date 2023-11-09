from transformers import DistilBertTokenizer, DistilBertModel
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


# Load pre-trained DistilBERT model and tokenizer
model_name = 'distilbert-base-uncased'
tokenizer = DistilBertTokenizer.from_pretrained(model_name)
model = DistilBertModel.from_pretrained(model_name)
sentence1 = """ 
Employee Remote Work Policy 
 
Effective Date: January 1, 20XX 
 
1. Introduction 
 
The Employee Remote Work Policy outlines the guidelines and procedures for employees who 
wish to work remotely on an occasional basis. Remote work arrangements are subject to 
approval and are intended to provide flexibility while maintaining productivity and teamwork. 
 
2. Eligibility 
 
Full-time employees with at least one year of service are eligible to request remote work 
arrangements. Requests must be submitted at least two weeks in advance and require 
managerial approval. 
 
3. Work Hours and Reporting 
 
Remote employees are expected to work their regular hours and follow the established 
reporting procedures. They must remain reachable during working hours and be available for 
virtual meetings as needed. 
 
4. Equipment and Security 
 
Remote employees are responsible for ensuring the security of company-provided equipment 
and data. All security protocols, including VPN usage and data protection, must be adhered to. 
 
5. Performance and Evaluation 
 
Remote employees' performance will be evaluated based on agreed-upon goals and objectives. 
The same performance standards apply, regardless of the work location. 
 
6. Termination of Arrangement 
 
Management reserves the right to terminate a remote work arrangement if it negatively 
impacts performance, teamwork, or security. 
 
7. Conclusion 
 
This policy ensures that remote work arrangements are conducted in alignment with company 
goals and values. It is the responsibility of both employees and managers to communicate 
effectively and maintain a high standard of performance. 
 
[Your Company Name] 
[Your Company Address]
"""
sentence2 = """ 
Flexible Work Arrangements Policy 
 
Effective Date: January 1, 20XX 
 
1. Purpose 
 
The Flexible Work Arrangements Policy establishes a framework that allows employees to 
choose work arrangements that best suit their needs and contribute to a balanced and 
productive work environment. 
 
2. Eligibility 
 
All employees are eligible to explore flexible work arrangements, including remote work, 
compressed workweeks, and flexible hours. Employees should discuss their preferences with 
their supervisors and mutually agree on suitable arrangements. 
 
3. Approval Process 
 
Supervisors and employees will collaboratively assess the feasibility of proposed flexible work 
arrangements. Once an agreement is reached, the arrangement can be implemented on a trial 
basis. 
 
4. Communication and Availability 
 
Employees participating in flexible work arrangements must maintain effective communication 
and availability during core business hours. Regular team meetings and virtual check-ins are 
encouraged to foster collaboration. 
 
5. Performance and Accountability 
 
Employees are accountable for meeting their performance goals and fulfilling their 
responsibilities, regardless of their chosen work arrangement. Regular performance evaluations 
will consider the impact of flexible work on overall performance. 
 
6. Technology and Data Security 
 
Employees working remotely are responsible for ensuring the security of company data and 
following all technology protocols. Company-provided equipment and software must be used 
for work-related tasks. 
 
7. Termination of Arrangement 
 
Flexible work arrangements can be terminated by mutual agreement or if they are found to 
impede team collaboration or business operations. 
 
8. Conclusion 
 
Our commitment to flexible work arrangements reflects our dedication to supporting a diverse 
and inclusive work environment. By fostering work-life balance and adapting to changing needs, 
we strive to enhance employee satisfaction and productivity. 
 
[Your Company Name] 
[Your Company Address]
"""

# Tokenize and encode sentences
inputs = tokenizer([sentence1, sentence2], return_tensors='pt', padding=True, truncation=True)

# Get embeddings for the [CLS] token
with torch.no_grad():
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state[:, 0, :].numpy()

# Calculate cosine similarity
similarity_score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
print(f"Similarity Score: {similarity_score:.4f}")
