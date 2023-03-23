import sys
from django.conf import settings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

settings.configure(
   
   INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nutrient',
    ], 
    ROOT_URLCONF=__name__,
    STATIC_URL = 'static/',

   TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
],
    ALLOWED_HOSTS = ['10.0.3.2','192.168.43.127','localhost', ],
    DEBUG=True,
    SECRET_KEY = 'django-insecure-*1ux8*cpx09qe14ot+35b=+l9wkl-o23r4yfwf#@m%opguxc)n',
   

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } },


    MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
),

)

from django.http import JsonResponse
from time import gmtime, strftime
from rest_framework.views import APIView
from rest_framework import parsers
from django.urls import path
from chatbot import ChatBot
from django.contrib import admin

# Create your views here.
class ChatView(APIView):
  parser_classes = (parsers.JSONParser,)

  def post(self, request, *args, **kwargs):
    print("result :",request.data)
    try:
        msg = request.data["msg"]
        print("msg :",msg)
        res = ChatBot.getBot().response(msg)
        print("res:",res)
        time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        return JsonResponse({
		    "status":"success",
            "desc": "Success",
            "ques": msg,
            "res": res,
            "time": time
        })
    except Exception as e:
         return JsonResponse({"status":"success","response":"Sorry I am not trained to do that yet..."})
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', ChatView.as_view(),name="chatbot"),
]


from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
if __name__ == "__main__":
   from django.core.management import execute_from_command_line
   execute_from_command_line(sys.argv)