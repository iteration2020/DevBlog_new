from django import forms

class InputDataForm(forms.Form):
    age = forms.IntegerField(label='Возраст')
    sex = forms.ChoiceField(label='Пол', choices=[('M', 'Мужчина'), ('F', 'Женщина')])
    bp = forms.ChoiceField(label='Уровень артериального давления (АД)', choices=[('L', 'Низкий'), ('N', 'Нормальный'), ('H', 'Высокий')])
    cholesterol = forms.ChoiceField(label='Уровень холестерина', choices=[('L', 'Низкий'), ('N', 'Нормальный'), ('H', 'Высокий')])
    na_to_k = forms.FloatField(label='Соотношение натрия к калию (Na/K)')