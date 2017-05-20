from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Score
from .serializers import ScoreSerializer


# Create your views here.

# Homepage
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# REST API
class ScoreView(APIView):

    def get(self, request):
        scores = Score.objects.all()
        serializer = ScoreSerializer(scores, many=True)

        return Response(serializer.data)

    def post(self, request):
        score = ScoreSerializer(data=request.data)

        if score.is_valid():
            score.save()
            return Response(score.data, status=status.HTTP_201_CREATED)
        else:
            return Response(score.errors, status=status.HTTP_400_BAD_REQUEST)