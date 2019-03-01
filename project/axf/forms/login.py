from django import forms
#from ..models import

class LoginForm(forms.Form):
    username = forms.CharField(max_length=12, min_length=6, required=True, widget=forms.TextInput(attrs={'class':'c'}),
                               error_messages={'required':'用户账号不能为空', 'invalid':'格式错误'})
    passwd = forms.CharField(max_length=16, min_length=6, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    class Meta:
        pass