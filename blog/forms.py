# Core imports.
from django import forms

# Third-party imports.
from ckeditor.widgets import CKEditorWidget

from .models import Post, Comment
from .validators import slug_validator


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'category', 'content', 'draft', 'publish_time', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'slug': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'category': forms.Select(attrs={'class': 'form-control mb-3'}),
            'content': CKEditorWidget(),
            'draft': forms.CheckboxInput(attrs={'class': 'form-control mb-3'}),
            'publish_time': forms.SelectDateWidget(attrs={'class': 'form-control mb-3'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file mb-3'}),
        }

    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        slug_validator(slug)
        return slug


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'content', 'draft', 'publish_time')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'category': forms.Select(attrs={'class': 'form-control mb-3'}),
            'content': forms.Textarea(attrs={'class': 'form-control mb-3', 'cols': 90, 'style': 'resize:none'}),
            'draft': forms.CheckboxInput(attrs={'class': 'form-control mb-3'}),
            'publish_time': forms.SelectDateWidget(attrs={'class': 'form-control mb-3'}),
        }
