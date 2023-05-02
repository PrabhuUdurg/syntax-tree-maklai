from django import forms


class InputForm(forms.Form):
    post = forms.CharField(label="Text", max_length=1000,
                           widget=forms.Textarea(attrs={'rows': 5}))
