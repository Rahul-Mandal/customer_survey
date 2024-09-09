from django.shortcuts import render, redirect
from .models import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def index(request):
    feedback = CustomerFeedback.objects.all()

    return render(request, 'surveys.html', {'feedbacks': feedback})

def customer_feedback(request, id):
    feedback = CustomerFeedback.objects.get(id = id)
    print(feedback)
    if request.method == 'POST':
        # feedback = CustomerFeedback.objects.create()
        for question in feedback.question.all():
            print(question, question.id)
            response_text = request.POST.get(f"response_{question.id}")
            selected_option_ids = request.POST.getlist(f"options_{question.id}")
            print(response_text)
            print(selected_option_ids)
        #     exit(0)

        #     response = CustomerResponse.objects.create(
        #         feedback=feedback,
        #         question=question,
        #         response_text=response_text if question.question_type in ["Text", "BigText"] else None
        #     )
            
        #     if selected_option_ids:
        #         selected_options = Options.objects.filter(id__in=selected_option_ids)
        #         response.selected_options.set(selected_options)
        
        # return redirect('thank_you')
    return render(request, 'survey.html', {'questions': feedback.question.all()})


def thank_you(request):
    return render(request, 'thank_you.html')

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED,HTTP_400_BAD_REQUEST
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class StudentApi(APIView):
    permission_classes = [IsAuthenticated] 
    def get(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many = True)
        return Response({'status': HTTP_200_OK, 'data':serializer.data})

class LoginApi(APIView):
    def post(self, request):
        data = request.data
        ser = LoginSerializer(data=data)
        if not ser.is_valid():
            return Response({'status': HTTP_400_BAD_REQUEST, 'data':ser.errors})
        username = ser.data['username']
        password = ser.data['password']
        user_obj = authenticate(username = username, password = password)
        if user_obj:
            token, _ = Token.objects.get_or_create(user = user_obj)
            print(token, _)
            return Response({'status': HTTP_200_OK, 'data':{'token': str(token)}})

        return Response({'status': HTTP_400_BAD_REQUEST, 'data':{}, 'msg':'invalid credentials'})

