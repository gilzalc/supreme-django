# api\views
import json
from django.shortcuts import render

from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from myapp.models import Book
from myapp.serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    '''
    DRF - API view implementing POST and GET
    '''
    if request.method == "GET":
        data = {}
        instance = Book.objects.all().order_by("?").first()
        if instance:
            data = BookSerializer(instance).data
        return Response(data)

    elif request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            print(instance)
            return Response(serializer.data)


def api_home_JSON_response(request, *args, **kwargs):
    '''
    Vanilla Django view for API request  JSON response
    '''
    data = dict()
    book_data = Book.objects.all().order_by("?").first()
    if book_data:
        author_name = book_data.author.name
        book_data = model_to_dict(book_data, fields=['id', 'title'])
        book_data['author'] = author_name
        data['book'] = book_data
        print('**', book_data)
    return JsonResponse(data)


def api_home_Text_response(request, *args, **kwargs):
    '''
    Vanilla Django view for API request  text response
    '''
    data = dict()
    book_data = Book.objects.all().order_by("?").first()
    if book_data:
        author_name = book_data.author.name
        book_data = model_to_dict(book_data, fields=['id', 'title'])
        print(book_data)
        book_data['author'] = author_name
        data['book'] = book_data
        print('**', book_data)
        json_data = json.dumps(data)
    return HttpResponse(json_data,
                        headers={'content-type': 'application/json'})
