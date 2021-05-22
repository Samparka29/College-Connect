from django.forms import ModelForm
from .models import Answer,Question,Userdetail,JobPosting,Notes
from django import forms

class PostingForm(ModelForm):
    class Meta:
        model=JobPosting
        fields=('title','Company_Name','JOB_ID','Description','Basic_Qualification')
        widgets={
            'title':forms.TextInput(attrs={'class':'title','placeholder':'enter title of the jpb','required':'required'}),
            'JOB_ID':forms.TextInput(attrs={'class':'JOB_ID','placeholder':'enter the ID of the job','required':'required'}),
            'Company_Name':forms.TextInput(attrs={'class':'Company_Name','placeholder':'enter name of comapany','required':'required'}),
            'Description':forms.Textarea(attrs={'class':'Description','placeholder':'enter description','required':'required'}),
            'Basic_Qualification':forms.Textarea(attrs={'class':'Basic_Qualification','placeholder':'add basic qualification required','required':'required'})
        }

class AnswerForm(ModelForm):    
    class Meta:
        model=Answer 
        fields = ('detail',)
        widgets={       
            'detail':forms.Textarea(attrs={'class':'details','placeholder':'You can reply to question here','required':'required'})  
        }

class QuestionForm(ModelForm):
    class Meta:
        model=Question 
        fields = ('title','detail','tags')

        widgets={
            'title':forms.TextInput(attrs={'id':'titleid','class':'title','placeholder':'enter title of question','required':'required'}),
            'detail':forms.Textarea(attrs={'id':'detailsid','class':'details','placeholder':'enter detail of question','required':'required'}),
            'tags':forms.Textarea(attrs={'id':'tagid','class':'tags','placeholder':'enter tags related to question','required':'required'})
        }

class UserDetail(ModelForm):
    class Meta:
        model=Userdetail
        fields=('first_name','last_name','username','email')

        widgets={
            'first_name':forms.TextInput(attrs={'class':'inputtext'}),
            'last_name':forms.TextInput(attrs={'class':'inputtext'}),
            'username':forms.TextInput(attrs={'class':'inputtext'}),
            'email':forms.TextInput(attrs={'class':'inputtext'}),
        }

class NotesForm(ModelForm):
    class Meta:
        model=Notes
        fields=('teacher','subject','pdf')

        widgets={
            'teacher':forms.TextInput(attrs={'class':'','placeholder':'Name'}),
            'subject':forms.TextInput(attrs={'class':'','placeholder':'Subject'}),
            
        }
