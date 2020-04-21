from django import forms
from .models import Day

class DayCreateForm(forms.ModelForm): # Django特有の自動バリデーションフォーム
  class Meta:
    model = Day
    fields = '__all__' # ('title', 'text', 'date')...
    