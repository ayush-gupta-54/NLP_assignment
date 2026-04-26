# Rule-Based Medical Chatbot using NLP

This project is a rule-based medical chatbot built using Python and NLTK for NLP.

It takes symptoms as input, matches them with symptoms from a medical dataset, and returns:
- possible disease
- disease description
- precautions

## Dataset
Disease Symptom Prediction Dataset (Kaggle)

Dataset Link:
https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset

## Features
- Symptom-based disease prediction
- Disease description retrieval
- Precaution suggestion
- Rule-based NLP chatbot

## Technologies Used
- Python
- Pandas
- NLTK

## How It Works
1. User enters symptoms
2. Symptoms are preprocessed using NLP
3. Input is matched with dataset symptoms
4. Best matching disease is identified
5. Description and precautions are displayed

## Run the Project
```bash
python chatbot.py