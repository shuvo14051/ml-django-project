from django.urls import path
from . import views

urlpatterns = [
    path("", views.predictors, name="predictors"),
    # path("result", views.features, name="result"),
]
