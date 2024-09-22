from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from taggit.forms import TagWidget


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
from .models import Post

class PostForm(forms.Form):
    class Meta:
        model = Post
        fields = ("title", "content", "image", "tags")
        
        widgets = {
            'tags': TagWidget()
        }
      
    def clean_content(self):
        content = self.cleaned_data.get("content")
        if not content:
            raise forms.ValidationError("Content is required")
        return content





from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if not content or len(content) < 5:
            raise forms.ValidationError("Comment must be at least 5 characters long")
        return content
    