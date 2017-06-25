# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from ocr.forms import UploadImageFileForm

from PIL import Image
from pytesseract import image_to_string


def upload_image(request):

    if request.method == 'POST':
        form = UploadImageFileForm(request.POST, request.FILES)
        if form.is_valid():
            language = form.cleaned_data['language']  # TODO use selected language
            image_scanned_content = image_to_string(Image.open(request.FILES['file']))
            return render(request, 'ocr/upload_image.html', {'image_form': form,
                                                             'image_scanned_content': image_scanned_content})

    form = UploadImageFileForm()
    return render(request, 'ocr/upload_image.html', {'image_form': form})
