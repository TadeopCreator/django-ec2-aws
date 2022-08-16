from django.shortcuts import render

def index(request):
    dic_ml = None

    if request.method == 'POST':
        dic_ml = { 'text': request.POST['textarea'] }

    return render(request, "index.html", {"dic_ml": dic_ml})