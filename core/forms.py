from core.models import Profile, User
from django.forms import ModelForm

# class ProfileForm(ModelForm):
#     class Meta:
#         model=Profile
#         exclude=['uuid']


class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        exclude = ['uuid', 'courses', 'user']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self.instance.pk:
    #         self.fields['courses'].initial = self.instance.group_courses.all()

    # def save(self, commit=True):
    #     instance = super(ProfileForm, self).save(commit=False)
    #     instance.group_courses.set(self.cleaned_data['courses'])
    #     if commit:
    #         instance.save()
    #     return instance
