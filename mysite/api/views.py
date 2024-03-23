# api\views
import json
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from myapp.models import Book
from myapp.serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, mixins, viewsets
from django.shortcuts import get_object_or_404


class MyModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # lookup_field = 'pk'


class BookDeleteAPIView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'


class BookUpdateAPIView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

    # def update(self, instance, validated_data):
    #     # Update author data if provided
    #     author_data = validated_data.pop('author', None)
    #     if author_data:
    #         author_instance = instance.author
    #         for key, value in author_data.items():
    #             setattr(author_instance, key, value)
    #         author_instance.save()
    #     # Update book instance fields
    #     for key, value in validated_data.items():
    #         setattr(instance, key, value)
    #     instance.save()
    #     return instance


class BookMixinView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                    mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update( request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class BookListCreateAPIView(generics.ListCreateAPIView):
    """
    When a GET request is sent to the API endpoint associated with
    BookListCreateAPIView, the view will return a list of existing book objects.
    When a POST request is sent to the same API endpoint, the view will create
    a new book object based on the data provided in the request body.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        content = serializer.validated_data.get('content') or None
        title = serializer.validated_data.get('title')
        print('******')
        if content is None:
            content = title + ' content vers'
        serializer.save(content=content)
        # TODO


#         Create book and reference an already existing Author
#         by pk or by name.


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


@api_view(["GET", "POST"])
def book_alt_view(request, pk=None, *args, **kwargs):
    '''
    Confusing!!
    '''
    if request.method == "GET":
        if pk is not None:
            # Detail view
            print("Detail mode *****")
            obj = get_object_or_404(Book, pk=pk)
            data = BookSerializer(obj, many=False).data
            return Response(data)
        else:
            print("List mode******")
            queryset = Book.objects.all()
            data = BookSerializer(queryset, many=True).data
            return Response(data)

    elif request.method == "POST":
        print("Create mode *****")
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            content = serializer.validated_data.get('content') or None
            title = serializer.validated_data.get('title')
            if content is None:
                content = title + ' content vers'
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({'Invalid': 'Not Good Data'})
