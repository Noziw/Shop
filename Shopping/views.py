from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class UserView(APIView):

    def post(self, request):
        serializers = UserSRl(data=request.data)
        if serializers.is_valid():
            user = serializers.save()
            access = AccessToken.for_user(user)
            refresh = RefreshToken.for_user(user)
            return Response({
                "user":serializers.data,
                "access":str(access),
                "refresh":str(refresh)
            })
        else:
            return Response(serializers.errors)
