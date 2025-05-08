from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required
def index_principal_view(request):
    return render(request, "general/index_principal.html")



