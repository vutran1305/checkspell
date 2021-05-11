from django import forms


class Text(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 20}))
