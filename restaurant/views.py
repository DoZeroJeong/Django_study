from rest_framework.views import APIView
from .Haksik import restaurant, dor_restaurant
from rest_framework.response import Response


# Create your views here.

class RestaurantView(APIView):

    def get(self, request):
        ddoock, il, rice, yang, noodle, faculty_menu = restaurant()
        breakfast, dinner = dor_restaurant()
        return Response({
            "뚝배기": ddoock,
            "일품": il,
            "덮밥": rice,
            "양식": yang,
            "면류": noodle,
            "교직원식단": faculty_menu,
            "조식": breakfast,
            "석식": dinner,
        })