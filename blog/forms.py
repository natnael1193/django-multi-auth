from django import forms
from .models import Blog


class AddBlog(forms.ModelForm):
    # title = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control"
    #         }
    #     )
    # )
    # description = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={
    #             "class": "form-control"
    #         }
    #     )
    # )
    # slug = forms.SlugField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control"
    #         }
    #     )
    # )
    # published = forms.DateTimeField(
    #     widget=forms.DateTimeInput(
    #         attrs={
    #             "class": "form-control",
    #             'type':'hidden',
                
    #         }
    #     )
    # )
    # image = forms.ImageField(
    #     widget=forms.FileInput(
    #         attrs={
    #             "class": "form-control"
    #         }
    #     )
    # )

    class Meta:
        model = Blog
        fields = "__all__"
