from django.forms import ModelForm,ValidationError,DateInput
from .models import bookingmodel,signupmodel



class dateinput(DateInput):
    input_type='date'



class bookingform(ModelForm):
    class Meta:
        model=bookingmodel
        fields="__all__"
        widgets={
            'booking_date':dateinput(),
        }
        labels={
            'p_name':'Patient Name:',
        'p_phone':'Patient Phone:',
        'p_email':'Patient Email',
        'doc_name':'Doctor Name',
        'booking_date':'Booking Date',
        }
class signupform(ModelForm):
    def clean(self):
        cleaned_data=super().clean()
        fname=cleaned_data.get('fname')
        password=cleaned_data.get('password')
        re_password=cleaned_data.get('re_password')

        if fname[0]!='s':
            raise ValidationError({"some message"})
        if password!=re_password:
            raise ValidationError("Passwords must be same!!")
        return cleaned_data

    class Meta:
        model=signupmodel
        fields="__all__"
        labels={
            'fname':'First Name:',
        'lname':'Last Name:',
        'phone':'Phone Number:',
        'email':'E-mail:',
        'password':'Password:',
        're_password':'Re-Enter Password',
        }