from datetime import datetime

from django.shortcuts import render

def index(request):
    return render(request, template_name='docBlog/index.html', context={'date': datetime.today()})