from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse

# Create your views here.


class GetMessageView(APIView):

    def get(self, request):
        get = request.GET
        a = get.get('a')
        print(a)
        d = {
            'status': 1,
            'message': 'success',
        }
        return JsonResponse(d)
        