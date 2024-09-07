from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from openai import OpenAI
from .bots import translate_bot


class TranslateAPIView(APIView):
    def post(self, request):
        user_message = request.data.get("message")
        chatgpt_response = translate_bot(user_message)
        return Response({"message": chatgpt_response})
