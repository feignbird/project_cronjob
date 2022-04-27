from django.contrib.auth import get_user_model
from cronjob_app.serializers import UserSerializer
from rest_framework import viewsets, pagination
from cronjob_app.cron import make_user
# Create your views here.

class GeneralPagination(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

User = get_user_model()

class UserView(viewsets.ModelViewSet):
    pagination_class = GeneralPagination
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    http_method_names = ["get"]