from django import forms

from feedback.models import Feedback


class FeedbackForm(forms.ModelForm):
    phone = forms.RegexField(regex=r'^\+?\d{9,15}$')

    class Meta:
        model = Feedback
        fields = ['name', 'email', 'phone', 'comment']
        labels = {
            'name': 'Имя',
            'email': 'E-mail',
            'phone': 'Телефон',
            'comment': 'Комментарий'
        }
        help_texts = {
            'name': 'Иван Иванов',
            'email': 'example@email.com',
            'phone': '+79991112233',
            'comment': 'Введите здесь ваш комментарий'
        }
