#from socket import fromshare
#from unittest.util import _MAX_LENGTH
from django import forms


class TodoListForm(forms.Form):
    text = forms.CharField(max_length=45,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Enter todo e.g Grocery Shopping', 'aria-label': 'Todo', 'aria-describedby': 'add-btn'}))
