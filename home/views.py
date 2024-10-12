from django.shortcuts import render
from home.models import *
from home.serializer import *
from rest_framework.decorators import APIView,api_view
from rest_framework.response import Response

# Create your views here.
class Enterstudentinformation(APIView):

    def post(self,request):
        serializer=studentserializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':404,'error':'invalid data provided'})
        serializer.save()
        return Response({'staus':200,'message':'success'})
 

class getonestudentdetails(APIView):
    def get(self,request,id):
        obj=student.objects.get(id=id)
        serializer=studentserializer(obj)
        return Response({'status':200,'data': serializer.data})
    

class getallstudent(APIView):

    def get(self,request):
        obj=student.objects.all()
        serializer=studentserializer(obj,many=True)

        return Response({'status':200,'data':serializer.data})

class deletestudent(APIView):

    def delete(self,request,id):
        obj=student.objects.get(id=id)
        obj.delete()
        return Response({'status':200,'message':'success'})

class updatestudent(APIView):

    def put(self,request,id):
        obj=student.objects.get(id=id)
        serializer=studentserializer(obj,data=request.data,partial=True)
        if serializer.is_valid():
             serializer.save()
             return Response({'status':200,'message':'success'})





    