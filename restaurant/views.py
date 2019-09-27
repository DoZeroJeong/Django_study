from rest_framework.views import APIView
from .Haksik import restaurant
from rest_framework.response import Response


# Create your views here.

class RestaurantView(APIView):

    def get(self, request):
        ddoock, il, rice, yang, noodle, faculty_menu = restaurant()
        print(faculty_menu)
        return Response({"뚝배기": ddoock,
                         "일품": il,
                         "덮밥": rice,
                         "양식": yang,
                         "면류": noodle,
                         "교직원 식당": faculty_menu,
                         })