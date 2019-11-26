from django import forms
from .models import User_Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = User_Profile
        fields = ['fname','lname','email','display_picture']