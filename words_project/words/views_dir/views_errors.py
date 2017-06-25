from django.shortcuts import render


def handler400(request):
    return render(request, 'words/errors/handler400.html')


def handler403(request):
    return render(request, 'words/errors/handler403.html')


def handler404(request):
    return render(request, 'words/errors/handler404.html')


def handler500(request):
    return render(request, 'words/errors/handler500.html')
