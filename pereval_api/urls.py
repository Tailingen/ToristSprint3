from django.urls import path
from .views import submit_data, SubmitDataEmailUsers, SubmitDataUpdateView, PerevalViewSet, SubmitDataDetailView

urlpatterns = [
    path('submitData/', SubmitDataEmailUsers.as_view(), name='pereval_list'),
    path('submitData/create/', submit_data, name='submit_data'),
    path('submitData/<int:pk>', SubmitDataDetailView.as_view(), name='get_data'),
    path('submitData/<int:pk>/update/', SubmitDataUpdateView.as_view(), name='update_data'),
]