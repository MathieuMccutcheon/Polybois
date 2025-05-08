from django.shortcuts import render


from django.shortcuts import render

def index_principal_view(request):
    return render(request, "general/index_principal.html")



