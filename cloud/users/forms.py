from django.contrib.gis import forms
from django.utils.translation import gettext as _

from apps.widgets.widgets import LocationInput

from .models import User



class UserCreateForm(forms.ModelForm):
 
    error_messages = {
	'duplicate_username': _("A user with that username already exists. "),
	'password_mismatch': _("The two password fields didn't match."),
    }

    userhandle = forms.RegexField(
	label=_("Userhandle"), 
        max_length=20,
	regex=r'^[\w.+-]+$',
	help_text=_("Required. 20 characters or less. Alphanumeric and (./+/-) only"),
	error_messages={
	    'invalid': _("This value may contain only letters, number an (./+/-/_) characters")
        }
    )

    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(
	label=_("Password confirmation"),
	widget=forms.PasswordInput,
	help_text=_("Enter the same password as above, for verification.")
    )

    location = forms.PointField(widget=LocationInput)

    class Meta:
	model = User
	fields = ("first_name", "last_name", "userhandle", "email", "location")

    def clean_username(self):
	username = self.cleaned_data["username"]
	try:
	    User._default_manager.get(username=username)
	except User.DoesNotExist:
	    return username
	raise forms.ValidationError(
	    self.error_messages['duplicate_username'],
	    code='duplicate_username',
	)

    def clean_password2(self):
	password1 = self.cleaned_data.get("password1")
	password2 = self.cleaned_data.get("password2")
	if password1 and password2 and password1 != password2:
	    raise forms.ValidationError(
	       self.error_messages['password_mismatch'],
	       code='password_mismatch',
	    )
	return password2

    def save(self, commit=True):
	user = super(UserCreateForm, self).save(commit=False)
	user.set_password(self.cleaned_data["password1"])
	if commit:
	  user.save()
	return user


