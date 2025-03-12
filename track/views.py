from django.shortcuts import render,redirect
from .models import Track
from .decorators import require_auth

@require_auth
def Tracklist(req):
    # tracks = Track.objects.all()
    tracks = Track.objects.filter(isactive=True)
    context={"tracks":tracks}
    return render(req,"track/tracklist.html",context)

@require_auth
def AddTrack(req):
    if req.method == "POST":
        Track.objects.create(name=req.POST["track_name"],
                              department=req.POST["track_department"],
                              location=req.POST["track_location"])
    return render(req,"track/addtrack.html")

@require_auth
def UpdateTrack(req,id):
    track = Track.objects.get(id=id)
    context = {'track':track}
    if req.method == "POST":
        Track.objects.filter(id=id).update(name=req.POST["track_name"],
                              department=req.POST["track_department"],
                              location=req.POST["track_location"])
        return redirect("track_list")
    return render(req,"track/updatetrack.html",context)

def DeleteTrack(req,id):
    track = Track.objects.get(id=id)
    track.isactive = False
    track.save()
    return redirect("track_list")
    