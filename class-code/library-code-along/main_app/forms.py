from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["first_name", "last_name", "is_best_seller"]
        labels = {
            "first_name": "First name",
            "last_name": "Last name",
            "is_best_seller": "Best-selling author?",
        }
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Toni"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Morrison"}),
            "is_best_seller": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
