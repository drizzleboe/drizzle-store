from dataclasses import fields
import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import cart, profession, address, contact, product,user,cart
import datetime

#create your form here
#class registerForm(UserCreationForm):
    #class Meta:
     #   model = User
      #  fields = ['username','email','password1','password2']

class sign_in(forms.Form):
    username=forms.CharField(label ='email yangu')
    passwd = forms.CharField(
        label='password',
        widget= forms.PasswordInput(
            attrs={
                   'class':'fa-password',
                   'id':'user-password'    
            }
        )
    )
    def clean(self):
        cleaned_data = super().clean()
        _email = self.cleaned_data.get('username')
        pwd1 = self.cleaned_data.get('passwd')
        db = user.objects.filter(email__iexact = _email)
        if db.exists():
            found_user = user.objects.get(email = _email)
            if found_user.password != pwd1:
                raise forms.ValidationError("password uliyo weka sio sahihi!")   
        else:
            raise forms.ValidationError('email uliyoingiza haijasajiliwa!')

class registerForm(forms.Form):
    firstname = forms.CharField(label='jina la kwanza')
    lastname = forms.CharField(label='jina la pili')
    email = forms.EmailField(label='email')
    
    passwd = forms.CharField(
        label='password',
        widget= forms.PasswordInput(
            attrs={
                   'class':'fa-password',
                   'id':'user-password'    
            }
        )
    )
    
    passwd2 = forms.CharField(
        label='rudia password',
        widget= forms.PasswordInput(
            attrs={
                   'class':'fa-password',
                   'id':'user-password'    
            }
        )
    )
    def clean(self):
        cleaned_data = super().clean()
        _email = self.cleaned_data.get('email')
        db = user.objects.filter(email__iexact = _email)

        pwd1 = self.cleaned_data.get('passwd')
        pwd2 = self.cleaned_data.get('passwd2')
        if db.exists():
            raise forms.ValidationError("""email hii imekwisha sajiliwa! tumia email 
            nyingine""")    
        elif pwd1 != pwd2:
            raise forms.ValidationError("password ulizo weka hazifanani!")   


class other_details(forms.ModelForm):
    class Meta:
        model = product
        fields = ['title','description','image','more']
class profession_form(forms.ModelForm):
    class Meta:
        model = profession
        fields = '__all__'
class contact_form(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'
class otherproduct(forms.Form):
    title = forms.CharField(label='huduma ninayohitaji')
    desc = forms.CharField(label='maelezo zaidi')
    phone  = forms.CharField(label='namba yangu ya simu')
    email= forms.EmailField(label='email yangu')
class order_form(forms.Form):
    usernames = forms.CharField(label="majina yangu")
    email = forms.EmailField()
    phone = forms.IntegerField(label="Namba ya simu")
class comments(forms.Form):
    comment = forms.CharField(label='maoni',widget=forms.Textarea(attrs={'name':'maoni','rows':3,'cols':60}))
class subscriberForm(forms.Form):
    email = forms.EmailField(
        label = 'email'
    )
class cartForm(forms.ModelForm):
    class Meta:
        model = cart
        fields = '__all__'

class contact_us_form(forms.Form):
    phone = forms.CharField(label='namba ya simu')
    email = forms.EmailField(label='email')
    date = forms.DateField(required=False, label='Ni lini unapenda tuwasiliane na wewe')