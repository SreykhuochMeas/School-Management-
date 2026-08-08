from django import forms
from .models import Student, Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'age', 'gender', 'date_of_birth', 'score', 'is_active', 'courses']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'courses': forms.CheckboxSelectMultiple(),
        }

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and (age < 10 or age > 100):
            raise forms.ValidationError("Age must be between 10 and 100.")
        return age

    def clean_score(self):
        score = self.cleaned_data.get('score')
        if score is not None and (score < 0 or score > 100):
            raise forms.ValidationError("Score must be between 0 and 100.")
        return score

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and len(name) < 3:
            raise forms.ValidationError("Name must contain at least three characters.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = Student.objects.filter(email=email)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Email must remain unique.")
        return email


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and len(name) < 2:
            raise forms.ValidationError("Course name must contain at least two characters.")
        return name