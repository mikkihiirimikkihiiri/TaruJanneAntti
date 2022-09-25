from django import forms

class MessageForm(forms.Form):
    message_text = forms.CharField(label='Message', max_length =160)
    def _str_(self):
        return self.message_text