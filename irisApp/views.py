from django.shortcuts import render
from joblib import load

model = load("savedModels/model.joblib")
# Create your views here.
def predictors(request):
    if request.method == "POST":
        sepal_length = request.POST.get('sepal_length')
        sepal_width = request.POST.get('sepal_width')
        petal_length = request.POST.get('petal_length')
        petal_width = request.POST.get('petal_width')

        y_pred = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])
        if y_pred[0] == 0:
            y_pred = 'Setosa'
        elif y_pred[0] == 1:
            y_pred = 'Verscicolor'
        else:
            y_pred = 'Virginica'
            
        return render(request, "main.html", {'result':y_pred})
    return render(request, "main.html")
