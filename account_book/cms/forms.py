"""cms models form."""
from django.forms import ModelForm
from cms.models.todo_model import ToDo


class ToDoForm(ModelForm):
    """ToDoList's form."""

    class Meta:
        """meta."""

        model = ToDo
        fields = ('title', 'text', 'situation', 'priority',
                  'is_complete', 'created_by', 'updated_by',)
