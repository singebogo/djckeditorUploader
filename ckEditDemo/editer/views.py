from django.shortcuts import render
from .models import  SPUModel


# Create your views here.
def index(request):
    all_obj = list(SPUModel.objects.all().all().values('name','sales','desc_pack'))

    return render(request, 'index.html', {'all': all_obj})