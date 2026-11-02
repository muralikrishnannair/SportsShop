from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from SportsApp.models import CategoryDb,ProductDb
from SportsApp.serializers import CategorySerializer,ProductSerializer


class CategoryListCreateView(APIView):

    def get(self, request):
        qs=CategoryDb.objects.all()
        serializer_instance=CategorySerializer(qs, many=True)

        return Response(data=serializer_instance.data)


    def post(self, request):
        form_data=request.data
        serializer_instance=CategorySerializer(data=form_data)

        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            qs=CategoryDb.objects.create(**actual_data)

            return Response(data=CategorySerializer(qs).data, status=status.HTTP_201_CREATED)

        else:
            return Response(data=serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk):
        qs=get_object_or_404(CategoryDb, id=pk)
        serializer_instance=CategorySerializer(qs)

        return Response(data=serializer_instance.data)


    def put(self, request, pk):
        qs=get_object_or_404(CategoryDb, id=pk)
        serializer_instance=CategorySerializer(qs, data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()

            return Response(data=serializer_instance.data)

        else:
            return Response(data=serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        qs=get_object_or_404(CategoryDb, id=pk)
        qs.delete()

        return Response(data={
            "Message":"Category deleted successfully...!"
        })


class ProductListCreateView(APIView):

    def get(self, request):
        qs=ProductDb.objects.all()

        category_id=request.query_params.get('category')

        if category_id:
            qs=qs.filter(category_id=category_id)

        serializer_instance=ProductSerializer(qs, many=True)

        return Response(data=serializer_instance.data)


    def post(self, request):
        form_data=request.data
        serializer_instance=ProductSerializer(data=form_data)

        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            qs=ProductDb.objects.create(**actual_data)

            return Response(data=ProductSerializer(qs).data, status=status.HTTP_201_CREATED)

        else:
            return Response(data=serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk):
        qs=get_object_or_404(ProductDb, id=pk)
        serializer_instance=ProductSerializer(qs)

        return Response(data=serializer_instance.data)


    def put(self, request, pk):
        qs=get_object_or_404(ProductDb, id=pk)
        serializer_instance=ProductSerializer(qs, data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()

            return Response(data=serializer_instance.data)

        else:
            return Response(data=serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        qs=get_object_or_404(ProductDb, id=pk)
        qs.delete()

        return Response(data={
            "Message":"Product deleted successfully...!"
        })