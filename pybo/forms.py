from django import forms
from django.forms import widgets
from pybo.models import Question, Answer
# from django.db.models import fields

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class':'form-control'}),
        #     'content': forms.Textarea(attrs={'class':'form-control', 'rows':10}),
        # }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }