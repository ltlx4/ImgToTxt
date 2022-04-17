from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
import base64
import numpy as np
import pytesseract
import cv2


def index(request):
    return render(request, 'website/index.html')


@require_POST
def get_text(request):
    image = request.POST.get('image')
    if image:
        encoded_data = image.split(',')[1]
        nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        text = pytesseract.image_to_string(img)
        print(text)
        return HttpResponse(text)
    else:
        return HttpResponse('Sorry, Please insert an image first')