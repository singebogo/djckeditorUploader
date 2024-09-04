from django.shortcuts import render
from editer import models


# Create your views here.
def index(request):
    all_obj = list(models.SPUModel.objects.all().all().values('name','sales','desc_pack'))

    return render(request, 'index.html', {'all': all_obj})