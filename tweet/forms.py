from django import forms

class TweetForm(forms.Form):
    description = forms.CharField(max_length=140)
    
    
    