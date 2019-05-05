from django.contrib.auth.models import User
from .models import Question,Choice
from django import forms


#For Adding and Compare User information using this Class
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password','email')


#For Adding Question require a format on form which follow following labels which also set
#in activeuser_ques.html
class ActiveQuesForm(forms.Form):
    
    question_text = forms.CharField(label ='Enter question')
    choiceFirst= forms.CharField(label ='Choice 1')
    choiceSecond= forms.CharField(label ='Choice 2')
    choiceThird= forms.CharField(label ='Choice 3')
    
    