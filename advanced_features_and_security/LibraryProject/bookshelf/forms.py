from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date']
    
    def clean_author(self):
        author = self.cleaned_data['author']
        return author
    
class ExampleForm(forms.Form):
    title = forms.CharField(max_length=200) 
    author = forms.CharField(max_length=200)
    publication_date = forms.DateField()
    