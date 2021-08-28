from django import forms

class CreateTodoForm(forms.Form):
    todo = forms.CharField(label='Tarefa', max_length=150)