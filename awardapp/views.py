from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Site,Profile
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='/accounts/login/')
def landing(request):
    
    # current_user = request.user
    # sites = Site.objects.all()
    return render(request,'landing.html')

# def site(request,site_id):
#     try:
#         site = Site.objects.get(id = site_id)
#     except ObjectDoesNotExist:
#         raise Http404()
#     return render(request,'site-detail.html',{'site':site})
#
# # @login_required(login_url='/accounts/login/')
# def new_site(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = SiteForm(request.POST, request.FILES)
#         if form.is_valid():
#             site = form.save(commit=False)
#             site.profile = current_user
#             site.save()
#         return redirect('landingPage')
#
#     else:
#         form = SiteForm()
#     return render(request, 'new_site.html', {"form": form})
#
# def profile(request):
#     current_user = request.user
#     sites = Site.objects.filter(profile=current_user)
#
#     print(current_user)
#
#
#     #
#     # try:
#     #     profile = Profile.objects.get(profile = current_user)
#     # except ObjectDoesNotExist:
#     #     return redirect('create-profile')
#     return render(request, 'profile.html',{'sites':sites,'profile':profile})
#
# def create_profile(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = SiteForm(request.POST, request.FILES)
#         if form.is_valid():
#             profile = form.save(commit = False)
#             profile.project = current_user
#             profile.save()
#         return redirect('Profile')
#     else:
#         form = ProfileForm()
#     return render(request,'create_profile.html',{'form':form})
#
# def search_results(request):
#
#     if 'project' in request.GET and request.GET["project"]:
#         search_term = request.GET.get("project")
#         searched_sites = Site.search_by_title(search_term)
#         message = f"{search_term}"
#
#         return render(request, 'search.html',{"message":message,"sites": searched_sites})
#
#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'search.html',{"message":message})
#
# def search_site(request,site_id):
#     try :
#         site = Site.objects.get(id = project_id)
#
#     except ObjectDoesNotExist:
#         raise Http404()
#         # return render(request, 'no_project.html')
#
#     return render(request, 'site-detail.html', {'site':site})
