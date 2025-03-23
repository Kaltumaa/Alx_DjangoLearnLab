from django import forms
from .models import Post
from .models import Comment
from taggit.forms import TagField
from taggit.forms import TagWidget  # ✅ Import TagWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']  # ✅ Match the field name in the Comment model


class PostForm(forms.ModelForm):
    tags = TagField(required=False)  # Allow users to add tags

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
class SearchForm(forms.Form):
    query = forms.CharField(label="Search", required=False)

