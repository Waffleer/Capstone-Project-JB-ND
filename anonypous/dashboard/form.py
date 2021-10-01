
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . models import student

class newUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(newUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class newStudentForm():
    bio = forms.Textarea()

    class Meta:
        model = student
        fields = ("bio")

    def save(self, commit=True):
        user = super(newStudentForm, self).save(commit=False)
        user.student.bio = self.cleaned_data["bio"]
        if commit:
            student.save()
        return user