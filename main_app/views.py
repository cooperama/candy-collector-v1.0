from django.shortcuts import render, redirect



# ------------------- STATIC
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


# ------------------- CANDY
def candy_index(request):
    all_candy = Candy.objects.all()
    context = {
        'all_candy': all_candy
    }
    return render(request, 'candy/index.html', all_candy)


