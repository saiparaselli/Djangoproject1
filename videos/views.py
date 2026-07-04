from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from . forms import VideoForm
from . models import Video



@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def add_video(request):

    if request.method == "POST":

        form = VideoForm(request.POST, request.FILES)

        if form.is_valid():

            video = form.save(commit=False)

            video.uploaded_by = request.user

            video.save()

            return redirect('view_videos')

    else:

        form = VideoForm()

    return render(request, 'add_video.html', {'form': form})

@login_required(login_url='login')
def view_videos(request):

    videos = Video.objects.all().order_by('-created_at')

    return render(request, 'view_videos.html', {'videos': videos})



@login_required(login_url='login')
def play_video(request, id):

    video = get_object_or_404(Video, id=id)

    return render(request, 'play_video.html', {'video': video})



@login_required(login_url='login')
def update_video(request, id):

    video = get_object_or_404(Video, id=id)

    if video.uploaded_by != request.user:

        return redirect('view_videos')

    if request.method == "POST":

        form = VideoForm(
            request.POST,
            request.FILES,
            instance=video
        )

        if form.is_valid():

            form.save()

            return redirect('view_videos')

    else:

        form = VideoForm(instance=video)
        return render(request,'update_video.html',{'form': form})
    
@login_required(login_url='login')
def delete_video(request, id):

    video = get_object_or_404(Video, id=id)

    if video.uploaded_by != request.user:

        return redirect('view_videos')

    video.delete()

    return redirect('view_videos')