from django.shortcuts import render
import numpy as np
import pickle
import os

model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
with open(model_path, 'rb') as f:
    model, scaler = pickle.load(f)

def home(request):
    return render(request, 'index.html')

def predict(request):
    if request.method == 'POST':
        area = float(request.POST.get('area'))
        rooms = int(request.POST.get('rooms'))
        age = int(request.POST.get('age'))
        input_data = np.array([[area, rooms, age]])
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)[0]
        return render(request, 'index.html', {'prediction': round(prediction, 2)})
    return render(request, 'index.html')