from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from rest_framework.decorators import api_view 
 
from rest_framework.response import Response
from api.serializers import postModelSerializer,commentModelSerializer
from api.models import Post, Comment

# Create your views here.
@api_view(['GET'])
def APIoverview(requests):
    api_urls = {

     'List' : ' /task-list/' ,
'View' : '/detail-view/',
'Create' : 'task-create/' ,
'Update': '/task-update/<str>',
'Delete' : 'task-delete/<str>' ,

   }
    
    return Response(api_urls)
 
@api_view(['GET'])
def task_list(request):
    query = Post.objects.all().order_by('-id').values()
    serializer = postModelSerializer(query, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def task_create(request):
    
    serializer = postModelSerializer(data=request.data)
    print(serializer)

    if serializer.is_valid():
        serializer.save()
    else:
        print("not valid")
    return Response(serializer.data)

@api_view(['GET'])
def one_task(request, pk):
    query = Post.objects.get(id=pk)
    serializer = postModelSerializer(query, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def task_update(request, pk):
    query = Post.objects.get(id=pk)
    
    serializer = postModelSerializer(instance=query,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

 
@api_view(['DELETE', 'GET'])
def task_delete(request, pk):
    print(pk)
    query = Post.objects.get(id=pk)
    print(query)
    query.delete()

    return Response("Item Deleted Successfully")



@api_view(['POST'])
def comment(request):
    
    serializer = commentModelSerializer(data=request.data)
    print(serializer)

    if serializer.is_valid():
        serializer.save()
    else:
        print("not valid")
    return Response(serializer.data)


@api_view(['GET'])
def showcomment(request):
    query = Post.objects.all().order_by('-id').values()
    serializer = commentModelSerializer(query, many=True)
    return Response(serializer.data)

   


