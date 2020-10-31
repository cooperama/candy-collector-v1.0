from django.shortcuts import render, redirect



# ------------------- STATIC
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


# ------------------- CANDY
def candy_index(request):
    candy = Candy.objects.all()
    context = {
        'candy': candy
    }
    return render(request, 'candy/index.html', candy)


