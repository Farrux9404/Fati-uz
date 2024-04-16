from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from api.paginations import ResultsSetPagination
from django.shortcuts import render
from rest_framework import generics
from .models import Dissertationabstract, Category, JournalUzbekistan
from .serializers import DissertationabstractSerializer, CategorySerializer, JournalUzbekistanSerializer


# position list and detail view

@swagger_auto_schema(methods=['get'], responses={200: DissertationabstractSerializer(many=True)}, tags=['user'])
@swagger_auto_schema(
    methods=['post'],
    request_body=DissertationabstractSerializer(),
    responses={200: DissertationabstractSerializer()},
    tags=['user'])
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def listUser(request):
    if request.method == 'POST':
        serializer = DissertationabstractSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    users = Dissertationabstract.objects.all().order_by('id')
    paginator = ResultsSetPagination()
    paginated_users = paginator.paginate_queryset(users, request)
    serializer = DissertationabstractSerializer(paginated_users, many=True, context={'request': request})
    return paginator.get_paginated_response(serializer.data)


@swagger_auto_schema(methods=['get'], responses={200: DissertationabstractSerializer()}, tags=['user'])
@swagger_auto_schema(methods=['delete'], tags=['user'])
@swagger_auto_schema(
    methods=['put'],
    request_body=DissertationabstractSerializer(),
    responses={200: DissertationabstractSerializer()},
    tags=['user'])
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detailUser(request, id):
    user = get_object_or_404(CustomUser, pk=id)
    if request.method == 'PUT':
        serializer = DissertationabstractSerializer(user, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=204)
    serializer = DissertationabstractSerializer(user, context={'request': request})
    return Response(serializer.data, status=200)

