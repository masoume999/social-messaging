from django import forms
from authentication.models import CustomUser
from .models import Chat

class CreateChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['name', 'type', 'members']
        widgets = {
            'type': forms.RadioSelect(),
            'members': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(CreateChatForm, self).__init__(*args, **kwargs)
        self.fields['members'].queryset = CustomUser.objects.exclude(pk=user.pk)

        # Add a custom attribute to the members field for type checking in JavaScript
        self.fields['members'].widget.attrs['data-chat-type'] = '1'

        excluded_type = 1
        self.fields['type'].widget.choices = [(key, value) for key, value in self.fields['type'].widget.choices if key != excluded_type]

    def clean(self):
        cleaned_data = super().clean()
        chat_type = cleaned_data.get('type')
        members = cleaned_data.get('members')

        # Additional validation based on chat type, if needed
        if chat_type == 'direct_message' and members.count() != 1:
            raise forms.ValidationError("Direct message chat should have exactly one member.")

        return cleaned_data
