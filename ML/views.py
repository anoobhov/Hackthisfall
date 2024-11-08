import pickle
from django.shortcuts import render,redirect
from .forms import SymptomForm

# Create your views here.

with open('daignostic.pkl', 'rb') as file:
    model = pickle.load(file)



def predict(request):
    if request.method == "POST":
        form = SymptomForm(request.POST)
        if form.is_valid():
            symptom1 = form.cleaned_data['symptom1']
            symptom2 = form.cleaned_data['symptom2']
            symptom3 = form.cleaned_data['symptom3']
            symptom4 = form.cleaned_data['symptom4']

            symptoms = [symptom1, symptom2, symptom3, symptom4]

            result = model.predict([symptoms])

            return render(request, 'result.html', {'result': result})

            

    else:
        form = SymptomForm()
    return render(request, 'index.html', {'form': form})




