from django import forms


class InputForm(forms.Form):
    post = forms.CharField(label="Text", max_length=1000)