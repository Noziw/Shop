from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from datetime import datetime

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
        

class LoginView(APIView):
    def post(self,request):
        Username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username = Username, password = password).first()
        if user:
            serializers = LoginSRL(data=request.data)
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
            return Response('bunday user yoq')
        

class AccountView(APIView):
    def get(self, request, id):
        user = User.objects.filter(id = id).first()
        serializers = AccountSRL(user)
        return Response(serializers.data)
    
    def patch(self, request, id):
        user = User.objects.filter(id = id).first()
        if user:
            user.card = request.data['card']
            user.adress = request.data['adress']
            serializers = AccountSRL(instance = user,data = request.data, partial = True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            else:
               return Response(serializers.errors)
        else:
            return Response('bunday user yoq')
        
    def delete(self,request, pk):
        pass



class AddProductView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self,request, id):
        admin = Admin.objects.filter(id = id).first()
        if admin:
            serializers = ProductSRL(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            else:
                return Response(serializers.errors)
        else:
            return Response('siz admin emasiz!!!')




class GetProductView(APIView):
    def get(self,request):
        serializers = ProductSRL(Product, many=True)
        return Response(serializers.data)
    

class OrderView(APIView):
    def post(self,request):
        id = request.data.get('product')

        serializers = OrderSRL(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)
        


class AdminView(APIView):
    def post(self,request):
        Username = request.data.get('username')
        password = request.data.get('password')
        user = Admin.objects.filter(username = Username, password = password).first()
        if user:
            access = LoginSRL(data=request.data)
            if serializers.is_valid():
                access = serializers.save()
                refresh = AccessToken.for_user(user)
                serializers = RefreshToken.for_user(user)
                return Response({
                "access":serializers.data,
                "refresh":str(access),
                "admin":serializers.data
             })
        else:
            return Response('bunday user yoq')
        


class AdminGetOrderEditView(APIView):
    
    def get(self, request, id):
        order = Order.objects.filter(id = id).first()
        if order:
            serializers = OrderSRL(order, many = True)
            return Response(serializers.data)
        else:
            return Response("Bunday buyurtma mavjud emas")
        

    def patch(self, request, id):
        order = Order.objects.filter(id = id).first()
        if order:
            serializers = OrderSRL(instance=order, data=request.data, partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            else:
                return Response(serializers.errors)
        else:
            return Response("Bunday buyurtma mavjud emas")




class AdminGetOrder(APIView):
    def get(self,request, id):
        admin = admin.objects.filter(id = id).first()
        if admin:
            order = Order.objects.all()
            if order:
                serializers = OrderSRL(order, many=True)
                return Response(serializers.data)
            else:
                return Response('bizda hali buyrtma mavjud emas')
        else:
            return Response('siz buyurtmani korish huquqiga ega emasiz')


class GetOrderUserView(APIView):
    def get(self, request, id):
        user = User.objects.filter(id=id).first()
        if user:
            orders = Order.objects.filter(user=user.id)
            if orders:
                summa = 0
                for order in orders:
                    if order.status == "ochiq":
                        product = Product.objects.filter(id = order.product).first()
                        narx = product.cost
                        payment = order.hajm * narx
                        summa += payment
                return Response({"MSG":f"Sizning buyurtmalaringizni umumiy narxi{summa}"})
            else:
                return Response("Sizda buyurtma topilmadi")
        else:
            return Response("Siz hali ro'yhatdan o'tmagansiz")
        


class GetOrderInfoAdminView():
    def get(self,request,id):
        admin = admin.objects.filter(id = id).first()
        if admin:
            order = Order.objects.all()
            srlorder = []
            for order in order:
                if order.date == datetime.today():
                    srlorder.append(order)
                    if srlorder:
                        serializers = OrderSRL(srlorder, many = True)
                        return Response(serializers.data)
                    else:
                        return Response('order topilmadi')
                else:
                    return Response("sizga malumotga ruxsat yoq")