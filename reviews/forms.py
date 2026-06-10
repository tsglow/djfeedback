from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'review_text', 'rating']
        labels = {
            'user_name': 'Your Name',
            'review_text': 'Your Feedback',            
        }
        error_messages = {
            'user_name':{
                "required" : "Your name must not be empty",
                "max_length" : "Your name should be shorter than that!"
            },
            'review_text': {                
                "max_length" : "Your review is too long"
            }
        }
