from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import google.generativeai as genai
import json

from openai import OpenAI
from .models import Chat, Message

# =========================================
# LANDING PAGE
# =========================================

def index(request):
    return render(request, 'index.html')


# =========================================
# HOME PAGE
# =========================================

@login_required(login_url='login_page')
def home(request):
    return render(request, 'home.html')


# =========================================
# SIGNUP PAGE
# =========================================

def signup(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobilenumber")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # PASSWORD CHECK
        if password != confirm_password:

            messages.error(request, "Passwords do not match")

            return redirect('signup')

        # EMAIL CHECK
        if User.objects.filter(email=email).exists():

            messages.error(request, "Email already registered")

            return redirect('signup')

        # CREATE USER
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=name
        )

        user.save()

        messages.success(request, "Account created successfully")

        return redirect('login_page')

    return render(request, 'signup.html')


# =========================================
# LOGIN PAGE
# =========================================

def login_page(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('home')

        else:

            messages.error(request, "Invalid Email or Password")

            return redirect('login_page')

    return render(request, 'login.html')


# =========================================
# LOGOUT PAGE
# =========================================

def logout_page(request):

    logout(request)

    return redirect('login_page')


# =========================================
# COURSES PAGE
# =========================================

def courses(request):
    return render(request, 'courses.html')


def languages(request):
    return render(request, 'languages.html')


def roadmap(request):
    return render(request, 'roadmap.html')


def about(request):
    return render(request, 'about.html')


def fullstackdevelopment(request):
    return render(request, 'fullstackdevelopment.html')


def datanalysiscourse(request):
    return render(request, 'datanalysiscourse.html')

def logout_page(request):

    logout(request)

    return redirect('index')

@login_required(login_url='login_page')
def chatboat(request):

    chats = Chat.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(request, 'chatboat.html', {
        'chats': chats
    })

@csrf_exempt
@login_required(login_url='login_page')
def chatbot(request):

    if request.method == 'POST':

        try:

            data = json.loads(request.body)

            user_message = data.get('message', '')

            chat_id = data.get('chat_id')

            # NEW CHAT
            if not chat_id:

                chat = Chat.objects.create(
                    user=request.user,
                    title=user_message[:30]
                )

                chat_id = chat.id

            else:

                chat = Chat.objects.get(id=chat_id)

            # SAVE USER MESSAGE
            Message.objects.create(
                chat=chat,
                sender='user',
                text=user_message
            )

            # AI API
            client = OpenAI(
                api_key=settings.GROK_API_KEY,
                base_url="https://api.x.ai/v1",
            )

            response = client.chat.completions.create(
                model="grok-3-mini",
                max_tokens=500,
                messages=[
                    {
                        "role": "user",
                        "content": user_message
                    }
                ]
            )

            bot_reply = response.choices[0].message.content

            # SAVE BOT MESSAGE
            Message.objects.create(
                chat=chat,
                sender='bot',
                text=bot_reply
            )

            return JsonResponse({
                'reply': bot_reply,
                'chat_id': chat_id
            })

        except Exception as e:

            return JsonResponse({
                'reply': str(e)
            })

    return JsonResponse({
        'reply': 'Invalid request'
    })

client = OpenAI(
    api_key=settings.GROK_API_KEY,
    base_url="https://api.x.ai/v1",
)
#=========================================
# CHATBOT API
# =========================================

