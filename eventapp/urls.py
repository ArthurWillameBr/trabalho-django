from django.urls import path
from . import views
from django.views.generic import RedirectView



urlpatterns = [
    path('adicionar/', views.eventFormView, name='event_url'),
    path('eventos/', views.showEventView, name='show_url'),
    path('atualizar/<int:id>/', views.updateEventView, name='update_url'),
    path('deletar/<int:id>/', views.deleteEventView, name='delete_url'),
    path('', RedirectView.as_view(url='/adicionar/', permanent=False)),
]  
