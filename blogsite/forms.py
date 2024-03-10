from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm
from django import forms
from .models import User,blog,comments,replies
import datetime

class writeCommentForm(forms.ModelForm):
    class Meta:
        model=comments
        fields=['body',]
    body = forms.CharField(widget=forms.TextInput(attrs={'placeholder':f'Write your comment here...'}))

class writeReplyForm(forms.ModelForm):
    class Meta:
        model=replies
        fields=['body',]
    body = forms.CharField(widget=forms.TextInput(attrs={'placeholder':f'Write your reply here...'}))


class createBlogForm(forms.ModelForm):
    class Meta:
        model = blog
        exclude = ('downvotes','upvotes','commentIDs','authorid','publish_date')
    quote = '"There is no greater agony than bearing an untold story inside you." \n- Maya Angelou'
    caption = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':"Give your blog a caption!"}))
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder':f'{quote}'}))
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email",)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'text-input-box'}))
    password = forms.CharField(widget=forms.PasswordInput())

class updateBlogForm(forms.ModelForm):
    class Meta:
        model = blog
        exclude = ('downvotes','upvotes','commentIDs','authorid','publish_date')
    caption = forms.CharField(max_length=50,widget=forms.TextInput())
    body = forms.CharField(widget=forms.Textarea())

YEAR_CHOICES = [str(r) for r in range(1900, datetime.date.today().year+1)]

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('name','bio','occupation','avatar','birthday','city','country')
    name = forms.CharField(max_length=50)
    bio = forms.Textarea()
    occupation = forms.CharField(max_length=70)
    birthday = forms.DateField(widget=forms.SelectDateWidget(years=YEAR_CHOICES))
    city = forms.CharField(max_length=30)
    country = forms.CharField(max_length=40)

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'text-input-box'}))
    password = forms.CharField(widget=forms.PasswordInput())
