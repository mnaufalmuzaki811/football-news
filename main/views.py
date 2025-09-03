from django.shortcuts import render

def show_main(request):
    context = {
        'npm': '2406428794',
        'name': 'Muhammad Naufal Muzaki',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)