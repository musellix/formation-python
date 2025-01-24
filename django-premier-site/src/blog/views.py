from django.shortcuts import render


def index(request):
    return render(request, template_name='blog/index.html')

def article(request, numero_article):
    print(numero_article)
    return render(request, template_name=f'blog/article_{numero_article}.html')
