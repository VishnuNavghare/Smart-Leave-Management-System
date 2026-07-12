from django import forms
from .models import Leave


class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave

        fields = [
            "leave_type",
            "from_date",
            "to_date",
            "reason",
        ]

        widgets = {
            "leave_type": forms.Select(
                attrs={"class": "form-select"}
            ),

            "from_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control"
                }
            ),

            "to_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control"
                }
            ),

            "reason": forms.Textarea(
                attrs={
                    "rows": 4,
                    "class": "form-control"
                }
            ),
        }