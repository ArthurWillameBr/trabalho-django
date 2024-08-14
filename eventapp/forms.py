from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

        labels = {
            'titulo': 'Título',
            'tipo': 'Tipo',
            'data_inicio': 'Data de Início',
            'local': 'Local',
            'data_fim': 'Data de Fim',
            'cidade': 'Cidade',
            'horario': 'Horário',
            'preco': 'Preço',
            'quantidade': 'Quantidade',
            'imagem': 'Imagem',
        }

        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Show de Música'}),
            'tipo': forms.TextInput(attrs={'placeholder': 'Música'}),
            'data_inicio': forms.DateInput(attrs={'placeholder': '2024-08-11', 'type': 'date'}),
            'local': forms.TextInput(attrs={'placeholder': 'Auditório Central'}),
            'data_fim': forms.DateInput(attrs={'placeholder': '2024-08-12', 'type': 'date', 'required': False}),
            'cidade': forms.TextInput(attrs={'placeholder': 'General Sampaio'}),
            'horario': forms.TimeInput(attrs={'placeholder': '19:00', 'type': 'time'}),
            'preco': forms.NumberInput(attrs={'placeholder': '100.00', 'required': False}),
            'quantidade': forms.NumberInput(attrs={'placeholder': '100', 'required': False}),
            'imagem': forms.ClearableFileInput(attrs={'multiple': False}),
        }
