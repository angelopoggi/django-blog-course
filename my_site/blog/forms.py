from django import forms
from .models import PostComments

class CommentsForm(forms.ModelForm):
    class Meta:
        model = PostComments
        exclude = ["post"]
        labels = {
            "user_name": "Your Name",
            "user_email": "Your Email",
        }
        error_message = {
            "user_name": {
                "required" : "You must specify a user name!"
            },
            "comment": {
                "required" : "You need to write something!"
            }
        }
