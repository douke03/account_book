from django import forms
from cms.models.todo_model import ToDo


class ToDoCreateForm(forms.ModelForm):

    class Meta:
        model = ToDo
        fields = ['title', 'text', 'correspondence_contents', 'correspondence_situation',
                  'priority', 'deadline', 'resolved_date', ]
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', }),
            'text': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}),
            'correspondence_contents': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}),
            'correspondence_situation': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}),
            'priority': forms.Select(
                attrs={'class': 'form-control'}),
            'deadline': forms.DateInput(
                attrs={'class': 'form-control pull-right', 'id': 'datepicker', }),
            'resolved_date': forms.DateInput(
                attrs={'class': 'form-control', }),
        }
