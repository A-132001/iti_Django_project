from rest_framework.response import Response
from rest_framework.decorators import api_view
from track.models import Track
from rest_framework import status
from .serializer import Track_Serializer
@api_view(['GET','PUT','PATCH','DELETE'])
def Get_Update_Delete(req,id):
    if (req.method == 'GET'):
        trackobjs = Track.objects.all()
        #------without using serializtion----------
        # json_data = {}
        # for obj in trackobjs:
        #     json_data[obj.id]= obj.name
        # track_serializer = Track_Serializer(trackobjs,many=True)
        # return Response(data=track_serializer.data,status=status.HTTP_200_OK)
        #------clean code using serializtion----------
        return Response(data=Track_Serializer.get_track_by_id(id),status=status.HTTP_200_OK)
    elif (req.method == "PUT"):
        old_track = Track.objects.get(id=id)
        comming_update_track = Track_Serializer(data=req.data,instance=old_track)
        if comming_update_track.is_valid():
            comming_update_track.save()
            return Response(data={"message":"Updated successfuly"},status=status.HTTP_200_OK)
        