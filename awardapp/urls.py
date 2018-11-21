from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.landing,name='landingPage'),
    # url(r'^sites/(\d+)',views.site,name ='sites'),
    # url(r'^new/project$', views.new_site, name='new-site'),
    # url(r'^profile/',views.profile,name = 'Profile'),
    # url(r'^create-profile/$',views.create_profile,name = 'create-profile'),
    # url(r'^search/', views.search_results, name='search_results'),
    # url(r'^site-detail/(\d+)',views.search_site,name = 'site-detail'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
