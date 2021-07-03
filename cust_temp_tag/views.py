from django.shortcuts import render

# Create your views here.
# def greeting_view(request):
#     return render(request, 'simple_tag_template.html', {'message':'Hey there', 'username':'Sador'})


def greeting_view(request):
    books = {
        'Python books':'Luth',
        'Java':'Kelly',
        'problem solving':'Bradly',
    }
    return render(request, 'simple_tag_template.html', {'username':'Sador', 'books':books})