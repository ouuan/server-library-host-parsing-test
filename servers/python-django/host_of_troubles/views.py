# host_header_app/views.py
from django.http import HttpRequest, HttpResponse

def show_host_header(request: HttpRequest):
    return HttpResponse(f"[{request.get_host()}]", content_type="text/plain")
