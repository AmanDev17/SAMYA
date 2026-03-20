from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .utils import process_files
import os
from django.conf import settings
from django.http import HttpResponse
from pdf2image import convert_from_path


def index(request):
    if request.method == 'POST' and request.FILES.getlist('files'):
        fs = FileSystemStorage()
        folder = os.path.join(settings.MEDIA_ROOT, 'uploads')
        os.makedirs(folder, exist_ok=True)

        for file in request.FILES.getlist('files'):
            fs.save(os.path.join('uploads', file.name), file)

        # process files
        groups = process_files(folder)   # this is already a LIST

        request.session.flush()
        request.session['groups'] = groups   # this is already a LIST

        return redirect('result')

    return render(request, 'index.html')


def result(request):
    return render(request, 'result.html', {
        'groups': request.session.get('groups', []),
        'pairs': request.session.get('pairs', [])
    })


def preview(request):
    file_type = request.GET.get("type")

    if file_type == "pdf":
        pdf = request.GET.get("pdf")
        page = int(request.GET.get("page"))

        pdf_path = os.path.join(settings.MEDIA_ROOT, "uploads", pdf)
        pages = convert_from_path(pdf_path, first_page=page, last_page=page)

        img = pages[0]
        response = HttpResponse(content_type="image/jpeg")
        img.save(response, "JPEG")
        return response

    elif file_type == "image":
        file = request.GET.get("file")
        path = os.path.join(settings.MEDIA_ROOT, "uploads", file)

        if os.path.exists(path):
            with open(path, "rb") as f:
                return HttpResponse(f.read(), content_type="image/jpeg")

    return HttpResponse("No preview available")