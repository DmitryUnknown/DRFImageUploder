from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadImageForm
from .models import Image


def upload_file(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Image(image_field=request.FILES['file'])
            instance.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadImageForm()
    return render(request, 'upload.html', {'form': form})
