from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.api_add, name = 'api_add'),
    path('predict/', views.predict, name = 'predict'),
    # path('predict/', views.IRIS_Model_Predict.as_view(), name = 'predict'),
    

]