from django import forms
from .models import AddCourse

from django import forms
from .models import FacultyPost
from .models import AddCourse


class AddCourseFrom(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = ['student', 'course', 'section']

from django import forms
"""from .models import Marks"""

class FacultyPostForm(forms.ModelForm):
    class Meta:
        model = FacultyPost
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'cols': 50}),
        }
        labels = {
            'title': 'Blog Title',
            'content': 'Write Your Blog',
        }

from .models import Marks

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = ['student', 'course', 'section']


class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'course', 'marks']