from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView
from .serializers import *
from .models import *

class MahsulotlarAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        mahsulotlar = Mahsulot.objects.filter(sotuvchi__user=request.user)
        ser = MahsulotSerializer(mahsulotlar,many=True)
        return Response(ser.data)
    def post(self,request):
        serializer = MahsulotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ombor=Sotuvchi.objects.get(user=request.user))
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class MahsulotAPIView(APIView):
    def delete(self,request,pk):
        mahsulot = Mahsulot.objects.get(id=pk,sotuvchi__user=request.user)
        mahsulot.delete()
        return Response({"deleted":True})
    def put(self,request,pk):
        mahsulot = Mahsulot.objects.get(id=pk,sotuvchi__user=request.user)
        ser = MahsulotSerializer(mahsulot,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'info':"masulot ozgartirildi","detail":ser.data})
        return Response(ser.errors)


class MijozlarAPIView(APIView):
    def get(self,request):
        mijozlar = Mijoz.objects.all()
        ser = MijozSerializer(mijozlar,many=True)
        return Response(ser.data)
    def post(self,request):
        serializer = MijozSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class UserAPIView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self,request):
        serializer = UserSerializer(User.objects.all(),many=True)
        return Response(serializer.data)

class SotuvchiAPIView(APIView):
    def get(self,request):
        serializer = SotuvchiSerializer(Sotuvchi.objects.all(),many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = SotuvchiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)