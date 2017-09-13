"""cms models form."""
from django.forms import ModelForm
from cms.models import ToDoList


class ToDoListForm(ModelForm):
    """ToDoList's form."""

    class Meta:
        """meta."""

        model = ToDoList
        fields = ('title', 'text', 'is_complete', 'created_by', 'updated_by',)
