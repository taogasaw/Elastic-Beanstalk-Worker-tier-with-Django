from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'put_log', views.put_log, name='put_log'),
    url(r'^$', views.root, name='root'),
]
