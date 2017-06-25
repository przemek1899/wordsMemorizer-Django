
from django.conf.urls import url
from ocr import views

urlpatterns = (
    url(r'^$', views.upload_image),
)
