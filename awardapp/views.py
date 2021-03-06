from django.shortcuts import render,redirect,HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import SiteForm,ProfileForm,VoteForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Site,Profile,AwardsProfiles,AwardsProjects
from .serializer import ProfileSerializer,ProjectSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly

# Create your views here.
# @login_required(login_url='/accounts/login/')

def landing(request):
    current_user = request.user
    sites = Site.get_all()
    return render(request,'landing.html',{'sites':sites})

def site(request,site_id):
    site = Site.objects.get(id = site_id)
    rating = round(((site.design + site.usability + site.content)/3),2)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid:
            if site.design == 1:
                site.design = int(request.POST['design'])
            else:
                site.design = (site.design + int(request.POST['design']))/2
            if site.usability == 1:
                site.usability = int(request.POST['usability'])
            else:
                site.usability = (site.design + int(request.POST['usability']))/2
            if site.content == 1:
                site.content = int(request.POST['content'])
            else:
                site.content = (site.design + int(request.POST['content']))/2
            site.save()
    else:
        form = VoteForm()
    return render(request,'site.html',{'form':form,'site':site,'rating':rating})


# @login_required(login_url='/accounts/login/')
def new_site(request):
    current_user = request.user
    if request.method == 'POST':
        form = SiteForm(request.POST, request.FILES)
        if form.is_valid():
            site = form.save(commit=False)
            site.user = current_user
            site.save()
        return redirect('landingPage')

    else:
        form = SiteForm()
    return render(request, 'new_site.html', {"form": form})

def profile(request):
    current_user = request.user
    sites = Site.objects.filter(profile=current_user)

    print(current_user)


    #
    # try:
    #     profile = Profile.objects.get(profile = current_user)
    # except ObjectDoesNotExist:
    #     return redirect('create-profile')
    return render(request, 'profile.html',{'sites':sites,'profile':profile})

def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = SiteForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.project = current_user
            profile.save()
        return redirect('Profile')
    else:
        form = ProfileForm()
    return render(request,'create_profile.html',{'form':form})

def search_results(request):

    if 'site' in request.GET and request.GET["site"]:
        search_term = request.GET.get("site")
        searched_sites = Site.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"sites": searched_sites})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def search_site(request,site_id):
    try :
        site = Site.objects.get(id = project_id)

    except ObjectDoesNotExist:
        raise Http404()
        # return render(request, 'no_project.html')

    return render(request, 'site-detail.html', {'site':site})

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = AwardsProfiles.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        permission_classes = (IsAdminOrReadOnly,)

class ProjectList(APIView):
    def get(self, request, format=None):
        all_project = AwardsProjects.objects.all()
        serializers = ProjectSerializer(all_project, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers =  ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        permission_classes = (IsAdminOrReadOnly,)

class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_profile(self, pk):
        try:
            return ProfileList.objects.get(pk=pk)
        except ProfileList.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        merch = self.get_profile(pk)
        serializers = ProfileSerializer(merch)
        return Response(serializers.data)

class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_project(self, pk):
        try:
            return ProjectList.objects.get(pk=pk)
        except ProjectList.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        merch = self.get_project(pk)
        serializers = ProjectSerializer(merch)
        return Response(serializers.data)
