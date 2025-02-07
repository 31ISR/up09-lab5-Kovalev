from django.shortcuts import render

# Импорт функции `render` из модуля `django.shortcuts`.
# Эта функция используется для отображения HTML-шаблонов
# с передачей в них данных.


def about(req):
    # Определение функции `about`, которая принимает один параметр `req`.
    # Обычно `req` — это объект запроса (request), передаваемый Django при вызове функции.

    return render(req, "about.html")
def home(req):
    # Определение функции `about`, которая принимает один параметр `req`.
    # Обычно `req` — это объект запроса (request), передаваемый Django при вызове функции.

    return render(req, "home.html")




