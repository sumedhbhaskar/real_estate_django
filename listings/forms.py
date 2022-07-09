from dataclasses import fields
from django import forms
from .models import Listings

class createlisting(forms.ModelForm):
    class Meta:
        model = Listings
        fields = [
            "title","price","num_beds","num_baths","square_footage","address","image"
        ]