from django.shortcuts import render, redirect
from .forms import DayCreateForm
from .models import Day

def index(request):
  context = {
    'day_list': Day.objects.all() # Dayモデルのデータ全抽出
  }
  return render(request, 'diary/day_list.html', context)

def add(request):
  # 送信内容をもとにフォームを作る。POSTじゃなければ、空のフォーム
  form = DayCreateForm(request.POST or None)

  # method = POST、つまり送信ボタン押下時、入力内容が問題なければ
  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('diary:index')
  context = {
    'form': DayCreateForm()
  }
  return render(request, 'diary/day_form.html', context)
