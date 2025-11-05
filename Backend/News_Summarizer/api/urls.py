from django.urls import path
from .views import SummarizerView

urlpatterns = [
    path('summarize/', SummarizerView.as_view(), name='summarize'),
]
