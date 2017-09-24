from django.forms import ModelForm
from cms.models.todo_model import ToDo


class ToDoForm(ModelForm):

    class Meta:

        model = ToDo
        fields = ('title', 'text', 'situation', 'priority',
                  'is_complete', 'updated_by',)
