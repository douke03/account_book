from django import forms
from cms.models.todo_model import ToDo


class ToDoForm(forms.ModelForm):

    class Meta:
        model = ToDo
        fields = ['title', 'text', 'correspondence_contents', 'correspondence_situation',
                  'priority', 'deadline', 'resolved_date', 'is_complete', ]
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': ''}),
            'text': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': '', 'rows': 3}),
                # attrs={'class': 'form-control', 'placeholder': '', 'rows': 3, 'readonly': True}),
            'correspondence_contents': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': '', 'rows': 3}),
            'correspondence_situation': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': '', 'rows': 3}),
            'priority': forms.Select(
                attrs={'class': 'form-control'}),
            'deadline': forms.DateInput(
                attrs={'class': 'form-control', 'placeholder': ''}),
            'resolved_date': forms.DateInput(
                attrs={'class': 'form-control', 'placeholder': ''}),
            'is_complete': forms.CheckboxInput(
                attrs={'class': ''}),
        }
