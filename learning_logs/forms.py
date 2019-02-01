from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """Модель формы для задания темы"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    """Модель для создания записей по темам"""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
