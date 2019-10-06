from rest_framework.views import APIView
from .Haksik import restaurant
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response


# Create your views here.

class RestaurantView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'restaurant/list.html'

    def get(self, request):
        if '식단' in restaurant():
            message = restaurant()
            return Response({
                'message': message,
            })
        else:
            ddoock, il, rice, yang, noodle, faculty_menu = restaurant()
            return Response({
                "뚝배기": ddoock,
                "일품": il,
                "덮밥": rice,
                "양식": yang,
                "면류": noodle,
                "교직원 식당": faculty_menu,
            })