import django_filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Pereval_added
from .serializers import PerevalSerializer, PerevalSubmitDataSerializer, PerevalSubmitDataUpdateSerializer

from rest_framework import status

from rest_framework.generics import RetrieveAPIView, UpdateAPIView, ListAPIView


class PerevalViewSet(ModelViewSet):
    queryset = Pereval_added.objects.all()
    serializer_class = PerevalSerializer


@api_view(['POST'])
def submit_data(request):
    serializer = PerevalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


class SubmitDataDetailView(RetrieveAPIView):
    queryset = Pereval_added.objects.all()
    serializer_class = PerevalSubmitDataSerializer


class SubmitDataUpdateView(UpdateAPIView):
    queryset = Pereval_added.objects.all()
    serializer_class = PerevalSubmitDataUpdateSerializer

    def update(self, request, *args, **kwargs):
        submit_data = self.get_object()

        if submit_data.status != 'new':
            message = 'Данные не могут быть отредактированы, поскольку данные не находятся в статусе "new".'
            return Response({'state': 0, 'message': message}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(submit_data, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({'state': 1})


class SubmitDataEmailUsers(ListAPIView):
    queryset = Pereval_added.objects.all()
    serializer_class = PerevalSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["users__email", ]



