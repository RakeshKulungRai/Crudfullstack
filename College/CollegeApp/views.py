from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from CollegeApp.Serializers import CollegeSerializer
from CollegeApp.models import College

@csrf_exempt
def studentApi(request,id=0):
    if request.method=="GET":
        college = College.objects.all()
        student_serializer = CollegeSerializer(college,many=True)
        return JsonResponse(student_serializer.data,safe=False)
    elif request.method=='POST':
        student_data= JSONParser().parse(request)
        student_serializer = CollegeSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse('Added Successfully',safe=False)
        return JsonResponse('Failed to Add',safe=False)
    
    elif request.method=='PUT':
        student_data=JSONParser().parse(request)
        college=College.objects.get(id=id)
        student_serializer=CollegeSerializer(college,data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        college=College.objects.get(id=id)
        college.delete()
        return JsonResponse("Deleted Successfully",safe=False)