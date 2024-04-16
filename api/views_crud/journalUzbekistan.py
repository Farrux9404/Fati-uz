from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.paginations import ResultsSetPagination
from django.shortcuts import render
from rest_framework import generics
from library.models import JournalUzbekistan
from library.serializers import JournalUzbekistanSerializer


@swagger_auto_schema(methods=['get'], responses={200: JournalUzbekistanSerializer(many=True)}, tags=['user'])
@swagger_auto_schema(
    methods=['post'],
    request_body=JournalUzbekistanSerializer(),
    responses={200: JournalUzbekistanSerializer()},
    tags=['user'])
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def journal_listUser(request):
    if request.method == 'POST':
        serializer = JournalUzbekistanSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    journal = JournalUzbekistan.objects.all().order_by('id')
    paginator = ResultsSetPagination()
    paginated_users = paginator.paginate_queryset(journal, request)
    serializer = JournalUzbekistanSerializer(paginated_users, many=True, context={'request': request})
    return paginator.get_paginated_response(serializer.data)


@swagger_auto_schema(methods=['get'], responses={200: JournalUzbekistanSerializer()}, tags=['user'])
@swagger_auto_schema(methods=['delete'], tags=['user'])
@swagger_auto_schema(
    methods=['put'],
    request_body=JournalUzbekistanSerializer(),
    responses={200: JournalUzbekistanSerializer()},
    tags=['user'])
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def journal_detailUser(request, id):
    journal = get_object_or_404(JournalUzbekistan, pk=id)
    if request.method == 'PUT':
        serializer = JournalUzbekistanSerializer(journal, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        journal.delete()
        return Response(status=204)
    serializer = JournalUzbekistanSerializer(journal, context={'request': request})
    return Response(serializer.data, status=200)
