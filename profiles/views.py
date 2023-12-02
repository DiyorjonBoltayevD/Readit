from django.shortcuts import render


def profiles(request):
    ctx = {}
    return render(request, 'profiles/about.html', ctx)
