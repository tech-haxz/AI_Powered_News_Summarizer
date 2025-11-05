from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SummarizerSerializer
from .utils import summarize_article

class SummarizerView(APIView):
    def get(self, request):
        # Write code for Fetching News from news API
        return Response({"message": "Welcome to the News Summarizer API. Please POST a URL to summarize."}, status=status.HTTP_200_OK)
    

    def post(self, request):
        serializer = SummarizerSerializer(data=request.data)
        if serializer.is_valid():
            url = serializer.validated_data['url']
            result = summarize_article(url)
            return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
