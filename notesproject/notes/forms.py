from django import forms

from .models import Note

from django.contrib.auth.models import User

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']  # ❌ Do NOT include 'author' here!

    
class SingupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
class NoteForm(forms.ModelForm):
    recipient = forms.ModelChoiceField(queryset=User.objects.all(), required=False, label="Send To (Optional)")

    class Meta:
        model = Note
        fields = ['title', 'content', 'recipient']