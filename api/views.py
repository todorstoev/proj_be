
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Form
from .serializers import FormSerializer


class FormViewSet(APIView):

    serializer_class = FormSerializer
    queryset = Form.objects.all().order_by('name')

    def get(self, request, format=None):
        print('============================================')
        snippets = Form.objects.all()
        serializer = FormSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data['name'],
            'address': request.data['address'],
            'email': request.data['email'],
            'country': request.data['country'],
            'file': request.data['file']
        }

        serializer = FormSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
