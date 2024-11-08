from django import forms

class SymptomForm(forms.Form):
    symptom1 = forms.CharField(label="Symptom 1", max_length=15)
    symptom2 = forms.CharField(label="Symptom 2", max_length=15)
    symptom3 = forms.CharField(label="Symptom 3", max_length=15)
    symptom4 = forms.CharField(label="Symptom 4", max_length=15)
