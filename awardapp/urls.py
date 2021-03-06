from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.landing,name='landingPage'),
    url(r'^sites/(\d+)',views.site,name ='sites'),
    url(r'^new/site$', views.new_site, name='new-site'),
    url(r'^profile/',views.profile,name = 'Profile'),
    url(r'^create-profile/$',views.create_profile,name = 'create-profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^site-detail/(\d+)',views.search_site,name = 'site-detail'),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'^api/project/$', views.ProjectList.as_view()),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
