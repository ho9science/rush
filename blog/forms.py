from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text',)

class SearchForm(forms.Form):
	srch = forms.CharField( required=True, label='search')

class GoldForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ()