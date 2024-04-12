from django.shortcuts import render,redirect


def error_404_view(request, exception):
    print("asawfs")

    return render(request, '404.html')