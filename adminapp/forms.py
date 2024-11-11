import pytz
from django import forms
from .models import Task, Feedback
from .models import StudentList


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentList
        fields = ['Register_Number', 'Name']


class UploadFileForm(forms.Form):
    file = forms.FileField()


class FeedbackForm:
    pass

from django import forms

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'mobile_no', 'comments']


from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'address']  # Specify the fields to include in the form
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter phone number', 'class': 'form-control'}),
            'address': forms.Textarea(attrs={'placeholder': 'Enter address', 'class': 'form-control'}),
        }


def add_contact():
    return None