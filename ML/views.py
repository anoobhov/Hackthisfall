import pickle
from django.shortcuts import render,redirect
from .forms import SymptomForm
import torch


# Create your views here.

with open('daignostic.pkl', 'rb') as file:
    data = pickle.load(file)
    model = data[0]  # BERT model
    tokenizer = data[1] 



def predict(request):
    if request.method == "POST":
        form = SymptomForm(request.POST)
        if form.is_valid():
            symptom1 = form.cleaned_data['symptom1']
            symptom2 = form.cleaned_data['symptom2']
            symptom3 = form.cleaned_data['symptom3']
            symptom4 = form.cleaned_data['symptom4']

            symptoms = [symptom1, symptom2, symptom3, symptom4]

        # Combine symptoms into a single text input
        symptoms_text = " ".join(symptoms)

        # Tokenize the input text
        inputs = tokenizer(
            symptoms_text, return_tensors="pt", padding=True, truncation=True
        )

        # Run the model on the tokenized input
        with torch.no_grad():
            outputs = model(**inputs)

        # Get the predicted label (assuming logits output)
        logits = outputs.logits

        # Get the class probabilities (softmax of logits)
        probabilities = torch.nn.functional.softmax(logits, dim=1)

        # Get the predicted class index (class with highest probability)
        predicted_class_index = torch.argmax(probabilities, dim=1).item()

        # Optionally: map the class index to a human-readable label (if you have this mapping)
        class_labels = ["Flu", "Cold", "COVID-19", "Malaria"]  # Example class labels

        # Safe check for class index to avoid IndexError
        if predicted_class_index < len(class_labels):
            predicted_class_label = class_labels[predicted_class_index]
        else:
            predicted_class_label = "Unknown Class"

        # Return the logits, predicted class, and probabilities
        response_data = {
            "predicted_class_index": predicted_class_index,
            "predicted_class_label": predicted_class_label,
            "logits": logits.tolist(),  # Convert logits to a list for JSON serialization
            "probabilities": probabilities.tolist(),  # Convert probabilities to a list for JSON
        }

        if predicted_class_index == 0:
            disease = "allergy"
        elif predicted_class_index == 1:
            disease = 'arthritis'

        elif predicted_class_index == 2:
            disease = 'arthritis'
        elif predicted_class_index == 3:
            disease = 'bronchial asthma'
        elif predicted_class_index == 4:
            disease = 'chicken pox'
        elif predicted_class_index == 5:
            disease = 'common cold'

        elif predicted_class_index == 6:
            disease = 'dengue'
        elif predicted_class_index == 7:
            disease = 'diabetes'
        elif predicted_class_index == 8:
            disease = 'drug reaction'
        elif predicted_class_index == 9:
            disease = 'fungal infection'
        elif predicted_class_index == 10:
            disease = 'gastroesophageal reflux disease'
        elif predicted_class_index == 11:
            disease = 'hypertension'
        elif predicted_class_index == 12:
            disease = 'impetigo'
        elif predicted_class_index == 13:
            disease = 'jaundice'
        elif predicted_class_index == 14:
            disease = 'malaria'
        elif predicted_class_index == 15:
            disease = 'migraine'
        elif predicted_class_index == 16:
            disease = 'peptic ulcer disease'
        elif predicted_class_index == 17:
            disease = 'pneumonia'
        elif predicted_class_index == 18:
            disease = 'psoriasis'
        elif predicted_class_index == 19:
            disease = 'typhoid'
        elif predicted_class_index == 20:
            disease = 'urinary tract infection'
        else:
            disease = 'varicose veins'
        


        return render(request, 'results.html', {'disease':disease})

            

    else:
        form = SymptomForm()
    return render(request, 'index.html', {'form': form})




    # "0": "allergy",
    # "1": "arthritis",
    # "2": "bronchial asthma",
    # "3": "cervical spondylosis",
    # "4": "chicken pox",
    # "5": "common cold",
    # "6": "dengue",
    # "7": "diabetes",
    # "8": "drug reaction",
    # "9": "fungal infection",
    # "10": "gastroesophageal reflux disease",
    # "11": "hypertension",
    # "12": "impetigo",
    # "13": "jaundice",
    # "14": "malaria",
    # "15": "migraine",
    # "16": "peptic ulcer disease",
    # "17": "pneumonia",
    # "18": "psoriasis",
    # "19": "typhoid",
    # "20": "urinary tract infection",
    # "21": "varicose veins"

