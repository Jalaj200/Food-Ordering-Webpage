from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-input'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'form-input'}))
    phone_number = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'placeholder': 'Phone Number (optional)', 'class': 'form-input'}))
    
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'phone_number']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply form-input class to username and password fields as well
        self.fields['username'].widget.attrs.update({'placeholder': 'Username', 'class': 'form-input'})
        self.fields['username'].help_text = None
        # UserCreationForm defines password fields, let's update their classes
        if 'password' in self.fields:
            self.fields['password'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Password'})
        # Specifically targeting UserCreationForm's built-in fields (usually they are named like password11, password12 etc)
        for field_name in self.fields:
            if 'password' in field_name.lower() or 'pass' in field_name.lower():
                self.fields[field_name].widget.attrs.update({'class': 'form-input'})
                self.fields[field_name].help_text = None

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.email = self.cleaned_data.get('email')
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                phone_number=self.cleaned_data.get('phone_number')
            )
        return user


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-input'}))
    remember_me = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={'class': 'form-checkbox'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-input'})
        self.fields['password'].widget.attrs.update({'class': 'form-input'})

from .models import Address

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['first_name', 'email']

class UserProfileForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'class': 'form-input'}))
    
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'profile_picture']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street_address', 'city', 'state', 'postal_code', 'is_default']
        widgets = {
            'street_address': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Street Address'}),
            'city': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'State'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Postal Code'}),
            'is_default': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }
