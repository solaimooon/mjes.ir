# from django import forms
#
# from rezervation.models import AvailableTime
#
#
# class AvailableTime_form(forms.ModelForm):
#     class Meta:
#         model = AvailableTime
#         fields = '__all__'
#         exclude = ('Hall',)
#
#         widgets = {
#             'start_time': forms.TimeInput(attrs={
#                 'type': 'time',
#                 'class': 'form-control',
#                 'id': 'start_time',
#             }),
#             'end_time': forms.TimeInput(attrs={
#                 'type': 'time',
#                 'class': 'form-control',
#                 'id': 'end_time',
#             }),
#         }
