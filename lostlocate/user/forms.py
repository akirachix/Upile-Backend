from django import forms

class VerificationCodeForm(forms.Form):
    code = forms.CharField(max_length=36, label='Enter the code sent to your email')