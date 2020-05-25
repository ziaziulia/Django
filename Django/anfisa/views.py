from django.http import HttpResponse
from django.shortcuts import render
from . import anfisa


def about(request):
    return render(request, 'templates/about.html')


def index(request):
    html = ''
    if request.method == 'POST':
        # извлекаем из POST-запроса вопрос пользователя
        query = request.POST['query']

        # допишите ваш код здесь
        answer = anfisa.process_query(query)

        # полученный из anfisa.py ответ оборачиваем в HTML-теги, будет нарядно
        html = f'<mark>{answer}</mark>'

    # подготовьте словарь context, чтобы вывести информацию в шаблон
    context = {
        'response': html,  # сюда передайте HTML-код с ответом Анфисы
        'where': request.path  # передаём абсолютный адрес страницы
    }

    # добавьте словарь context третьим аргументом
    return render(request, 'templates/index.html', context)