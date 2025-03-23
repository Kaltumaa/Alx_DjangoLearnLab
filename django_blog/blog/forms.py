from django import forms
from .models import Post, Comment
from taggit.forms import TagField, TagWidget  # ✅ Import TagWidget

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']  # ✅ Match the field name in the Comment model

class PostForm(forms.ModelForm):
    tags = TagField(widget=TagWidget(), required=False)  # ✅ Ensure TagWidget is used

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {  # ✅ Ensure widgets dictionary is present
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': TagWidget(attrs={'class': 'form-control'}),  # ✅ Explicit widget usage
        }

class SearchForm(forms.Form):
    query = forms.CharField(label="Search", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))  # ✅ Added Bootstrap styling
