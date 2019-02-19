from django.http import HttpResponse

# function that are called via the chosen path in the app file
def index(request):
    return HttpResponse("This is a bad request. Start with the music route.")


def music(request):
    return HttpResponse("King Princess, Ariana, Christine and the Queens")


def ari(request):
    return HttpResponse("Ariana Grande just released a killer album")


def king(request):
    return HttpResponse("King Princess writes songs about women loving women")


def chris(request):
    return HttpResponse("Chris is french")


