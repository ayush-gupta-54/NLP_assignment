import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

# Load datasets
symptom_df = pd.read_csv("data/dataset.csv")
desc_df = pd.read_csv("data/symptom_Description.csv")
prec_df = pd.read_csv("data/symptom_precaution.csv")

# Standardize disease column names
desc_df.columns = ["Disease", "Description"]
prec_df.columns = ["Disease", "Precaution_1", "Precaution_2", "Precaution_3", "Precaution_4"]


def preprocess(text):
    text = text.lower().replace(" ", "_")
    tokens = word_tokenize(text)
    return set(tokens)


def predict_disease(user_input):
    user_symptoms = preprocess(user_input)

    best_match = None
    max_count = 0

    for _, row in symptom_df.iterrows():
        disease = row["Disease"]
        symptoms = set()

        for col in symptom_df.columns[1:]:
            symptom = str(row[col]).strip().lower()
            if symptom != "nan":
                symptoms.add(symptom)

        match_count = len(user_symptoms.intersection(symptoms))

        if match_count > max_count:
            max_count = match_count
            best_match = disease

    return best_match


def get_description(disease):
    result = desc_df[desc_df["Disease"] == disease]
    if not result.empty:
        return result.iloc[0]["Description"]
    return "No description available."


def get_precautions(disease):
    result = prec_df[prec_df["Disease"] == disease]
    if not result.empty:
        row = result.iloc[0]
        return [row["Precaution_1"], row["Precaution_2"], row["Precaution_3"], row["Precaution_4"]]
    return []


def chatbot():
    print("Medical Chatbot")
    print("Enter your symptoms separated by space (example: itching skin_rash)")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("Chatbot: Take care. Goodbye!")
            break

        disease = predict_disease(user_input)

        if disease:
            print(f"\nPossible Disease: {disease}")
            print("Description:", get_description(disease))
            print("Precautions:")

            for p in get_precautions(disease):
                print("-", p)
            print()
        else:
            print("Sorry, I could not identify the disease.\n")


if __name__ == "__main__":
    chatbot()