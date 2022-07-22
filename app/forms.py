from django import forms

from app.tasks import send_email_task

class ReviewForm(forms.Form):
    name = forms.CharField(
        label="FirstName",
        min_length=6,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3", 
                "placeholder": "FirstName",
                "id": "form-firstname"
            }
        )
    )
    
    email = forms.EmailField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3", 
                "placeholder": "E-mail",
                "id": "form-email"
            }
        )
    )
    
    review = forms.CharField(
        label="Review",
        widget=forms.Textarea(
            attrs={
                "class": "form-control", 
                "rows": "5"
            }
        ) 
    )
    
    def send_email(self):
        return send_email_task.delay(
            self.cleaned_data["name"], self.cleaned_data["email"], self.cleaned_data["review"]
        )
    