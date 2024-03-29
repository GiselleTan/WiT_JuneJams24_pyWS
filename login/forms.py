from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password', 'email']
        widgets = {'password': forms.PasswordInput}
    