from django import forms

from mailinglist.models import MailingList, Subscriber


class SubscriberForm(forms.ModelForm):
    mailing_list = forms.ModelChoiceField(
        widget=forms.HiddenInput,
        queryset=MailingList.objects.all(),
        disabled=True,
    )

    class Meta:
        model = Subscriber
        fields = ['mailing_list', 'email', ]